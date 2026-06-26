import re, os, time, io, sys
from urllib.parse import urlencode
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

all_refs = {}
img_pat = re.compile(r'img/[^"\'\s)]+')
for fn in sorted(os.listdir(html_dir)):
    if not fn.endswith('.html'): continue
    with open(os.path.join(html_dir, fn), encoding='utf-8') as f:
        c = f.read()
    for m in img_pat.finditer(c):
        p = m.group(0)
        if not p.endswith(('.webp','.jpg','.jpeg','.png','.svg','.bmp','.gif')): continue
        fn_base = os.path.basename(p)
        if fn_base in ('yukings-factory.webp','yukings-logo.svg','yukings-logo.jpg'): continue
        if fn_base not in all_refs:
            mm = re.match(r'(.+)-([a-f0-9]{8})\.webp$', fn_base)
            all_refs[fn_base] = {'prompt': mm.group(1) if mm else None, 'is_banner': fn_base in hero_banner_images}

def is_valid(img):
    w, h = img.size
    if w < 1300 or h < 590: return False
    if w == 1832 and h == 1832: return False
    rgb = img.convert('RGB')
    c = Counter()
    step = max(1, min(w,h)//25)
    total = 0
    for x in range(0, w, step):
        for y in range(0, h, step):
            c[rgb.getpixel((x,y))] += 1
            total += 1
    top_pct = c.most_common(1)[0][1]/total*100
    return top_pct < 30

def crop_resize(img, tw, th):
    sw, sh = img.size
    scale = max(tw/sw, th/sh)
    if abs(scale-1.0) > 0.01:
        img = img.resize((int(sw*scale+0.5), int(sh*scale+0.5)), Image.LANCZOS)
        sw, sh = img.size
    l = (sw-tw)//2
    t = (sh-th)//2
    out = img.crop((l, t, l+tw, t+th))
    if out.mode in ('RGBA','P','LA'):
        out = out.convert('RGB')
    return out

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

def fetch_poll(prompt, poll_interval=15, max_polls=20):
    url = trae_api_base + '?' + urlencode({'prompt': prompt, 'image_size': 'landscape_16_9'})
    for poll in range(1, max_polls+1):
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=120) as resp:
                data = resp.read()
            if len(data) < 30000:
                print(f"    poll{poll}: {len(data)}b too small, waiting {poll_interval}s...", flush=True)
                time.sleep(poll_interval)
                continue
            img = Image.open(io.BytesIO(data))
            if img.mode in ('RGBA','P','LA'):
                img = img.convert('RGB')
            w, h = img.size
            if is_valid(img):
                print(f"    poll{poll}: GOT VALID {w}x{h} ({len(data)/1024:.0f}KB)", flush=True)
                return img
            print(f"    poll{poll}: {w}x{h} placeholder, waiting {poll_interval}s...", flush=True)
        except Exception as e:
            print(f"    poll{poll}: error {e}, waiting...", flush=True)
        time.sleep(poll_interval)
    return None

to_gen = []
for fname, info in sorted(all_refs.items()):
    fp = os.path.join(img_dir, fname)
    if not info['prompt']: continue
    if os.path.exists(fp) and os.path.getsize(fp) > 25000:
        try:
            with Image.open(fp) as img:
                w, h = img.size
                tw, th = (BANNER_W,BANNER_H) if info['is_banner'] else (CONTENT_W,CONTENT_H)
                if w == tw and h == th and is_valid(img):
                    continue
        except:
            pass
    to_gen.append((fname, info['prompt'], info['is_banner']))

print(f"Need to generate: {len(to_gen)} images", flush=True)
print(f"Waiting 30s for rate limit cooldown...", flush=True)
time.sleep(30)

success = 0
failed = []

for i, (fname, prompt, is_banner) in enumerate(to_gen, 1):
    fp = os.path.join(img_dir, fname)
    tw, th = (BANNER_W,BANNER_H) if is_banner else (CONTENT_W,CONTENT_H)
    cat = "BANNER" if is_banner else "content"
    
    if os.path.exists(fp):
        os.remove(fp)
    
    print(f"[{i}/{len(to_gen)}] {cat}: {fname[:55]}", flush=True)
    
    img = fetch_poll(prompt)
    if img is None:
        print(f"    FAILED", flush=True)
        failed.append(fname)
        time.sleep(20)
        continue
    
    out = crop_resize(img, tw, th)
    out.save(fp, 'WEBP', quality=88, method=6)
    sz = os.path.getsize(fp)/1024
    print(f"    SAVED: {out.size[0]}x{out.size[1]}, {sz:.0f}KB", flush=True)
    success += 1
    time.sleep(8)

print(f"\n{'='*60}", flush=True)
print(f"Done! Success: {success}/{len(to_gen)}, Failed: {len(failed)}", flush=True)
for f in failed:
    print(f"  FAIL: {f}", flush=True)
