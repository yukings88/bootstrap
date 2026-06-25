import json
import os
from PIL import Image

img_dir = '/workspace/html/img'
target_size = (800, 800)

with open('/workspace/html/image_match_mapping.json', 'r', encoding='utf-8') as f:
    matches = json.load(f)

print(f"📋 需要替换的图片: {len(matches)} 张")
print(f"🎯 目标尺寸: {target_size[0]}x{target_size[1]}")
print()

successful = 0
failed = []

for i, match in enumerate(matches, 1):
    failed_file = match['failed_filename']
    matched_file = match['matched_filename']
    score = match['score']
    failed_prompt = match['failed_prompt']
    
    src_path = os.path.join(img_dir, matched_file)
    dst_path = os.path.join(img_dir, failed_file)
    
    if not os.path.exists(src_path):
        print(f"❌ [{i}/{len(matches)}] 源文件不存在: {matched_file}")
        failed.append(failed_file)
        continue
    
    try:
        img = Image.open(src_path)
        if img.mode in ('RGBA', 'P', 'LA'):
            img = img.convert('RGB')
        
        w, h = img.size
        
        # 中心裁剪成正方形
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 2
        img_square = img.crop((left, top, left + side, top + side))
        
        # 调整到目标尺寸
        img_final = img_square.resize(target_size, Image.LANCZOS)
        img_final.save(dst_path, 'WEBP', quality=85)
        
        new_size = os.path.getsize(dst_path) / 1024
        status = "✅" if score >= 0.6 else "⚠️ " if score >= 0.4 else "❓"
        print(f"{status} [{i}/{len(matches)}] {failed_prompt[:50]:50s} ({score:.2f}) → {target_size[0]}x{target_size[1]}, {new_size:.1f}KB")
        successful += 1
        
    except Exception as e:
        print(f"❌ [{i}/{len(matches)}] 失败: {failed_prompt[:50]} - {e}")
        failed.append(failed_file)

print()
print("=" * 60)
print(f"📊 替换完成!")
print(f"   成功: {successful}/{len(matches)} 张")
print(f"   失败: {len(failed)} 张")
if failed:
    print(f"   失败列表:")
    for f in failed[:5]:
        print(f"     - {f}")
print("=" * 60)
