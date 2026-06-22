#!/usr/bin/env python3
"""
批量下载 trae-api text_to_image 图片并替换 HTML 文件中的 URL

使用方法：
  python3 batch_download_replace_images.py

流程：
  1. 扫描 /workspace/html/ 下所有 .html 文件
  2. 提取所有 https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=... 格式的 URL
  3. 去重，生成短文件名（取 prompt 中前 40 字符 + 短哈希）
  4. 下载到 /workspace/html/img/ 目录（格式：WebP）
  5. 批量替换所有 HTML 文件中的 URL 为相对路径 img/xxx.webp

结果报告：
  - 下载完成后，会在 /workspace/html/img/_download_report.txt 生成报告
  - 每个图片保存同时会保存同名 .headers.txt 记录响应头
"""
import os
import re
import sys
import time
import hashlib
import urllib.parse
import urllib.request
from collections import OrderedDict

TRAE_API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt="
HTML_DIR = "/workspace/html"
IMG_DIR = os.path.join(HTML_DIR, "img")

# 从 URL 中提取 prompt
def extract_prompt_from_url(url):
    m = re.search(r"\?prompt=([^&]+)\&image_size=", url)
    if m:
        return urllib.parse.unquote(m.group(1))
    return None

# 生成安全的文件名（短文件名）
def generate_filename(prompt, url):
    # 用 prompt 提取核心词（取前 60 字符），再加上 5 位哈希避免冲突
    short = prompt[:60].rstrip("-")
    # 清理非法字符
    safe = re.sub(r'[^a-z0-9-]+', '-', short.lower()).strip('-').strip('_')
    # 加上 5 位短哈希
    hash_suffix = hashlib.md5(url.encode()).hexdigest()[:5]
    return f"nb-{safe}-{hash_suffix}.webp"

# 扫描所有 HTML 文件
print("=== 第一步：扫描所有 HTML 文件并提取 URL ===")
url_map = OrderedDict()  # url -> (prompt, files_list)

for fn in sorted(os.listdir(HTML_DIR)):
    if not fn.endswith('.html'):
        continue
    fpath = os.path.join(HTML_DIR, fn)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  [跳过] {fn}: 读取失败: {e}")
        continue

    # 找到所有完整 URL
    for m in re.finditer(
        r'https://trae-api-cn\.mchost\.guru/api/ide/v1/text_to_image\?prompt=([^\&\"\']+)\&image_size=([a-z0-9_]+)',
        content
    ):
        full_url = m.group(0)
        prompt = urllib.parse.unquote(m.group(1))
        if full_url not in url_map:
            url_map[full_url] = (prompt, [])
        if fn not in url_map[full_url][1]:
            url_map[full_url][1].append(fn)

total_urls = len(url_map)
files_touched = set()
for url, (_, files) in url_map.items():
    files_touched.update(files)

print(f"  发现唯一 URL: {total_urls}")
print(f"  受影响 HTML 文件: {len(files_touched)}")

# 创建映射
print("\n=== 第二步：生成文件映射 ===")
url_to_filename = {}
used_filenames = set()
for url, (prompt, files) in url_map.items():
    fname = generate_filename(prompt, url)
    # 确保没有重名
    if fname in used_filenames:
        # 用更长的 hash 前缀
        hash_suffix = hashlib.md5(url.encode()).hexdigest()[:8]
        short = prompt[:50].rstrip("-")
        safe = re.sub(r'[^a-z0-9-]+', '-', short.lower()).strip('-').strip('_')
        fname = f"nb-{safe}-{hash_suffix}.webp"
    used_filenames.add(fname)
    url_to_filename[url] = fname
    print(f"  {prompt[:50]} -> {fname}")

# 确保图片目录存在
os.makedirs(IMG_DIR, exist_ok=True)

# 下载图片
print(f"\n=== 第三步：下载 {len(url_to_filename)} 张图片到 {IMG_DIR}/ ===")
success_count = 0
fail_count = 0
placeholder_count = 0
report_lines = []
report_lines.append("Trae-API 图片批量下载报告")
report_lines.append("=" * 60)
report_lines.append(f"下载时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
report_lines.append(f"唯一 URL 数: {total_urls}")
report_lines.append(f"受影响 HTML 文件: {len(files_touched)}")
report_lines.append("")

for idx, (url, fname) in enumerate(url_to_filename.items(), 1):
    fpath = os.path.join(IMG_DIR, fname)
    header_path = fpath + ".headers.txt"

    # 如果已存在，跳过下载
    if os.path.exists(fpath):
        file_size = os.path.getsize(fpath)
        print(f"  [{idx:3d}/{total_urls:3d}] ✓ 已存在: {fname} ({file_size} bytes)")
        success_count += 1
        report_lines.append(f"[EXIST] {fname} ({file_size} bytes)")
        continue

    try:
        print(f"  [{idx:3d}/{total_urls:3d}] 下载: {fname} -> ", end="", flush=True)
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) Yukings-Image-Bot/1.0'
            }
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            content_type = resp.headers.get('Content-Type', '')
            content_length = resp.headers.get('Content-Length', '')

            # 保存图片
            with open(fpath, 'wb') as f_out:
                f_out.write(data)

            # 保存 headers 信息
            with open(header_path, 'w', encoding='utf-8') as f_h:
                f_h.write(f"URL: {url}\n")
                f_h.write(f"Status: {resp.status}\n")
                f_h.write(f"Content-Type: {content_type}\n")
                f_h.write(f"Content-Length: {content_length}\n")
                f_h.write(f"Downloaded: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f_h.write(f"File Size: {len(data)} bytes\n")
                f_h.write("\n")
                for h_key, h_val in resp.headers.items():
                    f_h.write(f"{h_key}: {h_val}\n")

            file_size = len(data)
            print(f"✓ {file_size} bytes, Content-Type: {content_type}")
            success_count += 1

            # 检查是否为占位图（太小或非图片）
            is_placeholder = False
            if file_size < 1000 or 'image' not in content_type.lower():
                is_placeholder = True
                placeholder_count += 1
                print(f"    ⚠️  警告: 可能为占位图或错误响应 ({content_type}, {file_size} bytes)")

            report_lines.append(
                f"[{'PLACEHOLDER' if is_placeholder else 'OK'}] {fname} ({file_size} bytes, {content_type})"
            )

    except Exception as e:
        fail_count += 1
        print(f"✗ 失败: {e}")
        report_lines.append(f"[FAIL] {fname}: {e}")

    # 稍微限速
    if idx % 10 == 0:
        time.sleep(0.5)

print(f"\n=== 下载完成: {success_count} 成功, {fail_count} 失败, {placeholder_count} 疑似占位图 ===")
report_lines.append("\n")
report_lines.append(f"总计: {success_count} 成功, {fail_count} 失败, {placeholder_count} 疑似占位图")

# 第四步：替换 HTML 文件中的 URL
print("\n=== 第四步：替换所有 HTML 文件中的 trae-api URL ===")
replace_count_total = 0
files_replaced = 0

for fn in sorted(files_touched):
    fpath = os.path.join(HTML_DIR, fn)
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  [跳过] {fn}: 读取失败: {e}")
        continue

    original_content = content
    replace_count_this = 0

    for url, fname_img in url_to_filename.items():
        relative_path = f"img/{fname_img}"
        count = content.count(url)
        if count > 0:
            content = content.replace(url, relative_path)
            replace_count_this += count

    if content != original_content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_replaced += 1
        replace_count_total += replace_count_this
        print(f"  ✓ {fn}: 替换 {replace_count_this} 处")
    else:
        print(f"  - {fn}: 未找到可替换内容")

print(f"\n=== 替换完成: {files_replaced} 个文件, 共 {replace_count_total} 处替换 ===")
report_lines.append(f"\nHTML 文件替换: {files_replaced} 个文件, {replace_count_total} 处替换")

# 写入报告
report_lines.append("\n")
report_lines.append("=== 文件映射详情 ===")
for url, fname in url_to_filename.items():
    report_lines.append(f"img/{fname}  <-  {url}")

report_path = os.path.join(IMG_DIR, "_download_report.txt")
with open(report_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report_lines))

print(f"\n✓ 报告已保存到: {report_path}")
print("\n=== 全部完成 ===")
print(f"  图片目录: {IMG_DIR}/")
print(f"  下载文件数: {success_count}")
print(f"  失败数: {fail_count}")
print(f"  占位图数: {placeholder_count}")
print(f"  替换 HTML 文件: {files_replaced} 个")
print(f"  总替换处数: {replace_count_total}")
