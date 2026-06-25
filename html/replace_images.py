import re
import os
import hashlib
from urllib.parse import urlparse, parse_qs

html_dir = '/workspace/html'

trae_pattern = re.compile(r"https://trae-api-cn\.mchost\.guru[^'\"\)]+")
yukings_pattern = re.compile(r"https://www\.yukings\.net/[^'\"\)\s]+")

all_urls = set()
url_occurrences = {}

for filename in os.listdir(html_dir):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(html_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for match in trae_pattern.findall(content):
        all_urls.add(match)
        if match not in url_occurrences:
            url_occurrences[match] = []
        url_occurrences[match].append(filename)
    
    for match in yukings_pattern.findall(content):
        if match.endswith(('.webp', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp')):
            all_urls.add(match)
            if match not in url_occurrences:
                url_occurrences[match] = []
            url_occurrences[match].append(filename)

def generate_filename(url, index):
    if 'trae-api-cn.mchost.guru' in url:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        prompt = params.get('prompt', [''])[0]
        image_size = params.get('image_size', ['landscape_16_9'])[0]
        
        clean_prompt = re.sub(r'[^a-z0-9]+', '-', prompt.lower()).strip('-')
        if len(clean_prompt) > 80:
            clean_prompt = clean_prompt[:80]
        
        short_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        return f"img/{clean_prompt}-{short_hash}.webp"
    elif 'yukings.net' in url:
        parsed = urlparse(url)
        path = parsed.path.lstrip('/')
        return path
    else:
        short_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        return f"img/external-{short_hash}.webp"

url_mapping = {}
for i, url in enumerate(sorted(all_urls)):
    url_mapping[url] = generate_filename(url, i)

total_replacements = 0
file_replacements = {}

for filename in os.listdir(html_dir):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(html_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = 0
    for url, local_path in url_mapping.items():
        if url in content:
            occurrences = content.count(url)
            content = content.replace(url, local_path)
            count += occurrences
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        file_replacements[filename] = count
        total_replacements += count

report_lines = []
report_lines.append("# 全站图片路径合规性报告")
report_lines.append("")
report_lines.append("## 概述")
report_lines.append("")
report_lines.append(f"- **扫描文件数**: {len([f for f in os.listdir(html_dir) if f.endswith('.html')])} 个 HTML 文件")
report_lines.append(f"- **发现唯一外部图片URL数**: {len(all_urls)} 个")
report_lines.append(f"- **总替换次数**: {total_replacements} 处")
report_lines.append(f"- **涉及文件数**: {len(file_replacements)} 个")
report_lines.append("")
report_lines.append("## 替换规则")
report_lines.append("")
report_lines.append("### Trae AI 生成图片")
report_lines.append("- 原URL: `https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=...`")
report_lines.append("- 替换为: `img/{prompt关键词}-{哈希}.webp`")
report_lines.append("")
report_lines.append("### Yukings 官方域名图片")
report_lines.append("- 原URL: `https://www.yukings.net/img/...`")
report_lines.append("- 替换为: 相对路径 `img/...`")
report_lines.append("")
report_lines.append("## 各文件替换详情")
report_lines.append("")
report_lines.append("| 文件名 | 替换数量 |")
report_lines.append("|--------|----------|")
for filename in sorted(file_replacements.keys()):
    report_lines.append(f"| {filename} | {file_replacements[filename]} |")
report_lines.append("")
report_lines.append("## URL映射表（前50条）")
report_lines.append("")
report_lines.append("| 原URL | 新路径 |")
report_lines.append("|-------|--------|")
for i, (url, local_path) in enumerate(sorted(url_mapping.items())):
    if i >= 50:
        break
    display_url = url if len(url) < 80 else url[:77] + "..."
    report_lines.append(f"| {display_url} | {local_path} |")

if len(url_mapping) > 50:
    report_lines.append("")
    report_lines.append(f"*... 还有 {len(url_mapping) - 50} 条映射，完整映射见脚本输出*")

report_lines.append("")
report_lines.append("## 图片文件清单")
report_lines.append("")
report_lines.append("以下图片需要放置在 `/workspace/html/img/` 目录下：")
report_lines.append("")
for url, local_path in sorted(url_mapping.items()):
    report_lines.append(f"- `{local_path}`")

report_content = "\n".join(report_lines)

report_path = os.path.join(html_dir, 'image-path-compliance-report.md')
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report_content)

print(f"替换完成！总替换 {total_replacements} 处，涉及 {len(file_replacements)} 个文件")
print(f"报告已生成: {report_path}")
print(f"\n唯一URL数: {len(all_urls)}")
