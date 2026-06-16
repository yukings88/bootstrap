#!/usr/bin/env python3
"""Update blog.html: replace blog.html article links with correct detail-page URLs."""

path = "/workspace/html/blog.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Map: article title substring -> target filename
replacements = [
    ('How to choose the right noise barrier panel depth', 'blog-noise-barrier-panel-depth-guide.html'),
    ('Understanding EN 1793-1 acoustic performance classification', 'blog-en-1793-acoustic-performance-guide.html'),
    ('Aero-acoustic pulse: high-speed rail barrier design', 'blog-high-speed-rail-aero-acoustic-design.html'),
    ('Solar PV-integrated noise barriers: commercial guide', 'blog-solar-pv-noise-barrier-commercial.html'),
    ('Choosing between aluminum and galvanized steel noise barriers', 'blog-aluminum-vs-galvanized-steel-comparison.html'),
    ('EN 1794 mechanical performance and durability explained', 'blog-en-1794-mechanical-performance-guide.html'),
    ('FAQ deep dive: insertion loss, sound insulation and absorption coefficients', 'blog-insertion-loss-sound-insulation-faq.html'),
    ('Noise barrier project checklist for bidding and construction', 'blog-noise-barrier-project-checklist.html'),
    ('Global noise barrier market snapshot: EU, USA, Australia, Southeast Asia', 'blog-global-noise-barrier-market-report.html'),
]

# Work: for each title occurrence, find the NEXT blog.html link and replace it.
for title, filename in replacements:
    title_pos = content.find(title)
    if title_pos == -1:
        print("  [SKIP] title not found: {}".format(title))
        continue
    # find next href="blog.html" after title in the Read more link
    link_marker = 'Read more &rarr;</a>'
    pos_after = content.find(link_marker, title_pos)
    # Go back to find preceding href="blog.html"
    if pos_after == -1:
        print("  [SKIP] Read more marker not found for: {}".format(title))
        continue
    # Replace the href="blog.html" within 200 chars before Read more
    region_start = max(0, pos_after - 250)
    region_end = pos_after
    region = content[region_start:region_end]
    new_region = region.replace('href="blog.html"', 'href="' + filename + '"', 1)
    if new_region == region:
        print("  [SKIP] no blog.html link found near: {}".format(title[:50]))
        continue
    content = content[:region_start] + new_region + content[region_end:]
    print("  [OK] linked: {} -> {}".format(title[:50], filename))

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("\n  blog.html updated successfully.")
