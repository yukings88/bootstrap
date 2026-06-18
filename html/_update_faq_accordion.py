#!/usr/bin/env python3
"""批量更新 Yukings 所有 HTML 页面的 FAQ 模块为原生 HTML5 <details> 可折叠组件（默认收起）。

操作：
  1. 更新 .rsb-faq CSS 块，加入 details/summary 样式（展开动画、箭头、hover）
  2. 把 HTML 中的 <div class="rsb-faq__item"><div class="rsb-faq__q">Q</div><div class="rsb-faq__a">A</div></div>
     替换为  <details class="rsb-faq__item"><summary class="rsb-faq__q">Q</summary><div class="rsb-faq__a">A</div></details>

结果：默认全部收起，点击问题展开答案，再点收起；原生 HTML5，零 JS。
"""

import os
import re
import glob

HTML_DIR = "/workspace/html"


# ---------- 1. 替换 HTML FAQ 条目结构 ----------
# 模式：<div class="rsb-faq__item"><div class="rsb-faq__q">Q</div><div class="rsb-faq__a">A</div></div>
# 注意：Q/A 可能跨多行，也可能在单行，因此用非贪婪匹配
ITEM_OPEN_RE = re.compile(r'<div\s+class="rsb-faq__item">\s*<div\s+class="rsb-faq__q">')
ITEM_CLOSE_RE = re.compile(r'</div>\s*</div>\s*(?=<details|<div class="rsb-faq__item"|</div>\s*</div|$)')

def convert_faq_items(content: str) -> str:
    """三步替换，确保 FAQ item 从 <div> 结构变为 <details>/<summary> 结构。
    原结构: <div class="rsb-faq__item"><div class="rsb-faq__q">Q</div><div class="rsb-faq__a">A</div></div>
    新结构: <details class="rsb-faq__item"><summary class="rsb-faq__q">Q</summary><div class="rsb-faq__a">A</div></div></details>
    """
    # ① 把问题 <div> 改为 <summary>，其后紧跟的 </div>（在 a 开始之前）改为 </summary>
    content = re.sub(
        r'<div\s+class="rsb-faq__q">',
        '<summary class="rsb-faq__q">',
        content,
    )
    # ② 把 </div><div class="rsb-faq__a"> 改为 </summary><div class="rsb-faq__a">（只在 FAQ 内出现）
    content = content.replace(
        '</div><div class="rsb-faq__a">',
        '</summary><div class="rsb-faq__a">',
    )
    # ③ 把 item 容器 <div> 改为 <details>
    content = re.sub(
        r'<div\s+class="rsb-faq__item">',
        '<details class="rsb-faq__item">',
        content,
    )
    # 现在需要把 item 的闭合 </div></div> 替换为 </div></details>
    # 这是关键：每个 rsb-faq__item 结构是 <details class="rsb-faq__item"><summary ...>Q</summary><div class="rsb-faq__a">A</div></div></div>
    # 我们需要找到 "...</div></div>" 紧跟在 rsb-faq__a 之后（或对应一个 item 结束）
    # 由于文件压缩（单行多 item），我们用更精准的方案：
    # 每个 item 结尾模式是：</div></div> 其中 </div> 是关闭 a，然后是关闭 item
    # 但文件中可能多个 item 紧挨：</div></div><details class="rsb-faq__item">...
    # 因此我们只需要替换紧跟 <details 或 紧邻其他位置的闭合组合
    # 但这样做有风险。换一种更稳妥的方法：基于计数器/解析。

    # 更稳妥做法：从头到尾逐字符扫描，跟踪 rsb-faq__item 级别
    return _fix_item_close(content)


def _fix_item_close(content: str) -> str:
    """把 rsb-faq__item 的闭合 </div></div> 改为 </div></details>
    关键问题是压缩 HTML 中 item 紧密相连，例如：
    ...</div></div><details class="rsb-faq__item"><summary class="rsb-faq__q">...
    所以我们只把 <details class="rsb-faq__item"> ... </summary> ...answer... 之后的
    第一个 </div></div> 对（即关闭 a 和 item 的那对）替换成 </div></details>。
    算法：用状态机扫描。
    """
    # 先找出每个 <details class="rsb-faq__item"> 的位置，然后定位其对应的 summary 闭合，
    # 之后寻找成对的 </div></div> 作为关闭 a 和 item
    # 但这仍然复杂。简化：从左到右，遇到 details item 开始，标记 "待替换"；
    # 在 "待替换" 状态下，遇到第一个 </div></div> 就替换为 </div></details> 并清除状态。

    out = []
    i = 0
    n = len(content)
    in_item = False
    while i < n:
        if in_item and content[i:i+12] == "</div></div>":
            out.append("</div></details>")
            in_item = False
            i += 12
            continue
        if not in_item and content[i:i+29] == '<details class="rsb-faq__item">':
            in_item = True
            out.append(content[i:i+29])
            i += 29
            continue
        out.append(content[i])
        i += 1
    return "".join(out)


# ---------- 2. 替换 FAQ CSS 块 ----------
# 原 FAQ 样式开始位置
OLD_FAQ_BLOCK = (
    ".rsb-faq{max-width:920px;margin:0 auto;display:grid;gap:14px}\n"
    ".rsb-faq__item{border:1px solid var(--gray-200);border-radius:var(--radius-lg);background:var(--white);padding:22px 26px;transition:all .3s ease}\n"
    ".rsb-faq__item:hover{border-color:var(--orange);box-shadow:var(--shadow-sm)}\n"
    ".rsb-faq__q{font-size:16px;font-weight:700;color:var(--text-primary);margin-bottom:8px;display:flex;align-items:flex-start;gap:12px}\n"
    ".rsb-faq__q::before{content:\"Q\";flex-shrink:0;width:28px;height:28px;background:var(--orange);color:var(--white);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;margin-top:-2px}\n"
    ".rsb-faq__a{font-size:14.5px;color:var(--text-secondary);line-height:1.7;padding-left:40px}"
)

NEW_FAQ_BLOCK = (
    ".rsb-faq{max-width:920px;margin:0 auto;display:grid;gap:14px}\n"
    ".rsb-faq__item{border:1px solid var(--gray-200);border-radius:var(--radius-lg);background:var(--white);padding:22px 26px;transition:all .3s ease;overflow:hidden}\n"
    ".rsb-faq__item[open]{border-color:var(--orange);box-shadow:var(--shadow-sm);background:rgba(228,102,42,.02)}\n"
    ".rsb-faq__item[open] .rsb-faq__q{color:var(--orange)}\n"
    ".rsb-faq__q{font-size:16px;font-weight:700;color:var(--text-primary);margin-bottom:8px;display:flex;align-items:center;gap:12px;cursor:pointer;list-style:none}\n"
    ".rsb-faq__q::-webkit-details-marker{display:none}\n"
    ".rsb-faq__q::before{content:\"Q\";flex-shrink:0;width:28px;height:28px;background:var(--orange);color:var(--white);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;margin-top:-2px}\n"
    ".rsb-faq__q::after{content:\"+\";flex-shrink:0;margin-left:auto;width:26px;height:26px;border:1px solid var(--gray-200);border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--gray-500);font-size:18px;font-weight:700;line-height:1;transition:all .3s ease}\n"
    ".rsb-faq__item[open] .rsb-faq__q::after{content:\"−\";background:var(--orange);color:var(--white);border-color:var(--orange);transform:rotate(180deg)}\n"
    ".rsb-faq__a{font-size:14.5px;color:var(--text-secondary);line-height:1.7;padding-left:40px;padding-top:12px;margin-top:10px;border-top:1px dashed var(--gray-200);animation:rsbFaqSlide .35s ease}\n"
    "@keyframes rsbFaqSlide{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:translateY(0)}}"
)


def update_css_block(content: str) -> str:
    """在 content 中找到并替换 FAQ CSS 块。若找不到，记录返回。"""
    # 由于不同文件中行的空白可能略有不同，我们用更宽松的方式：
    # 查找 ".rsb-faq{" 开始的 5 行（含 rsb-faq__item, hover, q, q::before, a）
    # 逐行匹配替换。
    lines = content.split("\n")
    new_lines = []
    i = 0
    replaced = False
    while i < len(lines):
        if not replaced and lines[i].strip().startswith(".rsb-faq{"):
            # 检查接下来几行是否是 FAQ 样式块
            candidate = "\n".join(lines[i:i+6])
            if ".rsb-faq__a{" in candidate and "rsb-faq__q" in candidate:
                new_lines.append(NEW_FAQ_BLOCK)
                i += 6  # 跳过原 5~6 行 FAQ 样式
                replaced = True
                continue
        new_lines.append(lines[i])
        i += 1
    return "\n".join(new_lines), replaced


# ---------- 3. 主流程 ----------
def main():
    files = sorted(glob.glob(os.path.join(HTML_DIR, "*.html")))
    processed = 0
    css_updated = 0
    html_updated = 0
    skipped = []

    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"[SKIP] 读文件失败 {os.path.basename(fp)}: {e}")
            skipped.append(fp)
            continue

        if "rsb-faq__item" not in content:
            continue  # 该页面没有 FAQ，跳过

        processed += 1

        # 1) HTML 结构替换
        has_q_div = '<div class="rsb-faq__q">' in content
        if has_q_div:
            new_content = convert_faq_items(content)
        else:
            new_content = content

        # 2) FAQ CSS 替换
        new_content, css_ok = update_css_block(new_content)

        if new_content != content:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(new_content)
            html_updated += 1
            if css_ok:
                css_updated += 1

            # 简单统计
            details_n = new_content.count('<details class="rsb-faq__item">')
            print(f"[OK] {os.path.basename(fp):55s} FAQ items = {details_n}")
        else:
            print(f"[SKIP] {os.path.basename(fp):55s} 无变化")

    print()
    print(f"==== 汇总 ====")
    print(f"扫描 HTML 文件: {len(files)} 个")
    print(f"含 FAQ 模块: {processed} 个")
    print(f"成功更新: {html_updated} 个（其中同步更新 CSS: {css_updated} 个）")
    if skipped:
        print(f"读文件跳过: {len(skipped)} 个")


if __name__ == "__main__":
    main()
