import re, os, hashlib, time, io, sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, line_buffering=True)

html_dir = '/workspace/html'
img_dir = os.path.join(html_dir, 'img')
trae_api_base = 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image'

BANNER_W, BANNER_H = 1368, 600
CONTENT_W, CONTENT_H = 1368, 768

os.makedirs(img_dir, exist_ok=True)

print("Scanning HTML files...", flush=True)
all_images = {}
img_path_pattern = re.compile(r'img/[^"\'\s)]+')
hero_banner_images = set()
hero_pattern = re.compile(r'rsb-hero[^}]*?background-image\s*:\s*url\([\'"]?(img/[^\'")]+)[\'"]?\)', re.DOTALL)

for filename in sorted(os.listdir(html_dir)):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(html_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for m in hero_pattern.finditer(content):
        hero_banner_images.add(os.path.basename(m.group(1)))
    for match in img_path_pattern.finditer(content):
        img_path = match.group(0)
        if not img_path.endswith(('.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp')):
            continue
        img_filename = os.path.basename(img_path)
        if img_filename not in all_images:
            all_images[img_filename] = {'pages': set(), 'prompt': None}
        all_images[img_filename]['pages'].add(filename)

print(f"Found {len(all_images)} image references, {len(hero_banner_images)} banners", flush=True)

def extract_prompt(fname):
    m = re.match(r'(.+)-([a-f0-9]{8})\.webp$', fname)
    return m.group(1) if m else None

def fetch_raw_image(prompt, max_retries=3):
    url = trae_api_base + '?' + urlencode({'prompt': prompt, 'image_size': 'landscape_16_9'})
    for attempt in range(max_retries):
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'})
            with urlopen(req, timeout=90) as response:
                data = response.read()
            if len(data) < 5000:
                print(f"    Response too small ({len(data)} bytes), retrying...", flush=True)
                time.sleep(3)
                continue
            img = Image.open(io.BytesIO(data))
            if img.mode in ('RGBA', 'P', 'LA'):
                img = img.convert('RGB')
            return img
        except Exception as e:
            print(f"    Fetch attempt {attempt+1} error: {e}", flush=True)
            if attempt < max_retries - 1:
                time.sleep(3)
    return None

def crop_to_size(img, target_w, target_h):
    sw, sh = img.size
    scale = max(target_w / sw, target_h / sh)
    if scale > 1.01 or scale < 0.99:
        new_w, new_h = int(sw * scale + 0.5), int(sh * scale + 0.5)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        sw, sh = new_w, new_h
    left = (sw - target_w) // 2
    top = (sh - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))

def save_webp(img, path):
    if img.mode in ('RGBA', 'P', 'LA'):
        img = img.convert('RGB')
    img.save(path, 'WEBP', quality=88, method=6)

skip_list = []
crop_list = []
regen_list = []

for fname, info in sorted(all_images.items()):
    fpath = os.path.join(img_dir, fname)
    if fname in ('yukings-factory.webp', 'yukings-logo.svg', 'yukings-logo.jpg'):
        skip_list.append((fname, 'official'))
        continue
    prompt = extract_prompt(fname)
    if not prompt:
        skip_list.append((fname, 'no_prompt'))
        continue
    is_banner = fname in hero_banner_images
    tw, th = (BANNER_W, BANNER_H) if is_banner else (CONTENT_W, CONTENT_H)
    exists = os.path.exists(fpath) and os.path.getsize(fpath) > 500
    if exists:
        try:
            with Image.open(fpath) as img:
                w, h = img.size
            if w == tw and h == th:
                skip_list.append((fname, 'correct'))
                continue
            if w >= tw - 2 and h >= th - 2:
                crop_list.append((fname, prompt, is_banner, tw, th, w, h))
                continue
            regen_list.append((fname, prompt, is_banner, tw, th, f'wrong_size_{w}x{h}'))
        except Exception as e:
            regen_list.append((fname, prompt, is_banner, tw, th, f'corrupt:{e}'))
    else:
        regen_list.append((fname, prompt, is_banner, tw, th, 'missing'))

print(f"Skip: {len(skip_list)}, Crop: {len(crop_list)}, Regenerate: {len(regen_list)}", flush=True)

success = 0
failed = []

print(f"\nCropping {len(crop_list)} existing images...", flush=True)
for i, (fname, prompt, is_banner, tw, th, w, h) in enumerate(crop_list, 1):
    fpath = os.path.join(img_dir, fname)
    cat = "BANNER" if is_banner else "content"
    try:
        with Image.open(fpath) as img:
            out = crop_to_size(img, tw, th)
            save_webp(out, fpath)
        sz = os.path.getsize(fpath) / 1024
        print(f"  [{i}/{len(crop_list)}] CROP {cat}: {fname[:50]} ({w}x{h}->{tw}x{th}, {sz:.0f}KB)", flush=True)
        success += 1
    except Exception as e:
        print(f"  [{i}/{len(crop_list)}] CROP FAIL: {fname[:50]} -> {e}", flush=True)
        regen_list.append((fname, prompt, is_banner, tw, th, f'crop_fail:{e}'))

print(f"\nRegenerating {len(regen_list)} images...", flush=True)
for i, (fname, prompt, is_banner, tw, th, reason) in enumerate(regen_list, 1):
    fpath = os.path.join(img_dir, fname)
    cat = "BANNER" if is_banner else "content"
    print(f"  [{i}/{len(regen_list)}] REGEN {cat}: {fname[:50]} ({reason})", flush=True)
    if os.path.exists(fpath):
        os.remove(fpath)
    img = fetch_raw_image(prompt)
    if img is None:
        print(f"    FAILED to fetch", flush=True)
        failed.append(fname)
        continue
    try:
        out = crop_to_size(img, tw, th)
        save_webp(out, fpath)
        rw, rh = out.size
        sz = os.path.getsize(fpath) / 1024
        print(f"    OK: {rw}x{rh}, {sz:.0f}KB", flush=True)
        success += 1
    except Exception as e:
        print(f"    SAVE FAIL: {e}", flush=True)
        failed.append(fname)
    if i < len(regen_list):
        time.sleep(1.5)

print(f"\n{'='*60}", flush=True)
print(f"DONE! Success: {success}, Failed: {len(failed)}, Skipped: {len(skip_list)}", flush=True)
if failed:
    for f in failed:
        print(f"  FAIL: {f}", flush=True)

print(f"\nVerifying final sizes...", flush=True)
banner_ok = banner_bad = content_ok = content_bad = 0
for fname in all_images:
    fpath = os.path.join(img_dir, fname)
    if not os.path.exists(fpath):
        continue
    is_banner = fname in hero_banner_images
    try:
        with Image.open(fpath) as img:
            w, h = img.size
        if is_banner:
            if w == BANNER_W and h == BANNER_H:
                banner_ok += 1
            else:
                banner_bad += 1
                print(f"  BAD BANNER: {fname} ({w}x{h})", flush=True)
        else:
            if w >= 1000 and h >= 500:
                content_ok += 1
            else:
                content_bad += 1
                print(f"  BAD CONTENT: {fname} ({w}x{h})", flush=True)
    except:
        pass
print(f"Banner {BANNER_W}x{BANNER_H}: {banner_ok} OK, {banner_bad} bad", flush=True)
print(f"Content: {content_ok} OK, {content_bad} bad", flush=True)
