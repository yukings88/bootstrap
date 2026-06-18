#!/usr/bin/env python3
"""修复 v1 脚本的遗留问题：FAQ items 已改为 <details> 开启，但关闭仍为 </div>。
本脚本将所有 FAQ item 的最后一个 </div> 改为 </details>。

当前文件状态示例:
  <div class="rsb-faq">
    <details class="rsb-faq__item">
      <summary class="rsb-faq__q">Q?</summary>
      <div class="rsb-faq__a">A</div>
    </div>                ← 这是 item closer，应为 </details>
    <details class="rsb-faq__item">...
    ...
  </div>

修复规则: 在 FAQ 容器内，把 item closer 的 </div> 改为 </details>。
通过定位 <details class="rsb-faq__item"> 与它配对的 closer 完成。
"""

import os
import glob

HTML_DIR = "/workspace/html"


def fix_item_closers(content: str) -> str:
    """在 FAQ 容器内找到 <details class="rsb-faq__item"> 对应的 closer 并修复。

    关键模式:
      ...answer text...</div></div><details class="rsb-faq__item">...
      ...last answer...</div></div></div>
                        ↑↑↑ 第二个 </div> 应改为 </details>

    算法: 从左到右扫描，遇到 <details class="rsb-faq__item"> 后设状态为 "在 item 内"；
    遇到 </div></div> 时把第二个 </div> 替换为 </details> 并清除状态。
    """
    if '<details class="rsb-faq__item">' not in content:
        return content

    out = []
    i = 0
    n = len(content)
    in_item = False
    DETAILS_OPEN = '<details class="rsb-faq__item">'
    CLOSE_PAIR = '</div></div>'
    len_open = len(DETAILS_OPEN)
    len_pair = len(CLOSE_PAIR)

    while i < n:
        if in_item and i + len_pair <= n and content[i:i+len_pair] == CLOSE_PAIR:
            # 这是 a closer + item closer → 改为 </div></details>
            out.append('</div></details>')
            in_item = False
            i += len_pair
            continue
        if not in_item and i + len_open <= n and content[i:i+len_open] == DETAILS_OPEN:
            out.append(DETAILS_OPEN)
            in_item = True
            i += len_open
            continue
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

        if '<details class="rsb-faq__item">' not in content:
            continue

        # 统计当前 state
        open_before = content.count('<details class="rsb-faq__item">')
        close_before = content.count('</details>')

        new_content = fix_item_closers(content)

        if new_content != content:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(new_content)
            open_after = new_content.count('<details class="rsb-faq__item">')
            close_after = new_content.count('</details>')
            print(f"[OK] {os.path.basename(fp):55s}  open:{open_after}  close:{close_after}  (was close:{close_before})")
            updated += 1

    print(f"\n==== 共修复 {updated} 个文件 ====")


if __name__ == "__main__":
    main()
