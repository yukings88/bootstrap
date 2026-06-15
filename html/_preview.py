"""Three-viewport screenshot validation for the Yukings case study template."""
from playwright.sync_api import sync_playwright
import os

URL = "http://localhost:8765/case-template.html"
OUT_DIR = "/workspace/html/_preview"
os.makedirs(OUT_DIR, exist_ok=True)

VIEWPORTS = [
    ("desktop", 1280, 900),
    ("tablet",  900,  1100),
    ("mobile",  390,  844),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for name, w, h in VIEWPORTS:
        ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=1)
        page = ctx.new_page()
        page.goto(URL, wait_until="networkidle")
        out_full = f"{OUT_DIR}/case-template-{name}-full.png"
        out_top  = f"{OUT_DIR}/case-template-{name}-top.png"
        page.screenshot(path=out_full, full_page=True)
        page.screenshot(path=out_top, full_page=False)
        # check for horizontal overflow
        scroll_w = page.evaluate("document.documentElement.scrollWidth")
        client_w  = page.evaluate("document.documentElement.clientWidth")
        # verify the 8 module headings are present
        h1 = page.locator("h1").count()
        h2 = page.locator("h2").count()
        h3 = page.locator("h3").count()
        sections = page.locator("section, header, footer").count()
        print(f"[{name} {w}x{h}] scrollW={scroll_w} clientW={client_w}  overflow={scroll_w - client_w}px  "
              f"H1={h1} H2={h2} H3={h3}  sections+header+footer={sections}")
        ctx.close()
    browser.close()

print("\nScreenshots saved to", OUT_DIR)
for f in sorted(os.listdir(OUT_DIR)):
    p = os.path.join(OUT_DIR, f)
    print(f"  {f}  ({os.path.getsize(p)//1024} KB)")
