import re
import os
import hashlib
from PIL import Image
from urllib.parse import urlencode

html_dir = '/workspace/html'
img_dir = os.path.join(html_dir, 'img')
trae_api_base = 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image'

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
        img_rel = m.group(1)
        img_fname = os.path.basename(img_rel)
        hero_banner_images.add(img_fname)
    
    for match in img_path_pattern.finditer(content):
        img_path = match.group(0)
        if not img_path.endswith(('.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp')):
            continue
        img_filename = os.path.basename(img_path)
        if img_filename not in all_images:
            all_images[img_filename] = {'path': img_path, 'pages': set(), 'size_type': None, 'prompt': None}
        all_images[img_filename]['pages'].add(filename)

size_types = ['landscape_16_9', 'landscape_4_3', 'portrait_16_9', 'portrait_4_3', 'square_hd', 'square']
square_types = {'square_hd', 'square'}

for img_filename in list(all_images.keys()):
    m = re.match(r'(.+)-([a-f0-9]{8})\.webp$', img_filename)
    if m:
        prompt_part = m.group(1)
        expected_hash = m.group(2)
        for size in size_types:
            test_url = trae_api_base + '?' + urlencode({'prompt': prompt_part, 'image_size': size})
            actual_hash = hashlib.md5(test_url.encode()).hexdigest()[:8]
            if actual_hash == expected_hash:
                all_images[img_filename]['size_type'] = size
                all_images[img_filename]['prompt'] = prompt_part
                break

banner_list = []
square_list = []
other_list = []
missing_list = []

for img_filename, info in sorted(all_images.items()):
    fpath = os.path.join(img_dir, img_filename)
    exists = os.path.exists(fpath) and os.path.getsize(fpath) > 500
    w, h = 0, 0
    if exists:
        try:
            with Image.open(fpath) as img:
                w, h = img.size
        except:
            exists = False
    
    is_banner = img_filename in hero_banner_images
    is_square = info['size_type'] in square_types
    
    rec = {
        'filename': img_filename,
        'exists': exists,
        'w': w, 'h': h,
        'is_banner': is_banner,
        'is_square': is_square,
        'size_type': info['size_type'],
        'prompt': info['prompt'],
        'pages': info['pages']
    }
    
    if is_banner:
        banner_list.append(rec)
    elif is_square:
        square_list.append(rec)
    else:
        other_list.append(rec)
    
    if not exists:
        missing_list.append(rec)

print("=" * 70)
print("📊 图片分类统计")
print("=" * 70)
print(f"  Hero Banner 图片 (目标尺寸 1368×600): {len(banner_list)} 张")
print(f"  正方形 1:1 图片 (目标尺寸 800×800): {len(square_list)} 张")
print(f"  其他内容图片 (保持原尺寸): {len(other_list)} 张")
print(f"  总计: {len(all_images)} 张")
print()
print(f"  ❌ 缺失文件: {len(missing_list)} 张")
print()

print("=" * 70)
print(f"📋 Hero Banner 图片详情 ({len(banner_list)} 张)")
print("=" * 70)
for r in banner_list:
    status = f"✅ {r['w']}x{r['h']}" if r['exists'] else "❌ 缺失"
    print(f"  {status} | {r['filename'][:70]}")

print()
print("=" * 70)
print(f"📋 正方形图片详情 ({len(square_list)} 张)")
print("=" * 70)
for r in square_list:
    status = f"✅ {r['w']}x{r['h']}" if r['exists'] else "❌ 缺失"
    print(f"  {status} | {r['filename'][:70]}")

if missing_list:
    print()
    print("=" * 70)
    print(f"❌ 缺失图片列表 ({len(missing_list)} 张)")
    print("=" * 70)
    for r in missing_list:
        cat = "Banner" if r['is_banner'] else ("Square" if r['is_square'] else "Other")
        print(f"  [{cat}] {r['filename']} | size={r['size_type']}")
