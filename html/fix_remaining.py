import re, os, time, io, sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, line_buffering=True)

img_dir = '/workspace/html/img'
html_dir = '/workspace/html'
trae_api_base = 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image'

BANNER_W, BANNER_H = 1368, 600
CONTENT_W, CONTENT_H = 1368, 768

hero_banner_images = set()
hero_pattern = re.compile(r'rsb-hero[^}]*?background-image\s*:\s*url\([\'"]?(img/[^\'")]+)[\'"]?\)', re.DOTALL)
for fn in os.listdir(html_dir):
    if not fn.endswith('.html'): continue
    with open(os.path.join(html_dir, fn), encoding='utf-8') as f:
        c = f.read()
    for m in hero_pattern.finditer(c):
        hero_banner_images.add(os.path.basename(m.group(1)))

targets = [
    'reflective-noise-barrier-be6407e4.webp',
    'reflective-sound-barrier-steel-panel-installation-eede7f05.webp',
    'residential-community-noise-protection-housing-d9912071.webp',
    'residential-noise-barriers-community-garden-353b2b0e.webp',
    'residential-sensitive-highway-hybrid-noise-barrier-c58e7da0.webp',
    'solar-noise-barrier-project-pv-highway-1c717f65.webp',
    'solar-photovoltaic-noise-barrier-highway-pv-modules-4c67288e.webp',
    'solar-photovoltaic-noise-barrier-pv-modules-f0f8ad55.webp',
    'solar-pv-integrated-noise-barriers-04f918be.webp',
    'urban-arterial-road-solar-noise-wall-7ab27b7d.webp',
    'yukings-noise-barrier-free-quotation-engineer-474c6f32.webp',
    'yukings-noise-barrier-terms-of-service-legal-feb253ad.webp',
    'yukings-privacy-policy-data-protection-gdpr-d9613db8.webp',
    'semi-enclosed-u-shape-noise-barrier-highway-railway-06ed9585.webp',
    'semi-enclosed-u-shape-noise-wall-cantilever-cover-plate-installation-358fec1e.webp',
]

def extract_prompt(fname):
    m = re.match(r'(.+)-([a-f0-9]{8})\.webp$', fname)
    return m.group(1) if m else None

def fetch_raw(prompt, max_retries=5):
    url = trae_api_base + '?' + urlencode({'prompt': prompt, 'image_size': 'landscape_16_9'})
    for attempt in range(max_retries):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0 Chrome/120.0.0.0 Safari/537.36'})
            with urlopen(req, timeout=120) as resp:
                data = resp.read()
            if len(data) < 10000:
                text = data[:200].decode('utf-8', errors='replace')
                print(f"    Attempt {attempt+1}: response too small ({len(data)}b), waiting...", flush=True)
                time.sleep(5)
                continue
            img = Image.open(io.BytesIO(data))
            if img.mode in ('RGBA', 'P', 'LA'):
                img = img.convert('RGB')
            if img.size[0] < 1200 or img.size[1] < 600:
                print(f"    Attempt {attempt+1}: got {img.size}, too small, retrying...", flush=True)
                time.sleep(5)
                continue
            return img
        except Exception as e:
            print(f"    Attempt {attempt+1} error: {e}", flush=True)
            time.sleep(4)
    return None

def crop_resize(img, tw, th):
    sw, sh = img.size
    scale = max(tw / sw, th / sh)
    if abs(scale - 1.0) > 0.01:
        new_w, new_h = int(sw * scale + 0.5), int(sh * scale + 0.5)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        sw, sh = new_w, new_h
    left = (sw - tw) // 2
    top = (sh - th) // 2
    return img.crop((left, top, left + tw, top + th))

success = 0
failed = []

for i, fname in enumerate(targets, 1):
    fpath = os.path.join(img_dir, fname)
    prompt = extract_prompt(fname)
    if not prompt:
        print(f"[{i}/{len(targets)}] SKIP (no prompt): {fname}")
        continue
    is_banner = fname in hero_banner_images
    tw, th = (BANNER_W, BANNER_H) if is_banner else (CONTENT_W, CONTENT_H)
    cat = "BANNER" if is_banner else "content"
    
    print(f"[{i}/{len(targets)}] Generating {cat}: {fname[:55]}... (target {tw}x{th})", flush=True)
    
    if os.path.exists(fpath):
        os.remove(fpath)
    
    img = fetch_raw(prompt)
    if img is None:
        print(f"    FAILED after all retries", flush=True)
        failed.append(fname)
        continue
    
    out = crop_resize(img, tw, th)
    out.save(fpath, 'WEBP', quality=88, method=6)
    rw, rh = out.size
    sz = os.path.getsize(fpath) / 1024
    print(f"    OK: {rw}x{rh}, {sz:.0f}KB", flush=True)
    success += 1
    
    if i < len(targets):
        time.sleep(2)

print(f"\n{'='*60}", flush=True)
print(f"Done! Success: {success}, Failed: {len(failed)}", flush=True)
for f in failed:
    print(f"  FAILED: {f}", flush=True)
