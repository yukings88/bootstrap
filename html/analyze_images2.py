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
            all_images[img_filename] = {'path': img_path, 'pages': set(), 'size_type': None, 'prompt': None, 'w':0, 'h':0}
        all_images[img_filename]['pages'].add(filename)

size_types = ['landscape_16_9', 'landscape_4_3', 'portrait_16_9', 'portrait_4_3', 'square_hd', 'square']

square_1832_banners = []
for img_filename in sorted(all_images.keys()):
    fpath = os.path.join(img_dir, img_filename)
    exists = os.path.exists(fpath) and os.path.getsize(fpath) > 500
    if exists:
        try:
            with Image.open(fpath) as img:
                all_images[img_filename]['w'], all_images[img_filename]['h'] = img.size
        except:
            exists = False
    
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
    
    is_banner = img_filename in hero_banner_images
    if is_banner and exists and all_images[img_filename]['w'] == 1832 and all_images[img_filename]['h'] == 1832:
        square_1832_banners.append(img_filename)

print(f"发现 {len(square_1832_banners)} 张 Banner 图实际为 1832x1832 正方形 (错误参数生成):")
for f in square_1832_banners:
    info = all_images[f]
    print(f"  - {f}")
    print(f"    文件名hash匹配的size_type: {info['size_type']}")
    print(f"    prompt: {info['prompt']}")
    print()

print(f"\n其他1832x1832非Banner图:")
for img_filename, info in sorted(all_images.items()):
    is_banner = img_filename in hero_banner_images
    if not is_banner and info['w'] == 1832 and info['h'] == 1832:
        print(f"  - {img_filename} | size_type={info['size_type']}")

print(f"\n1368x768的图片: {sum(1 for i in all_images.values() if i['w']==1368 and i['h']==768)} 张")
print(f"1832x1832的图片: {sum(1 for i in all_images.values() if i['w']==1832 and i['h']==1832)} 张")
