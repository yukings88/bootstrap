import re
import os
import hashlib
import time
import io
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from PIL import Image

html_dir = '/workspace/html'
img_dir = os.path.join(html_dir, 'img')
trae_api_base = 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image'

BANNER_W, BANNER_H = 1368, 600
CONTENT_W, CONTENT_H = 1368, 768

os.makedirs(img_dir, exist_ok=True)

print("🔍 扫描所有HTML文件...")
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
        img_fname = os.path.basename(m.group(1))
        hero_banner_images.add(img_fname)
    for match in img_path_pattern.finditer(content):
        img_path = match.group(0)
        if not img_path.endswith(('.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp')):
            continue
        img_filename = os.path.basename(img_path)
        if img_filename not in all_images:
            all_images[img_filename] = {'pages': set(), 'prompt': None}
        all_images[img_filename]['pages'].add(filename)

print(f"   共发现 {len(all_images)} 张图片引用")
print(f"   其中 Hero Banner: {len(hero_banner_images)} 张")

def extract_prompt(fname):
    m = re.match(r'(.+)-([a-f0-9]{8})\.webp$', fname)
    if m:
        return m.group(1)
    return None

def download_and_resize(prompt, target_w, target_h, output_path, max_retries=3):
    url = trae_api_base + '?' + urlencode({'prompt': prompt, 'image_size': 'landscape_16_9'})
    
    for attempt in range(max_retries):
        try:
            req = Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
            with urlopen(req, timeout=90) as response:
                img_data = response.read()
            if len(img_data) < 1000:
                time.sleep(2)
                continue
            
            img = Image.open(io.BytesIO(img_data))
            if img.mode in ('RGBA', 'P', 'LA'):
                img = img.convert('RGB')
            
            src_w, src_h = img.size
            
            if src_w < target_w:
                scale = target_w / src_w
                new_w, new_h = target_w, int(src_h * scale)
                img = img.resize((new_w, new_h), Image.LANCZOS)
                src_w, src_h = new_w, new_h
            
            if src_h < target_h:
                scale = target_h / src_h
                new_w, new_h = int(src_w * scale), target_h
                img = img.resize((new_w, new_h), Image.LANCZOS)
                src_w, src_h = new_w, new_h
            
            left = (src_w - target_w) // 2
            top = (src_h - target_h) // 2
            img = img.crop((left, top, left + target_w, top + target_h))
            
            img.save(output_path, 'WEBP', quality=88, method=6)
            return True
        except Exception as e:
            print(f"     ❌ 尝试 {attempt+1} 失败: {e}")
            if attempt < max_retries - 1:
                time.sleep(3)
    return False

def crop_existing(img, target_w, target_h, output_path):
    src_w, src_h = img.size
    if src_w < target_w or src_h < target_h:
        new_img = img.copy()
        if new_img.mode in ('RGBA', 'P', 'LA'):
            new_img = new_img.convert('RGB')
        scale = max(target_w / src_w, target_h / src_h)
        new_w, new_h = int(src_w * scale + 0.5), int(src_h * scale + 0.5)
        new_img = new_img.resize((new_w, new_h), Image.LANCZOS)
    else:
        new_img = img
    
    sw, sh = new_img.size
    left = (sw - target_w) // 2
    top = (sh - target_h) // 2
    new_img = new_img.crop((left, top, left + target_w, top + target_h))
    if new_img.mode in ('RGBA', 'P', 'LA'):
        new_img = new_img.convert('RGB')
    new_img.save(output_path, 'WEBP', quality=88, method=6)
    return True

to_regen = []
to_crop = []
ok_skip = []

for img_filename, info in sorted(all_images.items()):
    fpath = os.path.join(img_dir, img_filename)
    
    if img_filename in ('yukings-factory.webp', 'yukings-logo.svg', 'yukings-logo.jpg'):
        ok_skip.append((img_filename, '官方资源/Logo', 0, 0))
        continue
    
    is_banner = img_filename in hero_banner_images
    target_w, target_h = (BANNER_W, BANNER_H) if is_banner else (CONTENT_W, CONTENT_H)
    
    prompt = extract_prompt(img_filename)
    if not prompt:
        ok_skip.append((img_filename, '无法解析prompt', 0, 0))
        continue
    
    exists = os.path.exists(fpath) and os.path.getsize(fpath) > 500
    if exists:
        try:
            with Image.open(fpath) as img:
                w, h = img.size
            if w == target_w and h == target_h:
                ok_skip.append((img_filename, '尺寸正确', w, h))
                continue
            if w >= target_w and h >= target_h and abs(w / h - target_w / target_h) < 0.1:
                to_crop.append((img_filename, prompt, is_banner, target_w, target_h, w, h, '现有图片裁剪'))
                continue
            to_regen.append((img_filename, prompt, is_banner, target_w, target_h, f'尺寸不符({w}x{h})'))
        except:
            to_regen.append((img_filename, prompt, is_banner, target_w, target_h, '文件损坏'))
    else:
        to_regen.append((img_filename, prompt, is_banner, target_w, target_h, '文件缺失'))

print(f"\n📊 处理计划:")
print(f"   ✅ 已正确，无需处理: {len(ok_skip)} 张")
print(f"   ✂️  需要裁剪: {len(to_crop)} 张")
print(f"   🔄 需要重新生成: {len(to_regen)} 张")
print()

processed = 0
success = 0
failed_list = []

print(f"✂️  开始裁剪现有图片 ({len(to_crop)} 张)...")
for item in to_crop:
    fname, prompt, is_banner, tw, th, w, h, reason = item
    fpath = os.path.join(img_dir, fname)
    cat = "Banner" if is_banner else "Content"
    print(f"  [{processed+1}/{len(to_crop)+len(to_regen)}] 裁剪 {cat}: {fname[:55]}... ({w}x{h} → {tw}x{th})")
    try:
        with Image.open(fpath) as img:
            crop_existing(img, tw, th, fpath)
        success += 1
    except Exception as e:
        print(f"     ❌ 裁剪失败: {e}")
        to_regen.append((fname, prompt, is_banner, tw, th, f'裁剪失败: {e}'))
    processed += 1

print(f"\n🔄 开始重新生成图片 ({len(to_regen)} 张)...")
for i, item in enumerate(to_regen, 1):
    fname, prompt, is_banner, tw, th, reason = item
    fpath = os.path.join(img_dir, fname)
    cat = "Banner" if is_banner else "Content"
    print(f"  [{processed+i}/{len(to_crop)+len(to_regen)}] 生成 {cat}: {fname[:55]}...")
    print(f"     原因: {reason}, 目标: {tw}x{th}")
    
    if os.path.exists(fpath):
        os.remove(fpath)
    
    if download_and_resize(prompt, tw, th, fpath):
        with Image.open(fpath) as img:
            rw, rh = img.size
        size_kb = os.path.getsize(fpath) / 1024
        print(f"     ✅ 成功! {rw}x{rh}, {size_kb:.1f}KB")
        success += 1
    else:
        print(f"     ❌ 生成失败")
        failed_list.append(fname)
    
    if i < len(to_regen):
        time.sleep(1.5)

print()
print("=" * 60)
print(f"📋 处理完成!")
print(f"   成功处理: {success} 张")
print(f"   跳过(已正确): {len(ok_skip)} 张")
print(f"   失败: {len(failed_list)} 张")
if failed_list:
    for f in failed_list:
        print(f"     - {f}")
print("=" * 60)

print(f"\n📐 最终尺寸验证...")
banner_ok = 0
banner_bad = 0
content_ok = 0
content_bad = 0
for img_filename in all_images:
    fpath = os.path.join(img_dir, img_filename)
    if not os.path.exists(fpath):
        continue
    is_banner = img_filename in hero_banner_images
    try:
        with Image.open(fpath) as img:
            w, h = img.size
        if is_banner:
            if w == BANNER_W and h == BANNER_H:
                banner_ok += 1
            else:
                banner_bad += 1
                print(f"  ⚠️  Banner尺寸不符: {img_filename} ({w}x{h})")
        else:
            if w == CONTENT_W and h == CONTENT_H:
                content_ok += 1
            elif w >= 1000 and h >= 500:
                content_ok += 1
            else:
                content_bad += 1
    except:
        pass

print(f"  Banner ({BANNER_W}x{BANNER_H}): {banner_ok} 张正确, {banner_bad} 张异常")
print(f"  内容图: {content_ok} 张正常, {content_bad} 张异常")
