#!/usr/bin/env python3
"""通用 FAQ 折叠组件转换器 - 处理所有 pattern:
  Pattern 1: <div class="rsb-faq__item"><div class="rsb-faq__q">Q</div><div class="rsb-faq__a">A</div></div>
  Pattern 2: <div class="rsb-faq__item"><h3 class="rsb-faq__q">Q</h3><p class="rsb-faq__a">A</p></div>
  都转换为:
  <details class="rsb-faq__item"><summary class="rsb-faq__q">Q</summary><div class="rsb-faq__a">A</div></details>
  或
  <details class="rsb-faq__item"><summary class="rsb-faq__q">Q</summary><p class="rsb-faq__a">A</p></details>
"""

import os
import glob
import re

HTML_DIR = "/workspace/html"


def convert_faq(content: str) -> str:
    """在 FAQ 容器内把 FAQ item 从 div 改为 details/summary。"""
    if '<div class="rsb-faq">' not in content:
        return content

    # ① item 容器开启: <div class="rsb-faq__item"> → <details class="rsb-faq__item">
    s = content.replace('<div class="rsb-faq__item">', '<details class="rsb-faq__item">')

    # ② 问题开启: <h3|div class="rsb-faq__q"> → <summary class="rsb-faq__q">
    s = re.sub(r'<(?:h3|div|h2|h4|p)\s+class="rsb-faq__q">', '<summary class="rsb-faq__q">', s)

    # ③ 问题关闭: </h3> 或 </div> 等，紧接着 <p|div class="rsb-faq__a">
    s = re.sub(r'</(?:h3|h2|h4|div|p)><(p|div)\s+class="rsb-faq__a">',
               r'</summary><\1 class="rsb-faq__a">', s)

    # ④ item 容器关闭: </div> → </details>
    # 用状态机追踪嵌套深度，找到 item 对应的 </div> 并替换为 </details>
    return _fix_remaining_item_closers(s)


def _fix_remaining_item_closers(content: str) -> str:
    """扫描并修复 <details class="rsb-faq__item"> 的 closer 标签。
    找到每一个 <details class="rsb-faq__item"> 后，追踪内部嵌套深度，
    当其内部所有标签都已平衡时遇到的 </div> 就是 item closer。
    """
    if '<details class="rsb-faq__item">' not in content:
        return content

    # 检查是否已经完全匹配
    open_count = content.count('<details class="rsb-faq__item">')
    close_count = content.count('</details>')
    if open_count == close_count:
        return content  # 已完成

    DETAILS_OPEN = '<details class="rsb-faq__item">'
    # 进入 <details class="rsb-faq__item"> 后，深度计数器从 0 开始。
    # 每遇到一个跟踪的内部开标签 +1，关标签 -1。
    # 当深度回到 0（表示所有内部内容都已闭合）且下一个 </div> 就是 item closer。
    tracked_tags = ('div', 'p', 'span', 'h2', 'h3', 'h4', 'ul', 'ol', 'li',
                    'section', 'article', 'a', 'strong', 'em', 'summary')
    void_tags = ('br', 'hr', 'img', 'input', 'meta', 'link')
    out = []
    i = 0
    n = len(content)
    in_item = False
    depth = 0  # 内部标签深度

    while i < n:
        if not in_item and i + len(DETAILS_OPEN) <= n and content[i:i+len(DETAILS_OPEN)] == DETAILS_OPEN:
            out.append(DETAILS_OPEN)
            in_item = True
            depth = 0
            i += len(DETAILS_OPEN)
            continue

        if in_item:
            tag_match = re.match(r'<(/?)([a-zA-Z0-9]+)(?:\s[^>]*)?>', content[i:])
            if tag_match:
                is_closing = tag_match.group(1) == '/'
                tag_name = tag_match.group(2).lower()
                tag_full = tag_match.group(0)

                if tag_name in void_tags or tag_full.endswith('/>'):
                    pass  # 自闭合标签
                elif tag_name in tracked_tags:
                    if not is_closing:
                        depth += 1
                    else:
                        # 关闭：如果 depth == 0 且是 div → item closer
                        if depth == 0 and tag_name == 'div':
                            out.append('</details>')
                            i += len(tag_full)
                            in_item = False
                            continue
                        depth -= 1

        out.append(content[i])
        i += 1

    return ''.join(out)


def main():
    files = sorted(glob.glob(os.path.join(HTML_DIR, "*.html")))
    updated = 0
    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        if '<div class="rsb-faq">' not in content:
            continue

        # 跳过已经完全转换为 details 的文件
        # 检查：如果已经有 <details class="rsb-faq__item"> 同时有匹配的 </details>，则跳过
        if '<details class="rsb-faq__item">' in content and '</details>' in content:
            open_count = content.count('<details class="rsb-faq__item">')
            close_count = content.count('</details>')
            if open_count == close_count:
                continue  # 已完全转换

        new_content = convert_faq(content)
        if new_content != content:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(new_content)
            o = new_content.count('<details class="rsb-faq__item">')
            c = new_content.count('</details>')
            print(f"[OK] {os.path.basename(fp):55s}  <details>={o}  </details>={c}")
            updated += 1

    print(f"\n==== 共更新 {updated} 个文件 ====")


if __name__ == "__main__":
    main()
