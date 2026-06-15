#!/usr/bin/env python3
"""Fix Python-syntax leftovers in products_bcde_data.json (product 20)."""
import re
import json
from pathlib import Path

path = Path("/workspace/products_bcde_data.json")
text = path.read_text(encoding="utf-8")

# 1) Replace img("...")  with  "..."  (Python function call)
# Match img("..."), possibly followed by , or )
text = re.sub(r'img\("([^"]*)"\)', r'"\1"', text)

# 2) Replace Python tuple syntax `(...)` with `[...]` at line starts.
# The pattern in the file: list items that start with `(`
# We split by lines and only fix lines inside list contexts.
# Heuristic: a line that begins with whitespace then `(` should begin with `[`.
new_lines = []
for line in text.splitlines(keepends=True):
    stripped = line.lstrip()
    indent = line[: len(line) - len(stripped)]
    if stripped.startswith("("):
        # Convert leading ( to [
        line = indent + "[" + stripped[1:]
    new_lines.append(line)
text = "".join(new_lines)

# 3) Now convert trailing `)` to `]` (line-level).
# Be careful: we only want closing tuples inside list contexts.
# Simple heuristic: lines that end with `)` and have unbalanced structure.
# Track depth: scan each character. When we see a `)` at end of line where
# depth suggests it's closing a tuple, convert.
def fix_closing_parens(text):
    out = []
    bracket_depth = 0
    for ch in text:
        if ch == "[":
            bracket_depth += 1
        elif ch == "]":
            bracket_depth = max(0, bracket_depth - 1)
        # If we are inside a list and we see `)`, replace with `]`
        if ch == ")" and bracket_depth > 0:
            out.append("]")
        else:
            out.append(ch)
    return "".join(out)

text = fix_closing_parens(text)

# 4) Fix the final `]` of product 20 to `}` (closing brace for the dict).
# Product 20 ends at the very last line of the file. The file structure is:
#   }   <- end of product 20 object (was `]` in corrupted form)
#   }   <- end of root dict
# So if the very last non-empty line is `  }` (close of root), and the line
# above ends with `]` instead of `}`, replace the line above's last `]` with `}`.
lines = text.splitlines()
# Find last "  }" (root close)
for i in range(len(lines) - 1, -1, -1):
    if lines[i].strip() == "}":
        root_close = i
        break
# Line above should be product 20's last item, e.g. `    ]`
if root_close >= 1:
    prev = lines[root_close - 1]
    if prev.strip() == "]":
        # The product 20 dict was closed with `]`. Change to `}`.
        lines[root_close - 1] = prev.replace("]", "}", 1)
text = "\n".join(lines)
if not text.endswith("\n"):
    text += "\n"

path.write_text(text, encoding="utf-8")

# Verify
try:
    data = json.loads(text)
    print(f"OK — JSON parses. Top-level keys: {sorted(data.keys(), key=int)}")
except json.JSONDecodeError as e:
    print(f"ERROR at line {e.lineno} col {e.colno}: {e.msg}")
    # Print 5 lines around the error
    lines = text.splitlines()
    for i in range(max(0, e.lineno - 3), min(len(lines), e.lineno + 2)):
        marker = " <-- HERE" if i + 1 == e.lineno else ""
        print(f"  {i+1:4}: {lines[i]}{marker}")
