#!/usr/bin/env python3
"""Create semi-enclosed and fully-enclosed noise barrier pages."""

HTML_DIR = "/workspace/html"

# Read flat-top to get CSS, header, nav, footer
with open(f"{HTML_DIR}/flat-top-noise-barriers.html", "r", encoding="utf-8") as f:
    flat = f.read()

# Extract CSS block (from <style> to </style>)
css_start = flat.index("<style>")
css_end = flat.index("</style>", css_start) + len("</style>")
CSS_BLOCK = flat[css_start:css_end]

# Extract topbar + header + nav dropdowns (starts after </script> for JSON-LD Product)
# Find the start of body section: <div class="rsb-topbar">
topbar_start = flat.index('<div class="rsb-topbar">')
# Find end of header (after </header>)
header_end = flat.index("</header>", topbar_start) + len("</header>")
HEADER_NAV = flat[topbar_start:header_end]

# Extract footer
footer_start = flat.index('<footer class="rsb-footer">')
footer_end = flat.index("</footer>", footer_start) + len("</footer>")
FOOTER = flat[footer_start:footer_end]

# Extract cookie notice
cookie_start = flat.index('<div class="rsb-cookie"')
cookie_end = flat.index("</div>", cookie_start) + len("</div>")
# need to get the right </div> - cookie has just one close tag
COOKIE = flat[cookie_start:cookie_end]

# Common JSON-LD org
ORG_JSONLD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"Shenzhen Yukings Industrial Co., Ltd.","alternateName":"Yukings","url":"https://www.yukings.net","logo":"https://www.yukings.net/img/yukings-logo.svg","image":"https://www.yukings.net/img/yukings-factory.webp","description":"Noise barrier manufacturer based in Shenzhen, China. 18+ years OEM experience, 42,000 m² factory, ISO 9001/14001/45001 and CE certified.","foundingDate":"2006","foundingLocation":"Shenzhen, Guangdong, China","hasOfferCatalog":{"@type":"OfferCatalog","name":"Yukings Noise Barrier Catalog","itemListElement":["Railway Noise Barriers","Highway Noise Barriers","Industrial Noise Barriers","Residential Noise Barriers","Solar Noise Barriers"]},"slogan":"Engineered Acoustic Barriers for a Quieter World","telephone":"+86-755-86366707","email":"weilai04525@163.com","address":{"@type":"PostalAddress","streetAddress":"Room 1405, Building B2, Yunzhi Tech Park, Guangming District","addressLocality":"Shenzhen","addressRegion":"Guangdong","postalCode":"518106","addressCountry":"CN"},"geo":{"@type":"GeoCoordinates","latitude":22.7673,"longitude":113.9696},"sameAs":["https://www.linkedin.com/company/yukings","https://www.facebook.com/yukings","https://www.youtube.com/@yukings"],"contactPoint":[{"@type":"ContactPoint","telephone":"+86-755-86366707","contactType":"customer service","availableLanguage":["English","Chinese"]}]}
</script>'''


def build_page(slug, title, description, keywords, og_title, og_desc, image_prompt,
               product_name, product_sku, product_desc,
               hero_h1, hero_lede, hero_chips, hero_stats,
               split_body, split_apps,
               spec_rows,
               features,
               related_cards,
               faqs,
               price_range):
    """Build a complete page."""
    canonical = f"https://www.yukings.net/{slug}.html"
    og_image = f"https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={image_prompt}&image_size=landscape_16_9"

    breadcrumb_jsonld = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://www.yukings.net/index.html"}},{{"@type":"ListItem","position":2,"name":"Products","item":"https://www.yukings.net/products.html"}},{{"@type":"ListItem","position":3,"name":"{title.replace(" | Yukings", "")}","item":"{canonical}"}}]}}
</script>'''

    product_jsonld = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Product","name":"{product_name}","description":"{product_desc}","brand":{{"@type":"Organization","name":"Yukings"}},"manufacturer":{{"@type":"Organization","name":"Shenzhen Yukings Industrial Co., Ltd."}},"sku":"{product_sku}","productID":"{product_sku}","image":"{og_image}","url":"{canonical}","material":"DX51D+Z galvanized steel perforated absorptive panels, polycarbonate transparent windows, steel H-beam columns","offers":{{"@type":"AggregateOffer","priceCurrency":"USD","priceRange":"{price_range}","availability":"https://schema.org/InStock","seller":{{"@type":"Organization","name":"Yukings","url":"https://www.yukings.net"}}}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.8","ratingCount":"128","bestRating":"5","worstRating":"1"}},"warranty":{{"@type":"WarrantyPromise","durationOfWarranty":{{"@type":"QuantitativeValue","value":15,"unitText":"years"}},"warrantyScope":{{"@type":"WarrantyScope","name":"15-year structural warranty"}}}},"isRelatedTo":[{{"@type":"Product","name":"Galvanized Steel Noise Barriers","url":"https://www.yukings.net/galvanized-steel-noise-barriers.html"}},{{"@type":"Product","name":"Angled / Folded Top Noise Barriers","url":"https://www.yukings.net/angled-folded-top-noise-barriers.html"}},{{"@type":"Product","name":"All Noise Barrier Products","url":"https://www.yukings.net/products.html"}}],"inLanguage":"en"}}
</script>'''

    # Build hero chips HTML
    hero_chips_html = "".join(f'<span class="rsb-hero__chip">{c}</span>' for c in hero_chips)

    # Build hero stats
    hero_stats_html = "".join(
        f'<div class="rsb-hero__stat"><strong>{s[0]}</strong><span>{s[1]}</span></div>'
        for s in hero_stats
    )

    # Build spec rows
    spec_html = "\n".join(
        f'            <tr><td>{r[0]}</td><td>{r[1]}</td></tr>'
        for r in spec_rows
    )

    # Build features
    features_html = "\n".join(
        f'      <div class="rsb-feature"><i class="rsb-feature__icon">F{idx+1}</i><h3>{f[0]}</h3><p>{f[1]}</p></div>'
        for idx, f in enumerate(features)
    )

    # Build related cards
    related_html = "\n".join(
        f'      <div class="rsb-card"><div class="rsb-card__media"><div class="rsb-card__img" style="background-image:url(\'{c[2]}\')"></div><span class="rsb-card__tag">{c[3]}</span></div><div class="rsb-card__body"><span class="rsb-card__meta">{c[4]}</span><h3 class="rsb-card__title">{c[0]}</h3><p class="rsb-card__text">{c[5]}</p><a class="rsb-card__link" href="{c[1]}">View Product &rarr;</a></div></div>'
        for c in related_cards
    )

    # Build FAQs
    faq_html = "\n".join(
        f'      <div class="rsb-faq__item"><div class="rsb-faq__q">{q}</div><div class="rsb-faq__a">{a}</div></div>'
        for q, a in faqs
    )

    # Page title for headings/forms
    short_title = title.replace(" | Yukings", "")

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Shenzhen Yukings Industrial Co., Ltd.">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Yukings - Noise Barrier Manufacturer">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="{og_image}">
{CSS_BLOCK}
{ORG_JSONLD}
{breadcrumb_jsonld}
{product_jsonld}
</head>
<body>
{HEADER_NAV}
<nav class="rsb-breadcrumb" aria-label="Breadcrumb">
  <div class="rsb-container">
    <ol class="rsb-breadcrumb__list"><li><a href="index.html">Home</a></li><li class="rsb-breadcrumb__sep">/</li><li><a href="products.html">Products</a></li><li class="rsb-breadcrumb__sep">/</li><li><span class="rsb-breadcrumb__current">{short_title}</span></li></ol>
  </div>
</nav>
<section class="rsb-hero" aria-labelledby="hero-title">
  <div class="rsb-hero__bg" style="background-image:url('{og_image}')"></div>
  <div class="rsb-container">
    <div class="rsb-hero__content">
      <span class="rsb-hero__eyebrow">Yukings  · Noise Barrier Manufacturer Since 2006</span>
      <h1 id="hero-title">{hero_h1}</h1>
      <p class="lede">{hero_lede}</p>
      <div class="rsb-hero__actions"><a href="get-quote.html" class="rsb-btn rsb-btn--primary rsb-btn--lg">Request a Free Quote</a><a href="products.html" class="rsb-btn rsb-btn--ghost rsb-btn--lg">Browse Our Products</a></div>
      <div class="rsb-hero__quick">{hero_chips_html}</div>
      <div class="rsb-hero__stats">{hero_stats_html}</div>
    </div>
  </div>
</section>
<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    <div class="rsb-section__head">
      <span class="rsb-eyebrow">Product Overview</span>
      <h2>{short_title} — Design Concept</h2>
      <div class="rsb-divider rsb-divider--center"></div>
      <p>{split_body}</p>
    </div>
    <div class="rsb-split">
      <div class="rsb-split__media"><div class="rsb-split__img" style="background-image:url('{og_image}')"></div></div>
      <div class="rsb-split__body">
        <span class="rsb-split__eyebrow">What it is</span>
        <h2>Intermediate / complete acoustic corridor around the noise source.</h2>
        <div class="rsb-divider"></div>
        <p>{split_body}</p>
        <ul class="rsb-split__list">{"".join(f"<li>{app}</li>" for app in split_apps)}</ul>
        <div class="rsb-split__actions"><a href="get-quote.html" class="rsb-btn rsb-btn--primary">Request a Quote</a><a href="products.html" class="rsb-btn rsb-btn--ghost-alt">Download Datasheet</a></div>
      </div>
    </div>
  </div>
</section>
<section class="rsb-section">
  <div class="rsb-container">
    <div class="rsb-section__head">
      <span class="rsb-eyebrow">Technical Specification</span>
      <h2>{short_title} — Full Specification</h2>
      <div class="rsb-divider rsb-divider--center"></div>
      <p>Detailed engineering specification for Yukings {short_title.lower()}. All parameters align with EN 1793 / EN 1794 / EN 1991-1-4 testing and design standards.</p>
    </div>
    <div class="rsb-tablewrap">
      <div class="rsb-table-head"><h3>{short_title} — Product Specification</h3><p>Engineering specification for project-specific acoustic corridor design.</p></div>
      <div class="rsb-table-body">
        <table class="rsb-table">
          <thead><tr><th>Property</th><th>Value</th></tr></thead>
          <tbody>
{spec_html}
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>
<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    <div class="rsb-section__head">
      <span class="rsb-eyebrow">Why Yukings</span>
      <h2>What makes our {short_title} different</h2>
      <div class="rsb-divider rsb-divider--center"></div>
      <p>Project-tested acoustic design, structural engineering, modular panel manufacturing and full EN / CE test documentation make Yukings enclosed-noise-barrier solutions reliable for the most demanding projects.</p>
    </div>
    <div class="rsb-features">
{features_html}
    </div>
  </div>
</section>
<section class="rsb-section">
  <div class="rsb-container">
    <div class="rsb-section__head">
      <span class="rsb-eyebrow">Related Products &amp; Use Cases</span>
      <h2>Other noise barrier forms and solutions</h2>
      <div class="rsb-divider rsb-divider--center"></div>
      <p>Compare enclosed noise barriers with Yukings flat panel, curved-top and angled folded-top forms, or explore our application-specific noise wall product lines.</p>
    </div>
    <div class="rsb-grid rsb-grid--3">
{related_html}
    </div>
  </div>
</section>
<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    <div class="rsb-section__head">
      <span class="rsb-eyebrow">Frequently Asked</span>
      <h2>{short_title} — FAQs</h2>
      <div class="rsb-divider rsb-divider--center"></div>
      <p>Commonly asked technical, commercial and logistics questions about Yukings {short_title.lower()}.</p>
    </div>
    <div class="rsb-faq">
{faq_html}
    </div>
  </div>
</section>
<section class="rsb-cta">
  <div class="rsb-container">
    <div class="rsb-cta__inner">
      <span class="rsb-eyebrow">Ready to Take the Next Step?</span>
      <h2>Need a {short_title} quotation for your project? Contact Yukings today.</h2>
      <p>Our enclosed-noise-barrier specialists will respond to your project inquiry within 24 hours, including technical guidance, acoustic modeling recommendations and project pricing where applicable.</p>
      <div class="rsb-cta__actions">
        <a href="get-quote.html" class="rsb-btn rsb-btn--primary rsb-btn--lg">Get a Free Project Quote</a>
        <a href="contact.html" class="rsb-btn rsb-btn--ghost rsb-btn--lg">Contact Our Engineers</a>
      </div>
      <div class="rsb-cta__contacts">
        <div class="rsb-cta__contact"><i>&#9742;</i><div><strong>Tel</strong><span>+86-755-86366707</span></div></div>
        <div class="rsb-cta__contact"><i>&#9993;</i><div><strong>Email</strong><span>weilai04525@163.com</span></div></div>
        <div class="rsb-cta__contact"><i>&#9990;</i><div><strong>Miss Tang (Sales)</strong><span>+86 17727812004</span></div></div>
        <div class="rsb-cta__contact"><i>&#9990;</i><div><strong>Mr. Yu (Engineering)</strong><span>+86 13828819804</span></div></div>
      </div>
    </div>
  </div>
</section>
<section class="rsb-section">
  <div class="rsb-container">
    <div class="rsb-section__head">
      <span class="rsb-eyebrow">Project Inquiry</span>
      <h2>Tell us about your {short_title.lower()} project</h2>
      <div class="rsb-divider rsb-divider--center"></div>
      <p>Share your project parameters and a Yukings engineer will prepare a tailored proposal, including panel dimensions, column spacing, barrier height and estimated attenuation performance.</p>
    </div>
    <form class="rsb-form" onsubmit="event.preventDefault();">
      <h3>Project Quote Request — {short_title}</h3>
      <p>Fields marked * are required. We respond within 24 hours Beijing time.</p>
      <div class="rsb-form__grid">
        <div class="rsb-form__field"><label>Company Name *</label><input type="text" placeholder="Your company or organization"></div>
        <div class="rsb-form__field"><label>Country / Region *</label><input type="text" placeholder="Country"></div>
        <div class="rsb-form__field"><label>Contact Person *</label><input type="text" placeholder="Your full name"></div>
        <div class="rsb-form__field"><label>Position</label><input type="text" placeholder="Role or title"></div>
        <div class="rsb-form__field"><label>Email *</label><input type="email" placeholder="name@company.com"></div>
        <div class="rsb-form__field"><label>Phone / WhatsApp</label><input type="tel" placeholder="+Country code number"></div>
        <div class="rsb-form__field"><label>Project Type</label><select><option>Highway / Expressway</option><option>Railway / High-Speed Rail</option><option>Industrial Plant</option><option>Residential / Community</option><option>Bridge / Viaduct</option><option>Other / Mixed</option></select></div>
        <div class="rsb-form__field"><label>Estimated Barrier Length (m)</label><input type="text" placeholder="e.g. 3000"></div>
        <div class="rsb-form__field"><label>Target Barrier Height (m)</label><input type="text" placeholder="e.g. 5.0"></div>
        <div class="rsb-form__field"><label>Panel Depth (mm)</label><select><option>80 mm</option><option>100 mm</option><option>120 mm</option><option>140 mm</option><option>Mixed / To be advised</option></select></div>
        <div class="rsb-form__field"><label>Panel Face Material</label><select><option>Galvanized Steel (DX51D+Z)</option><option>Polycarbonate / Acrylic Clear</option><option>Laminated Glass (fully-enclosed only)</option><option>To be advised</option></select></div>
        <div class="rsb-form__field"><label>Finish</label><select><option>Hot-dip galvanized only</option><option>Galvanized + RAL powder coat</option><option>To be advised</option></select></div>
        <div class="rsb-form__field rsb-form__field--full"><label>Project Notes &amp; Requirements</label><textarea placeholder="Site description, timeline, standards required (EN, CE, ISO), tender reference, etc."></textarea></div>
      </div>
      <button type="submit" class="rsb-btn rsb-btn--primary rsb-btn--lg rsb-form__submit">Submit Project Quote Request</button>
    </form>
  </div>
</section>
{FOOTER}
{COOKIE}
</body>
</html>
"""
    return page


# ============================================================
# SEMI-ENCLOSED PAGE
# ============================================================
semi_page = build_page(
    slug="semi-enclosed-noise-barriers",
    title="Semi-Enclosed Noise Barriers | Yukings",
    description="Semi-enclosed noise barriers — U-shaped / half-tunnel acoustic design for highways, railways and urban roads. 35-50 dB insertion loss with integrated transparent windows. Request a free quote.",
    keywords="semi-enclosed noise barrier, half-enclosed sound barrier, U-shaped acoustic barrier, semi-closed noise wall, partial enclosure noise barrier, Yukings semi-enclosed noise barrier manufacturer",
    og_title="Semi-Enclosed Noise Barriers",
    og_desc="Semi-enclosed noise barriers — U-shaped / half-tunnel acoustic design for highways, railways and urban roads. 35-50 dB insertion loss with integrated transparent windows. Request a free quote.",
    image_prompt="semi-enclosed-u-shaped-noise-barrier-highway-half-tunnel",
    product_name="Semi-Enclosed / U-Shaped Noise Barriers",
    product_sku="YK-SEMI-ENCLOSED",
    product_desc="Semi-enclosed / U-shaped half-tunnel noise barriers. Vertical absorptive wall panels on both sides combined with a partially overhanging top structure creating an enclosed acoustic corridor. Ideal for highways, urban expressways and railway lines near residential zones.",
    hero_h1='Semi-enclosed U-shaped / half-tunnel noise barriers creating an enclosed acoustic corridor for <span>35-50 dB highway and railway noise attenuation</span>.',
    hero_lede="Yukings semi-enclosed noise barriers use a U-shaped or half-tunnel structure: vertical absorptive wall panels on both sides of the road combined with a partially overhanging top structure to create an enclosed acoustic corridor. This design delivers 35-50 dB of insertion loss while maintaining driver visibility through integrated transparent windows. Ideal for highways, urban expressways and railway lines near residential zones.",
    hero_chips=["U-Shaped / Half-Tunnel", "35-50 dB Insertion Loss", "Integrated Transparent Windows", "Dual-Side Absorption", "Residential Zone Friendly"],
    hero_stats=[
        ("35-50 dB", "insertion loss (DL)"),
        ("80-140 mm", "panel depth"),
        ("2.0-2.5 m", "column spacing"),
        ("25 yr", "design life"),
    ],
    split_body="Semi-enclosed noise barriers offer an intermediate solution between standard roadside barriers and full enclosures. The U-shaped configuration traps noise inside the acoustic corridor while maintaining natural light and driver visibility through integrated transparent panels.",
    split_apps=[
        "Highways / Urban Expressways",
        "Railway lines near residential buildings",
        "School and hospital roadside noise control",
        "Residential community boundary noise management",
    ],
    spec_rows=[
        ("Insertion Loss DL (EN 1793-3)", "35 – 50 dB"),
        ("Sound Insulation Rw (EN ISO 717-1)", "42 – 58 dB"),
        ("Form / Shape", "Semi-Enclosed / U-Shape Half-Tunnel"),
        ("Panel Width", "2,500 mm standard"),
        ("Panel Height", "500 mm modules"),
        ("Panel Depth", "80 / 100 / 120 / 140 mm"),
        ("Panel Face", "DX51D+Z galvanized steel perforated absorptive + polycarbonate transparent"),
        ("Top Structure", "Partially overhanging steel canopy or clear PC canopy"),
        ("Column", "Steel H-beam / steel pipe truss"),
        ("Column Spacing", "2.0 – 2.5 m"),
        ("Barrier Height", "4.0 – 6.5 m"),
        ("Design Service Life", "25 years"),
        ("Structural Warranty", "15 years"),
        ("Corrosion Resistance", "ISO 12944 C3-M"),
        ("Fire Rating", "Class A (EN 13501-1)"),
        ("Wind Load Rating", "1.2 – 1.5 kN/m²"),
        ("Finish", "hot-dip galvanized + optional RAL powder coat"),
    ],
    features=[
        ("Dual-Side Absorptive Panels", "Rock-wool filled galvanized steel panels on both sides of the road delivering broadband absorption."),
        ("Integrated Transparent Windows", "UV-stabilized polycarbonate / acrylic clear panels maintaining driver visibility and natural light."),
        ("Partially Overhanging Top Structure", "Steel or clear canopy extending over the road, creating an acoustic shadow zone without the cost of a full enclosure."),
        ("Fast Modular Installation", "Standard modular panels for rapid installation along long corridors."),
        ("Custom RAL Color Matching", "Custom powder coat colors available to blend with surrounding environment."),
        ("Noise Reduction for Residential Zones", "Designed to protect residential communities, schools and hospitals from road and railway noise."),
    ],
    related_cards=[
        ("Flat Panel Noise Barriers", "flat-top-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=flat-panel-straight-noise-barrier-highway&image_size=landscape_16_9",
         "Flat Panel", "Product",
         "Classic straight-profile modular noise wall — the cost-effective baseline for highway and railway noise control."),
        ("Curved / Arched Top Noise Barriers", "curved-top-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=curved-arched-top-noise-barrier-highway-profile&image_size=landscape_16_9",
         "Curved Top", "Product",
         "Engineered arc-profile cap redirects diffracted sound waves over the barrier top, delivering +3-8 dB additional attenuation."),
        ("Angled / Folded Top Noise Barriers", "angled-folded-top-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=angled-folded-l-cap-cantilever-noise-barrier&image_size=landscape_16_9",
         "L-Cap Cantilever", "Product",
         "L-shaped cantilever cap creates an extended acoustic shadow zone, delivering the highest effective insertion loss per meter height."),
        ("Highway / Road Noise Barriers", "highway-road-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=highway-road-noise-barrier-expressway&image_size=landscape_16_9",
         "Highway", "Use Case",
         "Metal-louvered absorption panels with optional polycarbonate or concrete sections for expressway and ring road noise control."),
        ("Residential Community Noise Barriers", "residential-community-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=residential-community-noise-barrier-housing-acoustic-wall&image_size=landscape_16_9",
         "Residential", "Use Case",
         "Visually softer noise barriers for housing developments, schools, hospitals and sensitive residential reception areas."),
        ("Railway Noise Barriers", "railway-noise-barriers-rail.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=railway-noise-barrier-trackside-wall&image_size=landscape_16_9",
         "Railway", "Use Case",
         "Rigid modular panels engineered for high-speed rail aerodynamic loads, vibration and fatigue performance requirements."),
    ],
    faqs=[
        ("How much noise does a semi-enclosed noise barrier reduce?",
         "A properly designed Yukings semi-enclosed noise barrier delivers 35 to 50 dB of insertion loss (DL) measured to EN 1793-3. The U-shaped configuration creates an acoustic corridor that traps and absorbs noise inside the barrier volume, significantly outperforming single-sided flat panel barriers."),
        ("Do semi-enclosed barriers block driver visibility?",
         "No. Yukings semi-enclosed barriers integrate transparent polycarbonate or acrylic panels into the vertical walls, and the top structure typically includes clear polycarbonate canopy sections or leaves an open central lane to preserve driver visibility and natural light."),
        ("What is the typical height of a semi-enclosed barrier?",
         "Barrier heights range from 4.0 m to 6.5 m depending on noise source height, receiver height and required attenuation. The partially overhanging top canopy typically extends 0.8-1.5 m inward from each side."),
        ("Can semi-enclosed barriers be customized?",
         "Yes. Yukings provides full acoustic simulation modeling, CAD design, custom RAL colors, decorative finish panels, integration of transparent sections, green-wall elements and project-specific structural engineering for every semi-enclosed noise barrier installation."),
    ],
    price_range="$85-$168",
)

# ============================================================
# FULLY-ENCLOSED PAGE
# ============================================================
full_page = build_page(
    slug="fully-enclosed-noise-barriers",
    title="Fully-Enclosed Noise Barriers | Yukings",
    description="Fully-enclosed noise barrier tunnels — complete 360° acoustic enclosures for high-speed rail, urban expressways and sensitive receiver zones. 45-60 dB insertion loss. Request a free quote.",
    keywords="fully-enclosed noise barrier, full enclosure sound barrier, 360 degree acoustic tunnel, noise enclosure tunnel, enclosed noise wall, Yukings fully-enclosed noise barrier manufacturer",
    og_title="Fully-Enclosed Noise Barriers",
    og_desc="Fully-enclosed noise barrier tunnels — complete 360° acoustic enclosures for high-speed rail, urban expressways and sensitive receiver zones. 45-60 dB insertion loss. Request a free quote.",
    image_prompt="fully-enclosed-noise-barrier-tunnel-360-acoustic-enclosure-high-speed-rail",
    product_name="Fully-Enclosed / Acoustic Tunnel Noise Barriers",
    product_sku="YK-FULLY-ENCLOSED",
    product_desc="Fully-enclosed noise barrier tunnels creating a complete 360° acoustic enclosure. Vertical absorptive walls + fully overhanging top roof. Highest attenuation performance for high-speed rail, urban expressways and hospital / school sensitive receiver zones.",
    hero_h1='Fully-enclosed 360° acoustic tunnel noise barriers delivering the highest attenuation of <span>45-60 dB</span> for high-speed rail, urban expressways and sensitive receiver zones.',
    hero_lede="Yukings fully-enclosed noise barrier tunnels create a complete 360° acoustic enclosure around the noise source. Vertical absorptive wall panels on both sides are combined with a fully overhanging roof structure to trap and absorb virtually all airborne noise. Delivering 45-60 dB of insertion loss, fully-enclosed barriers are the highest-performance solution for high-speed rail lines, urban expressways passing through dense residential areas, and sensitive receiver zones including schools and hospitals.",
    hero_chips=["360° Full Acoustic Enclosure", "45-60 dB Insertion Loss", "HSR / Urban Expressway Ready", "Transparent Roof + Side Windows", "Highest Attenuation Available"],
    hero_stats=[
        ("45-60 dB", "insertion loss (DL)"),
        ("80-140 mm", "panel depth"),
        ("2.0-3.0 m", "column spacing"),
        ("25 yr", "design life"),
    ],
    split_body="Fully-enclosed noise barriers are the highest-performance acoustic solution, creating a complete acoustic tunnel around the road or railway line. The fully overhanging roof structure combined with absorptive vertical panels delivers unmatched attenuation for the most sensitive receiver environments.",
    split_apps=[
        "High-speed rail lines through urban areas",
        "Urban expressways passing dense residential districts",
        "Highways adjacent to schools, hospitals and research facilities",
        "Mixed traffic corridors with strict environmental noise limits",
    ],
    spec_rows=[
        ("Insertion Loss DL (EN 1793-3)", "45 – 60 dB"),
        ("Sound Insulation Rw (EN ISO 717-1)", "50 – 65 dB"),
        ("Form / Shape", "Fully-Enclosed / 360° Acoustic Tunnel"),
        ("Panel Width", "2,500 mm standard"),
        ("Panel Height", "500 mm modules"),
        ("Panel Depth", "80 / 100 / 120 / 140 mm"),
        ("Panel Face", "DX51D+Z galvanized steel perforated absorptive + polycarbonate transparent"),
        ("Roof Structure", "Fully overhanging steel truss + transparent or absorptive roof panels"),
        ("Column", "Heavy steel H-beam / steel truss"),
        ("Column Spacing", "2.0 – 3.0 m"),
        ("Barrier Height", "5.5 – 8.0 m"),
        ("Design Service Life", "25 years"),
        ("Structural Warranty", "15 years"),
        ("Corrosion Resistance", "ISO 12944 C4-H"),
        ("Fire Rating", "Class A (EN 13501-1)"),
        ("Wind Load Rating", "1.5 – 2.0 kN/m²"),
        ("Finish", "hot-dip galvanized + optional RAL powder coat"),
        ("Transparent Roof", "Polycarbonate / laminated glass"),
    ],
    features=[
        ("Complete 360° Acoustic Enclosure", "Vertical absorptive walls + fully overhanging roof create a complete acoustic tunnel trapping airborne noise."),
        ("45-60 dB Insertion Loss", "Highest attenuation performance available for road and rail noise control projects."),
        ("Transparent Roof & Side Windows", "UV-stabilized polycarbonate / laminated glass roof and side windows for driver visibility and natural light."),
        ("HSR Aerodynamic Design", "Structural design engineered for high-speed rail aerodynamic slipstream loads and pressure waves."),
        ("Project-Specific Acoustic Modeling", "Full acoustic simulation and CAD design for each project site with receiver noise prediction."),
        ("Heavy-Corrosion Protection", "ISO 12944 C4-H level corrosion protection for coastal and industrial environments."),
    ],
    related_cards=[
        ("Angled / Folded Top Noise Barriers", "angled-folded-top-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=angled-folded-l-cap-cantilever-noise-barrier&image_size=landscape_16_9",
         "L-Cap Cantilever", "Product",
         "L-shaped cantilever cap creates an extended acoustic shadow zone, delivering the highest effective insertion loss per meter height."),
        ("Curved / Arched Top Noise Barriers", "curved-top-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=curved-arched-top-noise-barrier-highway-profile&image_size=landscape_16_9",
         "Curved Top", "Product",
         "Engineered arc-profile cap redirects diffracted sound waves over the barrier top, delivering +3-8 dB additional attenuation."),
        ("Highway / Road Noise Barriers", "highway-road-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=highway-road-noise-barrier-expressway&image_size=landscape_16_9",
         "Highway", "Use Case",
         "Metal-louvered absorption panels with optional polycarbonate or concrete sections for expressway and ring road noise control."),
        ("Railway Noise Barriers", "railway-noise-barriers-rail.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=railway-noise-barrier-trackside-wall&image_size=landscape_16_9",
         "Railway", "Use Case",
         "Rigid modular panels engineered for high-speed rail aerodynamic loads, vibration and fatigue performance requirements."),
        ("Industrial Plant Noise Barriers", "industrial-plant-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=industrial-plant-factory-noise-barrier-perimeter&image_size=landscape_16_9",
         "Industrial", "Use Case",
         "Absorptive metal-faced panels with Class A fire rating for power plants, factories, compressor stations and industrial perimeter walls."),
        ("Residential Community Noise Barriers", "residential-community-noise-barriers.html",
         "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=residential-community-noise-barrier-housing-acoustic-wall&image_size=landscape_16_9",
         "Residential", "Use Case",
         "Visually softer noise barriers for housing developments, schools, hospitals and sensitive residential reception areas."),
    ],
    faqs=[
        ("How much noise does a fully-enclosed noise barrier reduce?",
         "A properly designed Yukings fully-enclosed noise barrier delivers 45 to 60 dB of insertion loss (DL) measured to EN 1793-3. The 360° acoustic tunnel configuration traps and absorbs virtually all airborne noise, making it the highest-performance solution available for sensitive receiver environments."),
        ("How does a fully-enclosed barrier differ from a semi-enclosed barrier?",
         "A semi-enclosed barrier has vertical side walls but only a partially overhanging top canopy. A fully-enclosed barrier adds a complete roof structure for 360° coverage. Fully-enclosed barriers deliver 10-15 dB additional attenuation compared to equivalent semi-enclosed designs, but at higher material cost and structural complexity."),
        ("Are fully-enclosed barriers suitable for high-speed rail?",
         "Yes. Yukings fully-enclosed noise barriers are specifically engineered for HSR applications with reinforced structural design to handle high-speed train slipstream aerodynamic loads, pressure wave fatigue and vibration. All components are tested and certified for HSR service conditions."),
        ("How much does a fully-enclosed noise barrier cost?",
         "Fully-enclosed noise barrier projects are project-specific and depend on length, height, structural span requirements, transparent panel ratio, foundation type and finish specifications. Yukings provides free project engineering and quotation — contact our specialists for your site-specific assessment."),
    ],
    price_range="$128-$285",
)

with open(f"{HTML_DIR}/semi-enclosed-noise-barriers.html", "w", encoding="utf-8") as f:
    f.write(semi_page)
print("Created semi-enclosed-noise-barriers.html")

with open(f"{HTML_DIR}/fully-enclosed-noise-barriers.html", "w", encoding="utf-8") as f:
    f.write(full_page)
print("Created fully-enclosed-noise-barriers.html")
