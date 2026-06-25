import re
import os
import io
import time
import glob
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from PIL import Image

img_dir = '/workspace/html/img'
api_base = 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image'
target_size = (800, 800)

failed_images = []
for f in sorted(glob.glob(os.path.join(img_dir, '*.webp'))):
    try:
        img = Image.open(f)
        w, h = img.size
        size_kb = os.path.getsize(f) / 1024
        if w == h and size_kb < 30:
            filename = os.path.basename(f)
            failed_images.append(filename)
    except:
        pass

print(f"📋 需要重新生成的正方形图片: {len(failed_images)} 张")
print()

successful = 0
failed = []

for i, filename in enumerate(failed_images, 1):
    m = re.match(r'(.+)-([a-f0-9]{8})\.webp$', filename)
    if not m:
        print(f"⚠️  [{i}/{len(failed_images)}] 跳过: {filename}")
        continue
    
    prompt = m.group(1)
    output_path = os.path.join(img_dir, filename)
    
    print(f"🎨 [{i}/{len(failed_images)}] {prompt[:60]}...")
    
    success = False
    for attempt in range(3):
        try:
            url = api_base + '?' + urlencode({'prompt': prompt, 'image_size': 'square_hd'})
            req = Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            with urlopen(req, timeout=90) as response:
                data = response.read()
            
            if len(data) < 30000:
                print(f"     ⚠️  Attempt {attempt+1}: 图片过小 ({len(data)} bytes)")
                time.sleep(3)
                continue
            
            img = Image.open(io.BytesIO(data))
            if img.mode in ('RGBA', 'P', 'LA'):
                img = img.convert('RGB')
            
            img_resized = img.resize(target_size, Image.LANCZOS)
            img_resized.save(output_path, 'WEBP', quality=85)
            
            new_size = os.path.getsize(output_path) / 1024
            print(f"     ✅ 成功! 800x800, {new_size:.1f}KB")
            successful += 1
            success = True
            break
            
        except Exception as e:
            print(f"     ❌ Attempt {attempt+1} failed: {e}")
            if attempt < 2:
                time.sleep(3)
    
    if not success:
        failed.append(filename)
    
    if i < len(failed_images):
        time.sleep(1)

print()
print("=" * 60)
print(f"📊 重生成完成!")
print(f"   成功: {successful}/{len(failed_images)} 张")
print(f"   失败: {len(failed)} 张")
if failed:
    print(f"   失败列表:")
    for f in failed[:10]:
        print(f"     - {f}")
    if len(failed) > 10:
        print(f"     ... 还有 {len(failed)-10} 张")
print("=" * 60)
