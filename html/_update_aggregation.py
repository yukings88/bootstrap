#!/usr/bin/env python3
"""Update aggregation sections (By Top Profile → By Barrier Form/Shape)."""
HTML_DIR = "/workspace/html"


# ------ PRODUCTS.HTML ------
with open(f"{HTML_DIR}/products.html", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(
    "organized by acoustic principle, material, application and top profile.",
    "organized by acoustic principle, material, application and barrier form / shape.",
)

old_block = '''<div>
      <h3 style="font-size:22px;margin-bottom:18px;color:var(--text-primary)">By Top Profile</h3>
      <div class="rsb-grid rsb-grid--4" style="grid-template-columns:repeat(3,1fr)">
        <a href="flat-top-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__body">
    <span class="rsb-card__meta">Top Profile</span>
    <h3 class="rsb-card__title" style="font-size:18px">Flat-Top Noise Barriers</h3>
    <p class="rsb-card__text">Classic straight-top profile for uniform barrier lines.</p>
    <span class="rsb-card__link">Explore flat-top barriers &rarr;</span>
  </div>
</a><a href="curved-top-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__body">
    <span class="rsb-card__meta">Top Profile</span>
    <h3 class="rsb-card__title" style="font-size:18px">Curved-Top Noise Barriers</h3>
    <p class="rsb-card__text">Cantilevered curved-crown profile for diffraction control.</p>
    <span class="rsb-card__link">Explore curved-top barriers &rarr;</span>
  </div>
</a><a href="angled-folded-top-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__body">
    <span class="rsb-card__meta">Top Profile</span>
    <h3 class="rsb-card__title" style="font-size:18px">Angled &amp; Folded-Top Noise Barriers</h3>
    <p class="rsb-card__text">Y-shaped and folded-profile tops for enhanced noise reduction.</p>
    <span class="rsb-card__link">Explore angled-top barriers &rarr;</span>
  </div>
</a>
      </div>
    </div>'''

new_block = '''<div>
      <h3 style="font-size:22px;margin-bottom:18px;color:var(--text-primary)">By Barrier Form / Shape</h3>
      <div class="rsb-grid rsb-grid--4" style="grid-template-columns:repeat(3,1fr)">
        <a href="flat-top-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title" style="font-size:18px">Flat Panel Noise Barriers</h3>
    <p class="rsb-card__text">Classic straight-profile modular panels for cost-effective highway, railway and urban noise control.</p>
    <span class="rsb-card__link">Explore flat panel barriers &rarr;</span>
  </div>
</a><a href="curved-top-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title" style="font-size:18px">Curved / Arched Top Noise Barriers</h3>
    <p class="rsb-card__text">Engineered arc-profile cap delivers +3-8 dB additional diffraction attenuation compared to flat-top walls.</p>
    <span class="rsb-card__link">Explore curved-top barriers &rarr;</span>
  </div>
</a><a href="angled-folded-top-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title" style="font-size:18px">Angled / Folded Top Noise Barriers</h3>
    <p class="rsb-card__text">L-shaped cantilever cap creates an extended acoustic shadow zone — highest effective dB per meter height.</p>
    <span class="rsb-card__link">Explore angled-top barriers &rarr;</span>
  </div>
</a><a href="semi-enclosed-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title" style="font-size:18px">Semi-Enclosed Noise Barriers</h3>
    <p class="rsb-card__text">U-shaped / half-tunnel acoustic corridors with integrated transparent windows — 35-50 dB insertion loss.</p>
    <span class="rsb-card__link">Explore semi-enclosed barriers &rarr;</span>
  </div>
</a><a href="fully-enclosed-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title" style="font-size:18px">Fully-Enclosed Noise Barriers</h3>
    <p class="rsb-card__text">360° acoustic tunnel enclosures delivering 45-60 dB insertion loss for HSR and sensitive receiver zones.</p>
    <span class="rsb-card__link">Explore fully-enclosed barriers &rarr;</span>
  </div>
</a>
      </div>
    </div>'''

if old_block in c:
    c = c.replace(old_block, new_block)
    with open(f"{HTML_DIR}/products.html", "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated products.html")
else:
    print("WARNING: products.html block not found (may have whitespace differences)")


# ------ SOLUTIONS.HTML ------
with open(f"{HTML_DIR}/solutions.html", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace(
    "Drill deeper into our noise barrier portfolio by exploring classification pages organized by acoustic principle, material, application and top profile.",
    "Drill deeper into our noise barrier portfolio by exploring classification pages organized by acoustic principle, material, application and barrier form / shape.",
)

# Solutions uses same block pattern but let's check - read the actual content
if old_block in c:
    c = c.replace(old_block, new_block)
    with open(f"{HTML_DIR}/solutions.html", "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated solutions.html")
else:
    print("WARNING: solutions.html block not found - trying alternate match")
    # Try looser match based on h3
    if '<h3 style="font-size:22px;margin-bottom:18px;color:var(--text-primary)">By Top Profile</h3>' in c:
        # Find the section boundaries
        h3_idx = c.index('<h3 style="font-size:22px;margin-bottom:18px;color:var(--text-primary)">By Top Profile</h3>')
        # Find the opening <div> before h3
        div_open = c.rfind('<div>', 0, h3_idx - 5)
        # Find the section end after the cards (look for pattern after last card close)
        # The structure is <div><h3>...</h3><div ...>cards</div></div>
        # Try to find "</div>\n    </div>\n  </div>\n</section>" after
        end_marker = '</div>\n      </div>\n    </div>\n  </div>\n</section>'
        end_idx = c.find(end_marker, h3_idx) + len(end_marker)
        # Replace
        # Reconstruct: <div>\n      + new_block + \n  </div>\n</section>
        # But new_block already has wrapping <div> inside
        # The structure in new_block starts with <div>\n      <h3>... so we need only the inner part
        c = c[:div_open] + new_block + c[end_idx:]
        with open(f"{HTML_DIR}/solutions.html", "w", encoding="utf-8") as f:
            f.write(c)
        print("Updated solutions.html (looser match)")


# ------ INDEX.HTML ------
with open(f"{HTML_DIR}/index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Intro text
c = c.replace(
    "Explore noise barriers grouped by acoustic principle, material, application and top profile to quickly find the right solution for your project.",
    "Explore noise barriers grouped by acoustic principle, material, application and barrier form / shape to quickly find the right solution for your project.",
)

# Replace the single "By Top Profile" card with 5 cards
old_index_card = '''<a href="products.html#tab-categories" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__media">
    <div class="rsb-card__img" style="background-image:url('https://trae-api-cn.mchost.guru/api/ide/v1/text-to-image?prompt=noise-barrier-top-profiles-flat-curved-y-shaped&image_size=landscape_16_9')"></div>
    <span class="rsb-card__tag">TOP PROFILE</span>
  </div>
  <div class="rsb-card__body">
    <span class="rsb-card__meta">Browse by Top Profile</span>
    <h3 class="rsb-card__title">By Top Profile</h3>
    <p class="rsb-card__text">Flat-top, curved-top and angled/folded-top barrier configurations.</p>
    <span class="rsb-card__link">Explore by top profile &rarr;</span>
  </div>
</a>'''

new_index_cards = '''<a href="flat-top-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__media">
    <div class="rsb-card__img" style="background-image:url('https://trae-api-cn.mchost.guru/api/ide/v1/text-to-image?prompt=flat-panel-straight-noise-barrier-highway&image_size=landscape_16_9')"></div>
    <span class="rsb-card__tag">FLAT PANEL</span>
  </div>
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title">Flat Panel Noise Barriers</h3>
    <p class="rsb-card__text">Classic straight-profile modular panels for cost-effective highway, railway and urban noise control.</p>
    <span class="rsb-card__link">Explore flat panel barriers &rarr;</span>
  </div>
</a><a href="curved-top-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__media">
    <div class="rsb-card__img" style="background-image:url('https://trae-api-cn.mchost.guru/api/ide/v1/text-to-image?prompt=curved-arched-top-noise-barrier-highway-profile&image_size=landscape_16_9')"></div>
    <span class="rsb-card__tag">CURVED TOP</span>
  </div>
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title">Curved / Arched Top Noise Barriers</h3>
    <p class="rsb-card__text">Arc-profile cap delivers +3-8 dB additional diffraction attenuation compared to flat-panel equivalents.</p>
    <span class="rsb-card__link">Explore curved-top barriers &rarr;</span>
  </div>
</a><a href="angled-folded-top-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__media">
    <div class="rsb-card__img" style="background-image:url('https://trae-api-cn.mchost.guru/api/ide/v1/text-to-image?prompt=angled-folded-l-cap-cantilever-noise-barrier&image_size=landscape_16_9')"></div>
    <span class="rsb-card__tag">ANGLED L-CAP</span>
  </div>
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title">Angled / Folded Top Noise Barriers</h3>
    <p class="rsb-card__text">L-shaped cantilever cap creates an extended acoustic shadow zone — highest effective dB per meter height.</p>
    <span class="rsb-card__link">Explore angled-top barriers &rarr;</span>
  </div>
</a><a href="semi-enclosed-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__media">
    <div class="rsb-card__img" style="background-image:url('https://trae-api-cn.mchost.guru/api/ide/v1/text-to-image?prompt=semi-enclosed-u-shaped-noise-barrier-half-tunnel&image_size=landscape_16_9')"></div>
    <span class="rsb-card__tag">SEMI-ENCLOSED</span>
  </div>
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title">Semi-Enclosed Noise Barriers</h3>
    <p class="rsb-card__text">U-shaped / half-tunnel acoustic corridor — 35-50 dB insertion loss with integrated transparent windows.</p>
    <span class="rsb-card__link">Explore semi-enclosed barriers &rarr;</span>
  </div>
</a><a href="fully-enclosed-noise-barriers.html" class="rsb-card" style="text-decoration:none">
  <div class="rsb-card__media">
    <div class="rsb-card__img" style="background-image:url('https://trae-api-cn.mchost.guru/api/ide/v1/text-to-image?prompt=fully-enclosed-noise-barrier-tunnel-360-acoustic&image_size=landscape_16_9')"></div>
    <span class="rsb-card__tag">FULLY-ENCLOSED</span>
  </div>
  <div class="rsb-card__body">
    <span class="rsb-card__meta">By Form / Shape</span>
    <h3 class="rsb-card__title">Fully-Enclosed Noise Barriers</h3>
    <p class="rsb-card__text">360° acoustic tunnel enclosures delivering 45-60 dB insertion loss for HSR and sensitive receiver zones.</p>
    <span class="rsb-card__link">Explore fully-enclosed barriers &rarr;</span>
  </div>
</a>'''

if old_index_card in c:
    c = c.replace(old_index_card, new_index_cards)
    with open(f"{HTML_DIR}/index.html", "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated index.html")
else:
    print("WARNING: index.html card text not found exactly")


# ------ FAQS.HTML ------
with open(f"{HTML_DIR}/faqs.html", "r", encoding="utf-8") as f:
    c = f.read()

old_faqs = '''<div>
      <h3 style="font-size:20px;margin-bottom:14px;color:var(--text-primary)">By Top Profile</h3>
      <div class="rsb-chips" style="justify-content:center;flex-wrap:wrap;gap:10px">
        <a href="flat-top-noise-barriers.html" class="rsb-chip" style="text-decoration:none">Flat-Top Noise Barriers</a><a href="curved-top-noise-barriers.html" class="rsb-chip" style="text-decoration:none">Curved-Top Noise Barriers</a><a href="angled-folded-top-noise-barriers.html" class="rsb-chip" style="text-decoration:none">Angled &amp; Folded-Top Noise Barriers</a>
      </div>
    </div>'''

new_faqs = '''<div>
      <h3 style="font-size:20px;margin-bottom:14px;color:var(--text-primary)">By Barrier Form / Shape</h3>
      <div class="rsb-chips" style="justify-content:center;flex-wrap:wrap;gap:10px">
        <a href="flat-top-noise-barriers.html" class="rsb-chip" style="text-decoration:none">Flat Panel Noise Barriers</a><a href="curved-top-noise-barriers.html" class="rsb-chip" style="text-decoration:none">Curved / Arched Top Noise Barriers</a><a href="angled-folded-top-noise-barriers.html" class="rsb-chip" style="text-decoration:none">Angled / Folded Top Noise Barriers</a><a href="semi-enclosed-noise-barriers.html" class="rsb-chip" style="text-decoration:none">Semi-Enclosed Noise Barriers</a><a href="fully-enclosed-noise-barriers.html" class="rsb-chip" style="text-decoration:none">Fully-Enclosed Noise Barriers</a>
      </div>
    </div>'''

if old_faqs in c:
    c = c.replace(old_faqs, new_faqs)
    with open(f"{HTML_DIR}/faqs.html", "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated faqs.html")
else:
    print("WARNING: faqs.html block not found")
