"""Three-viewport validation for all 5 case pages."""
from playwright.sync_api import sync_playwright
import os, re

PAGES = [
    ("1", "case-1-jakarta-cikampek-elevated-toll-noise-barrier"),
    ("2", "case-2-jakarta-bandung-hsr-railway-acoustic-barrier"),
    ("3", "case-3-volkswagen-wolfsburg-industrial-noise-barrier"),
    ("4", "case-4-sydney-pennant-hills-residential-noise-barrier"),
    ("5", "case-5-neom-saudi-solar-noise-barrier"),
]
VIEWPORTS = [("desktop", 1280, 900), ("tablet", 900, 1100), ("mobile", 390, 844)]
OUT_DIR = "/workspace/html/_preview"
os.makedirs(OUT_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for cid, slug in PAGES:
        url = f"http://localhost:8765/../pages/case-studies/{slug}.html"
        for vname, w, h in VIEWPORTS:
            ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=1)
            page = ctx.new_page()
            page.goto("file:///workspace/pages/case-studies/" + slug + ".html", wait_until="networkidle")
            scroll_w = page.evaluate("document.documentElement.scrollWidth")
            client_w = page.evaluate("document.documentElement.clientWidth")
            h1c = page.locator("h1").count()
            h2c = page.locator("h2").count()
            h3c = page.locator("h3").count()
            meta_title = page.title()
            overflow = scroll_w - client_w
            print(f"  case-{cid} [{vname} {w}x{h}]  overflow={overflow}px  H1={h1c} H2={h2c} H3={h3c}  title='{meta_title[:60]}'")
            # Take full-page screenshot
            page.screenshot(path=f"{OUT_DIR}/case-{cid}-{vname}-full.png", full_page=True)
            ctx.close()
    browser.close()
print("\nAll screenshots in", OUT_DIR)
