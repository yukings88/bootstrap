import os
OUT = "/workspace/html"
os.makedirs(OUT, exist_ok=True)

with open(os.path.join(OUT, "_css.txt"), "r", encoding="utf-8") as f:
    CSS = f.read()
with open(os.path.join(OUT, "_parts.txt"), "r", encoding="utf-8") as f:
    PARTS = f.read()

# Execute parts as Python module (very small)
ns = {}
exec(PARTS, ns)
nav = ns["nav"]
topbar = ns["topbar"]
breadcrumb = ns["breadcrumb"]
footer = ns["footer"]
cookie = ns["cookie"]
hero = ns["hero"]
sec_head = ns["sec_head"]
card = ns["card"]
cards_grid = ns["cards_grid"]
split = ns["split"]
stat = ns["stat"]
feat = ns["feat"]
spec_tbl = ns["spec_tbl"]
faq_blk = ns["faq_blk"]
cta = ns["cta"]
form = ns["form"]
timeline = ns["timeline"]
team_blk = ns["team_blk"]
cert_blk = ns["cert_blk"]
article_blk = ns["article_blk"]
chips = ns["chips"]
page_head = ns["page_head"]
close_page = ns["close_page"]
write_page = ns["write_page"]
build_pages = ns["build_pages"]

build_pages(OUT, CSS)
print("[done] all pages written")
