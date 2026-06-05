#!/usr/bin/env python3
"""
Bing图片搜索+下载脚本
- 读取./cdn/待搜图片清单.md
- 按关键词组在bing.com/images检索
- 每组下载前6张高清图
- 统一转为.webp存到./cdn/对应类目
"""
import os
import re
import time
import urllib.parse
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from bs4 import BeautifulSoup

CDN_ROOT = "/workspace/cdn"
CDN_BANNER = os.path.join(CDN_ROOT, "banner")
CDN_PRODUCT = os.path.join(CDN_ROOT, "product")
CDN_CASE = os.path.join(CDN_ROOT, "case")

os.makedirs(CDN_BANNER, exist_ok=True)
os.makedirs(CDN_PRODUCT, exist_ok=True)
os.makedirs(CDN_CASE, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# 从markdown清单解析 (分类|搜图关键词|本地保存路径)
MD_FILE = os.path.join(CDN_ROOT, "待搜图片清单.md")
jobs = []
with open(MD_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line.startswith("|") or "---" in line or "分类" in line:
            continue
        parts = [p.strip() for p in line.split("|") if p.strip()]
        if len(parts) >= 3:
            jobs.append((parts[0], parts[1], parts[2]))

print(f"[INFO] 解析到 {len(jobs)} 个下载任务")

def search_bing_images(query, limit=6):
    """Bing图片搜索，返回图片URL列表"""
    encoded = urllib.parse.quote_plus(query)
    url = f"https://www.bing.com/images/search?q={encoded}&form=HDRSC2&first=1&count=20"
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        if r.status_code != 200:
            print(f"  [WARN] HTTP {r.status_code}")
            return []
    except Exception as e:
        print(f"  [WARN] 请求失败: {e}")
        return []
    # 提取 murl 字段（媒体原图URL）
    urls = re.findall(r'"murl":"(https?://[^"]+\.(?:jpg|jpeg|png|webp))(?:\?[^"]*)?"', r.text)
    return urls[:limit]

def download_image(url, timeout=15):
    """下载图片二进制"""
    try:
        r = requests.get(url, headers={**HEADERS, "Referer": "https://www.bing.com/"}, timeout=timeout, stream=True)
        if r.status_code != 200:
            return None
        return r.content
    except Exception:
        return None

def save_as_webp(data, out_path, target_size=None):
    """保存为webp，可选调整尺寸"""
    try:
        img = Image.open(BytesIO(data)).convert("RGB")
        if target_size:
            img.thumbnail(target_size, Image.LANCZOS)
        img.save(out_path, "WEBP", quality=85, method=4)
        return True
    except Exception as e:
        print(f"    [WARN] webp转换失败: {e}")
        return False

def make_placeholder(keyword, out_path, w, h):
    """生成品牌色占位webp"""
    img = Image.new("RGB", (w, h), (8, 36, 87))  # #082457
    draw = ImageDraw.Draw(img)
    # 标题文字
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except Exception:
        font = ImageFont.load_default()
        font_small = font
    # 强调色斜条
    draw.rectangle([0, 0, 12, h], fill=(228, 102, 42))  # #E4662A
    # 文本
    text = "YUKINGS"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((w - tw) // 2, h // 2 - 30), text, fill=(255, 255, 255), font=font)
    # 关键词
    kw = keyword[:60]
    bbox2 = draw.textbbox((0, 0), kw, font=font_small)
    tw2 = bbox2[2] - bbox2[0]
    draw.text(((w - tw2) // 2, h // 2 + 10), kw, fill=(228, 102, 42), font=font_small)
    img.save(out_path, "WEBP", quality=85, method=4)

# 类目尺寸预设
SIZE_MAP = {
    "banner": (1920, 520),
    "product": (800, 600),
    "case": (1000, 600),
}

# 任务执行
stats = {"bing_ok": 0, "placeholder": 0, "fail": 0}
for idx, (cat, kw, local_path) in enumerate(jobs, 1):
    fname = os.path.basename(local_path)
    out_full = os.path.join(CDN_ROOT, cat, fname)
    if os.path.exists(out_full) and os.path.getsize(out_full) > 1000:
        print(f"[{idx}/{len(jobs)}] 已存在: {fname}")
        stats["bing_ok"] += 1
        continue
    w, h = SIZE_MAP.get(cat, (800, 600))
    print(f"[{idx}/{len(jobs)}] {cat}/{fname} | kw={kw[:50]}...")
    # Bing搜索 + 下载
    urls = search_bing_images(kw, limit=6)
    saved = False
    for u in urls:
        data = download_image(u)
        if data and len(data) > 5000:
            if save_as_webp(data, out_full, (w, h)):
                print(f"  [OK] {fname} ({os.path.getsize(out_full)//1024}KB)")
                stats["bing_ok"] += 1
                saved = True
                break
        time.sleep(0.3)
    if not saved:
        make_placeholder(kw, out_full, w, h)
        print(f"  [PLACEHOLDER] {fname}")
        stats["placeholder"] += 1
    time.sleep(0.5)

print("\n========== 下载统计 ==========")
print(f"Bing实际下载成功: {stats['bing_ok']}")
print(f"占位图生成: {stats['placeholder']}")
print(f"失败: {stats['fail']}")
print(f"总计: {len(jobs)}")
