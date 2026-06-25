import re
import os
import glob
import difflib

img_dir = '/workspace/html/img'

success_prompts = {}
failed_prompts = {}

for f in sorted(glob.glob(os.path.join(img_dir, '*.webp'))):
    size_kb = os.path.getsize(f) / 1024
    m = re.match(r'(.+)-([a-f0-9]{8})\.webp$', os.path.basename(f))
    if not m:
        continue
    prompt = m.group(1)
    if size_kb >= 30:
        success_prompts[prompt] = os.path.basename(f)
    else:
        failed_prompts[prompt] = os.path.basename(f)

def similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

def smart_match(failed_prompt, success_list):
    best_score = 0
    best_prompt = None
    
    failed_words = set(failed_prompt.split('-'))
    
    for s_prompt in success_list:
        score = similarity(failed_prompt, s_prompt)
        
        s_words = set(s_prompt.split('-'))
        common_words = failed_words & s_words
        word_score = len(common_words) / max(len(failed_words), 1)
        
        combined = score * 0.6 + word_score * 0.4
        
        if combined > best_score:
            best_score = combined
            best_prompt = s_prompt
    
    return best_prompt, best_score

print(f"成功图片: {len(success_prompts)} 张")
print(f"失败图片: {len(failed_prompts)} 张")
print()
print("=== 匹配结果 ===")

matches = []
for failed_prompt, failed_filename in sorted(failed_prompts.items()):
    best_prompt, score = smart_match(failed_prompt, list(success_prompts.keys()))
    matches.append({
        'failed_prompt': failed_prompt,
        'failed_filename': failed_filename,
        'matched_prompt': best_prompt,
        'matched_filename': success_prompts[best_prompt],
        'score': score
    })

matches.sort(key=lambda x: x['score'], reverse=True)

high_score = [m for m in matches if m['score'] >= 0.6]
mid_score = [m for m in matches if 0.4 <= m['score'] < 0.6]
low_score = [m for m in matches if m['score'] < 0.4]

print(f"\n高匹配 (>=0.6): {len(high_score)} 张")
for m in high_score[:10]:
    print(f"  ✅ {m['failed_prompt'][:50]:50s} ← {m['matched_prompt'][:50]} ({m['score']:.2f})")

print(f"\n中等匹配 (0.4-0.6): {len(mid_score)} 张")
for m in mid_score[:10]:
    print(f"  ⚠️  {m['failed_prompt'][:50]:50s} ← {m['matched_prompt'][:50]} ({m['score']:.2f})")

print(f"\n低匹配 (<0.4): {len(low_score)} 张")
for m in low_score[:10]:
    print(f"  ❌ {m['failed_prompt'][:50]:50s} ← {m['matched_prompt'][:50]} ({m['score']:.2f})")

import json
with open('/workspace/html/image_match_mapping.json', 'w', encoding='utf-8') as f:
    json.dump([{
        'failed_filename': m['failed_filename'],
        'matched_filename': m['matched_filename'],
        'failed_prompt': m['failed_prompt'],
        'matched_prompt': m['matched_prompt'],
        'score': round(m['score'], 3)
    } for m in matches], f, indent=2, ensure_ascii=False)

print(f"\n📄 匹配映射已保存到: image_match_mapping.json")
