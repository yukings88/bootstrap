import re
import os
import hashlib
import time
import io
import sys
from urllib.parse import urlparse, parse_qs, urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from PIL import Image

html_dir = '/workspace/html'
img_dir = os.path.join(html_dir, 'img')

os.makedirs(img_dir, exist_ok=True)

trae_api_base = 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image'

def generate_filename(prompt, size_param):
    clean_prompt = re.sub(r'[^a-z0-9]+', '-', prompt.lower()).strip('-')
    if len(clean_prompt) > 80:
        clean_prompt = clean_prompt[:80]
    
    url = trae_api_base + '?' + urlencode({'prompt': prompt, 'image_size': size_param})
    short_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    return f"{clean_prompt}-{short_hash}.webp"

def download_image(prompt, size_param, output_path, max_retries=3):
    url = trae_api_base + '?' + urlencode({'prompt': prompt, 'image_size': size_param})
    
    for attempt in range(max_retries):
        try:
            req = Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
            
            with urlopen(req, timeout=60) as response:
                img_data = response.read()
            
            if len(img_data) < 1000:
                print(f"  ⚠️  Response too small ({len(img_data)} bytes), retrying...")
                time.sleep(2)
                continue
            
            img = Image.open(io.BytesIO(img_data))
            
            if img.mode in ('RGBA', 'P', 'LA'):
                img = img.convert('RGB')
            
            img.save(output_path, 'WEBP', quality=85)
            return True
            
        except Exception as e:
            print(f"  ❌ Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(3)
    
    return False

all_images = {}
img_path_pattern = re.compile(r'img/[^"\'\s)]+')

for filename in sorted(os.listdir(html_dir)):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(html_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for match in img_path_pattern.finditer(content):
        img_path = match.group(0)
        if not img_path.endswith(('.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp')):
            continue
        
        img_filename = os.path.basename(img_path)
        if img_filename not in all_images:
            all_images[img_filename] = {
                'path': img_path,
                'pages': set()
            }
        all_images[img_filename]['pages'].add(filename)

yukings_known = {
    'yukings-logo.svg': 'https://www.yukings.net/img/yukings-logo.svg',
    'yukings-factory.webp': 'https://www.yukings.net/img/yukings-factory.webp',
}

trae_images = []
external_images = []

for img_filename, info in sorted(all_images.items()):
    if img_filename in yukings_known:
        external_images.append({
            'filename': img_filename,
            'url': yukings_known[img_filename],
            'pages': info['pages'],
            'type': 'yukings'
        })
        continue
    
    m = re.match(r'(.+)-([a-f0-9]{8})\.webp$', img_filename)
    if m:
        prompt_part = m.group(1)
        expected_hash = m.group(2)
        
        found = False
        for size in ['landscape_16_9', 'landscape_4_3', 'portrait_16_9', 'portrait_4_3', 'square_hd', 'square']:
            test_url = trae_api_base + '?' + urlencode({'prompt': prompt_part, 'image_size': size})
            actual_hash = hashlib.md5(test_url.encode()).hexdigest()[:8]
            if actual_hash == expected_hash:
                trae_images.append({
                    'filename': img_filename,
                    'prompt': prompt_part,
                    'size': size,
                    'pages': info['pages'],
                    'type': 'trae'
                })
                found = True
                break
        
        if not found:
            external_images.append({
                'filename': img_filename,
                'url': None,
                'pages': info['pages'],
                'type': 'unknown'
            })
    else:
        external_images.append({
            'filename': img_filename,
            'url': None,
            'pages': info['pages'],
            'type': 'unknown'
        })

print(f"📊 图片统计:")
print(f"   Trae AI生成图片: {len(trae_images)} 张")
print(f"   Yukings官方图片: {len([i for i in external_images if i['type'] == 'yukings'])} 张")
print(f"   未知来源图片: {len([i for i in external_images if i['type'] == 'unknown'])} 张")
print(f"   总计: {len(all_images)} 张")
print()

successful = 0
failed = []

print(f"🚀 开始批量生成 Trae AI 图片 ({len(trae_images)} 张)...")
print()

for i, img_info in enumerate(trae_images, 1):
    output_path = os.path.join(img_dir, img_info['filename'])
    
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        print(f"✅ [{i}/{len(trae_images)}] 已存在: {img_info['filename']}")
        successful += 1
        continue
    
    print(f"🎨 [{i}/{len(trae_images)}] 生成中: {img_info['filename'][:60]}...")
    print(f"     Size: {img_info['size']}, 引用页面: {len(img_info['pages'])} 个")
    
    if download_image(img_info['prompt'], img_info['size'], output_path):
        size_kb = os.path.getsize(output_path) / 1024
        with Image.open(output_path) as img:
            w, h = img.size
        print(f"     ✅ 成功! {w}x{h}, {size_kb:.1f}KB")
        successful += 1
    else:
        print(f"     ❌ 失败")
        failed.append(img_info['filename'])
    
    if i < len(trae_images):
        time.sleep(1.5)

print()
print(f"📥 下载 Yukings 官方图片...")
for img_info in external_images:
    if img_info['type'] != 'yukings':
        continue
    
    output_path = os.path.join(img_dir, img_info['filename'])
    
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        print(f"✅ 已存在: {img_info['filename']}")
        successful += 1
        continue
    
    print(f"⬇️  下载: {img_info['filename']}")
    try:
        req = Request(img_info['url'], headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urlopen(req, timeout=30) as response:
            data = response.read()
        
        with open(output_path, 'wb') as f:
            f.write(data)
        print(f"   ✅ 成功! {len(data)/1024:.1f}KB")
        successful += 1
    except Exception as e:
        print(f"   ❌ 失败: {e}")
        failed.append(img_info['filename'])

print()
print("=" * 60)
print(f"📋 生成完成!")
print(f"   成功: {successful} 张")
print(f"   失败: {len(failed)} 张")
if failed:
    print(f"   失败列表: {failed[:5]}")
    if len(failed) > 5:
        print(f"            ... 还有 {len(failed)-5} 张")
print("=" * 60)
