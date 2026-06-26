import re, os, time, io, sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from PIL import Image
import hashlib

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

def is_valid_image(img, min_size_kb=40):
    w, h = img.size
    if w < 1300 or h < 600:
        return False, f"too small: {w}x{h}"
    pixels = img.convert('RGB')
    from collections import Counter
    colors = Counter()
    step = max(1, min(w, h) // 20)
    total = 0
    for x in range(0, w, step):
        for y in range(0, h, step):
            px = pixels.getpixel((x, y))
            colors[px] += 1
            total += 1
    if total == 0:
        return False, "no pixels sampled"
    most_common_pct = colors.most_common(1)[0][1] / total * 100
    if most_common_pct > 40:
        return False, f"too uniform: {most_common_pct:.0f}% same color"
    return True, f"OK ({w}x{h}, most common color {most_common_pct:.0f}%)"

def fetch_with_retry(prompt, max_retries=5):
    url = trae_api_base + '?' + urlencode({'prompt': prompt, 'image_size': 'landscape_16_9'})
    for attempt in range(max_retries):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0 Chrome/120.0.0.0 Safari/537.36', 'Accept': 'image/webp,image/*,*/*;q=0.8'})
            with urlopen(req, timeout=120) as resp:
                data = resp.read()
            if len(data) < 30000:
                print(f"    Attempt {attempt+1}: response only {len(data)}b, too small, waiting...", flush=True)
                time.sleep(8)
                continue
            img = Image.open(io.BytesIO(data))
            if img.mode in ('RGBA', 'P', 'LA'):
                img = img.convert('RGB')
            ok, msg = is_valid_image(img)
            if ok:
                return img
            print(f"    Attempt {attempt+1}: invalid image ({msg}), waiting...", flush=True)
            time.sleep(8)
        except Exception as e:
            print(f"    Attempt {attempt+1} error: {e}", flush=True)
            time.sleep(8)
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
    
    if os.path.exists(fpath):
        os.remove(fpath)
    
    print(f"[{i}/{len(targets)}] Generating {cat}: {fname[:50]}...", flush=True)
    
    img = fetch_with_retry(prompt)
    if img is None:
        print(f"    FAILED after all retries", flush=True)
        failed.append(fname)
        time.sleep(10)
        continue
    
    out = crop_resize(img, tw, th)
    if out.mode in ('RGBA', 'P', 'LA'):
        out = out.convert('RGB')
    out.save(fpath, 'WEBP', quality=88, method=6)
    rw, rh = out.size
    sz = os.path.getsize(fpath) / 1024
    print(f"    OK: {rw}x{rh}, {sz:.0f}KB", flush=True)
    success += 1
    time.sleep(4)

print(f"\n{'='*60}", flush=True)
print(f"Done! Success: {success}, Failed: {len(failed)}", flush=True)
for f in failed:
    print(f"  FAILED: {f}", flush=True)
