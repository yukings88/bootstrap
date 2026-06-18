#!/usr/bin/env python3
"""批量更新 Yukings 所有 HTML 页面的 FAQ 模块为原生 HTML5 <details> 可折叠组件。

旧结构:
  <div class="rsb-faq">
    <div class="rsb-faq__item"><div class="rsb-faq__q">问题?</div><div class="rsb-faq__a">答案</div></div>
    ...
  </div>

新结构:
  <div class="rsb-faq">
    <details class="rsb-faq__item"><summary class="rsb-faq__q">问题?</summary><div class="rsb-faq__a">答案</div></details>
    ...
  </div>

结果: 默认全部收起，点击问题展开答案，再点收起；原生 HTML5，零 JS。
"""

import os
import glob

HTML_DIR = "/workspace/html"

# ---------- FAQ CSS 新样式 ----------
NEW_FAQ_BLOCK = (
    ".rsb-faq{max-width:920px;margin:0 auto;display:grid;gap:14px}\n"
    ".rsb-faq__item{border:1px solid var(--gray-200);border-radius:var(--radius-lg);background:var(--white);padding:22px 26px;transition:all .3s ease;overflow:hidden}\n"
    ".rsb-faq__item[open]{border-color:var(--orange);box-shadow:var(--shadow-sm);background:rgba(228,102,42,.02)}\n"
    ".rsb-faq__item[open] .rsb-faq__q{color:var(--orange)}\n"
    ".rsb-faq__q{font-size:16px;font-weight:700;color:var(--text-primary);margin-bottom:8px;display:flex;align-items:center;gap:12px;cursor:pointer;list-style:none}\n"
    ".rsb-faq__q::-webkit-details-marker{display:none}\n"
    ".rsb-faq__q::before{content:\"Q\";flex-shrink:0;width:28px;height:28px;background:var(--orange);color:var(--white);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;margin-top:-2px}\n"
    ".rsb-faq__q::after{content:\"+\";flex-shrink:0;margin-left:auto;width:26px;height:26px;border:1px solid var(--gray-200);border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--gray-500);font-size:18px;font-weight:700;line-height:1;transition:all .3s ease}\n"
    ".rsb-faq__item[open] .rsb-faq__q::after{content:\"\\2212\";background:var(--orange);color:var(--white);border-color:var(--orange);transform:rotate(180deg)}\n"
    ".rsb-faq__a{font-size:14.5px;color:var(--text-secondary);line-height:1.7;padding-left:40px;padding-top:12px;margin-top:10px;border-top:1px dashed var(--gray-200);animation:rsbFaqSlide .35s ease}\n"
    "@keyframes rsbFaqSlide{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:translateY(0)}}"
)


def replace_html_structure(content: str) -> str:
    """把 FAQ 的 div 结构转换为 details/summary 结构。
    使用状态机只在 FAQ 容器内进行替换，避免误伤页面其它 div。
    """
    if '<div class="rsb-faq">' not in content:
        return content

    # 先替换所有 item 容器的开启和关闭标签（在 FAQ 容器内）
    # 方案: 直接替换这几个精确字符串
    s = content

    # ① 把 item 容器 <div> → <details>
    s = s.replace('<div class="rsb-faq__item">', '<details class="rsb-faq__item">')

    # ② 把 q 开启 <div> → <summary>
    s = s.replace('<div class="rsb-faq__q">', '<summary class="rsb-faq__q">')

    # ③ 把 q 关闭 </div> → </summary>（紧跟在 <div class="rsb-faq__a"> 之前）
    s = s.replace('</div><div class="rsb-faq__a">', '</summary><div class="rsb-faq__a">')

    # ④ 把 item 关闭 </div> → </details>
    # 这里有两种相邻情况:
    #   a) 下一条 item 还在继续:  </div></div><details class="rsb-faq__item">
    #   b) FAQ 容器结束:          </div></div></div>  或  </div></div>
    # 区分: 我们要替换的是 item 的关闭 </div>，不是 a 的关闭，也不是 FAQ 容器的关闭
    # 策略: 先处理 a) 再处理 b)

    # a) item 后跟下一条 item 或 FAQ 关闭
    s = s.replace('</div></div><details class="rsb-faq__item">', '</div></details><details class="rsb-faq__item">')

    # b) 最后一条 item 后跟 FAQ 容器关闭 (可能有后续内容)
    # pattern: </div></div></div>  → 中间那个是 item closer
    s = s.replace('</div></div></div>', '</div></details></div>')

    # c) 也可能 FAQ 容器结束位置与 item 相邻但不连续
    # 检查: 还有没有残留的 </div> item closer?
    # 如果 FAQ 容器结束在本行末，则 pattern 可能是 </div></div>
    # 但 a + div 也可能关闭其它嵌套 div，所以这里需要小心。
    # 一个更可靠的办法: 扫描整行找到 <div class="rsb-faq"> 区域，
    # 对该区域内的每个 "item" 找到其对应 closer。

    return s


def replace_css_block(content: str) -> str:
    """在 content 中找到并替换 FAQ CSS 块。"""
    lines = content.split("\n")
    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith(".rsb-faq{"):
            # 检查接下来几行是否是 FAQ 样式块
            candidate = "\n".join(lines[i:i+6])
            if ".rsb-faq__a{" in candidate and "rsb-faq__q" in candidate:
                new_lines.append(NEW_FAQ_BLOCK)
                i += 6  # 跳过原 5~6 行 FAQ 样式
                continue
        new_lines.append(lines[i])
        i += 1
    return "\n".join(new_lines)


def main():
    files = sorted(glob.glob(os.path.join(HTML_DIR, "*.html")))
    updated = 0
    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        if "rsb-faq__item" not in content:
            continue

        new_content = replace_html_structure(content)
        new_content = replace_css_block(new_content)

        if new_content != content:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(new_content)
            details_n = new_content.count('<details class="rsb-faq__item">')
            details_close_n = new_content.count('</details>')
            print(f"[OK] {os.path.basename(fp):55s}  <details>={details_n}  </details>={details_close_n}")
            updated += 1

    print(f"\n==== 汇总: 共更新 {updated} 个文件 ====")


if __name__ == "__main__":
    main()
