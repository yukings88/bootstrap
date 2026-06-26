import re, os, time, io, sys
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen
from PIL import Image
from collections import Counter

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

def is_valid_image(img):
    w, h = img.size
    if w < 1300 or h < 600:
        return False
    if w == 1832 and h == 1832:
        return False
    rgb = img.convert('RGB')
    c = Counter()
    step = max(1, min(w, h) // 25)
    total = 0
    for x in range(0, w, step):
        for y in range(0, h, step):
            c[rgb.getpixel((x, y))] += 1
            total += 1
    top_pct = c.most_common(1)[0][1] / total * 100
    if top_pct > 25:
        return False
    return True

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

def fetch_one(prompt, max_attempts=20):
    url = trae_api_base + '?' + urlencode({'prompt': prompt, 'image_size': 'landscape_16_9'})
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
    }
    for attempt in range(1, max_attempts + 1):
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=120) as resp:
                data = resp.read()
            if len(data) < 30000:
                print(f"    Attempt {attempt}: only {len(data)}b, waiting 10s...", flush=True)
                time.sleep(10)
                continue
            img = Image.open(io.BytesIO(data))
            if img.mode in ('RGBA', 'P', 'LA'):
                img = img.convert('RGB')
            w, h = img.size
            if is_valid_image(img):
                print(f"    Attempt {attempt}: got valid image {w}x{h}, {len(data)/1024:.0f}KB", flush=True)
                return img
            else:
                print(f"    Attempt {attempt}: {w}x{h} invalid (placeholder?), waiting 12s...", flush=True)
                time.sleep(12)
        except Exception as e:
            print(f"    Attempt {attempt}: error {e}, waiting 10s...", flush=True)
            time.sleep(10)
    return None

success = 0
failed = []

for i, fname in enumerate(targets, 1):
    fpath = os.path.join(img_dir, fname)
    prompt = extract_prompt(fname)
    if not prompt:
        print(f"[{i}/{len(targets)}] SKIP: {fname}", flush=True)
        continue
    is_banner = fname in hero_banner_images
    tw, th = (BANNER_W, BANNER_H) if is_banner else (CONTENT_W, CONTENT_H)
    cat = "BANNER" if is_banner else "content"
    
    if os.path.exists(fpath):
        try:
            with Image.open(fpath) as test_img:
                if is_valid_image(test_img) and test_img.size == (tw, th):
                    print(f"[{i}/{len(targets)}] SKIP (already valid): {fname[:50]}", flush=True)
                    success += 1
                    continue
        except:
            pass
        os.remove(fpath)
    
    print(f"[{i}/{len(targets)}] Generating {cat}: {fname[:50]}...", flush=True)
    
    img = fetch_one(prompt)
    if img is None:
        print(f"    FAILED after all attempts", flush=True)
        failed.append(fname)
        time.sleep(15)
        continue
    
    out = crop_resize(img, tw, th)
    if out.mode in ('RGBA', 'P', 'LA'):
        out = out.convert('RGB')
    out.save(fpath, 'WEBP', quality=88, method=6)
    rw, rh = out.size
    sz = os.path.getsize(fpath) / 1024
    print(f"    SAVED: {rw}x{rh}, {sz:.0f}KB", flush=True)
    success += 1
    time.sleep(5)

print(f"\n{'='*60}", flush=True)
print(f"Done! Success: {success}/{len(targets)}, Failed: {len(failed)}", flush=True)
for f in failed:
    print(f"  FAILED: {f}", flush=True)
