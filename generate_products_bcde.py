#!/usr/bin/env python3
"""Yukings B/C/D/E product page generator (products 09-20).

Reuses /workspace/public/yukings-noise-barrier.css and the shared JS.
Extends the pattern established in /workspace/generate_products.py
but adds Group B (Industrial), C (Rail/Transit), D (Residential/Municipal),
and E (Custom + Accessories with non-standard layouts).
"""
import sys
from pathlib import Path
from urllib.parse import quote

OUT = Path("/workspace")
DOMAIN = "https://yukings.net"
PUBLIC_CSS = "public/yukings-noise-barrier.css"
PUBLIC_JS = "public/yukings-noise-barrier.js"
IMG_API = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
PRODUCTS_ROOT = f"{DOMAIN}/products"

sys.path.insert(0, str(OUT))
# Reuse shared helpers (img, SLUGS, renderers, build_page) from existing generator
import generate_products as g
img = g.img
SLUGS = dict(g.SLUGS)
SECTIONS = list(g.SECTIONS)
RENDERERS = dict(g.RENDERERS)
build_page = g.build_page

# Extend slugs for 9-20
SLUGS.update({
    9: "factory-noise-barriers", 10: "power-plant-noise-barriers", 11: "chemical-plant-noise-barriers",
    12: "construction-site-noise-barriers",
    13: "high-speed-rail-noise-barriers", 14: "metro-viaduct-noise-barriers",
    15: "railway-station-noise-barriers",
    16: "residential-noise-barriers", 17: "school-noise-barriers", 18: "hospital-noise-barriers",
    19: "custom-noise-barrier-system", 20: "noise-barrier-accessories",
})
# Also patch the imported module's SLUGS dict so renderers that look up
# SLUGS[num] inside generate_products.py (e.g. _render_related) can find
# products 9-20.
g.SLUGS.update({
    9: "factory-noise-barriers", 10: "power-plant-noise-barriers", 11: "chemical-plant-noise-barriers",
    12: "construction-site-noise-barriers",
    13: "high-speed-rail-noise-barriers", 14: "metro-viaduct-noise-barriers",
    15: "railway-station-noise-barriers",
    16: "residential-noise-barriers", 17: "school-noise-barriers", 18: "hospital-noise-barriers",
    19: "custom-noise-barrier-system", 20: "noise-barrier-accessories",
})


# ---------------------------------------------------------------------------
# E-group spec renderers
# ---------------------------------------------------------------------------
def _render_custom_options(p):
    rows = "\n".join(
        f"""        <div class="rsb-custom-option">
          <div class="rsb-custom-option__icon">⚙️</div>
          <h3 class="rsb-custom-option__title">{title}</h3>
          <p class="rsb-custom-option__text">{text}</p>
        </div>"""
        for title, text in p["custom_options"]
    )
    return f"""
  <section class="rsb-section" id="specifications">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Configuration Options</span>
        <h2 class="rsb-section__title">{p['name']}: Choose Your Configuration</h2>
        <div class="rsb-divider"></div>
        <p style="color: #4a5568; font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">Yukings Custom Modular Noise Barrier Systems offer unlimited configuration combinations. Mix and match any material, shape, color, and finish to match your project requirements.</p>
      </div>
      <div style="margin: 0 0 40px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(8,36,87,0.10);">
        <img src="{p['spec_image']}" alt="Custom noise barrier configuration design drawing" loading="lazy" style="width: 100%; height: auto; display: block;">
      </div>
      <div class="rsb-custom-options">
{rows}
      </div>
    </div>
  </section>"""


def _render_accessories(p):
    cats = "\n".join(
        f"""        <div class="rsb-accessory-category">
          <div class="rsb-accessory-category__icon">{icon}</div>
          <h3 class="rsb-accessory-category__title">{title}</h3>
          <p class="rsb-accessory-category__text">{text}</p>
        </div>"""
        for icon, title, text in p["accessory_categories"]
    )
    return f"""
  <section class="rsb-section" id="specifications">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Compatible Accessories</span>
        <h2 class="rsb-section__title">{p['name']}: Universal Fit Accessories Catalog</h2>
        <div class="rsb-divider"></div>
        <p style="color: #4a5568; font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">Original Yukings-manufactured accessories for noise barrier systems. Universal fit across our full product range, including posts, bolts, gaskets, brackets, drainage, and acoustic infill. Same quality, same warranty.</p>
      </div>
      <div style="margin: 0 0 40px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(8,36,87,0.10);">
        <img src="{p['spec_image']}" alt="Noise barrier accessories catalog layout" loading="lazy" style="width: 100%; height: auto; display: block;">
      </div>
      <div class="rsb-accessory-categories">
{cats}
      </div>
      <div style="text-align: center; margin-top: 40px;">
        <a href="{DOMAIN}/accessories" class="rsb-btn rsb-btn--primary">Download Full Catalog (PDF) →</a>
      </div>
    </div>
  </section>"""


# Inject new renderers
RENDERERS["_render_custom_options"] = _render_custom_options
RENDERERS["_render_accessories"] = _render_accessories


# ---------------------------------------------------------------------------
# Override build_page to support spec_mode
# ---------------------------------------------------------------------------
ORIGINAL_BUILD = g.build_page


def build_page(num: int, p: dict) -> str:
    # For E-group products, swap specs section
    if p.get("spec_mode") == "custom_options":
        custom = _render_custom_options(p)
        # Build the page manually with the custom section in place of specs
        return _manual_build(num, p, custom)
    if p.get("spec_mode") == "accessories":
        custom = _render_accessories(p)
        return _manual_build(num, p, custom)
    return ORIGINAL_BUILD(num, p)


def _manual_build(num: int, p: dict, specs_html: str) -> str:
    url = f"{PRODUCTS_ROOT}/{p['slug']}/product-{num:02d}"
    breadcrumb_label = p["category"]
    page_url = url

    # Use original SECTIONS but replace _render_specs
    class _SpecProxy:
        def __getattr__(self, name):
            if name == "_render_specs":
                return lambda _: specs_html
            return getattr(g, name)
    proxy = _SpecProxy()
    # Just call the original logic but with replaced section list
    # Simpler approach: regenerate manually
    sections = []
    for mode, gen_name in SECTIONS:
        if gen_name == "_render_specs":
            sections.append(specs_html)
        else:
            sections.append(RENDERERS[gen_name](p))
    sections_html = "\n".join(sections)

    # JSON-LD blocks
    product_schema = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "{p['name']}",
    "description": "{p['description']}",
    "image": "{p['og_image']}",
    "brand": {{"@type": "Brand", "name": "Yukings"}},
    "manufacturer": {{
      "@type": "Organization",
      "name": "Yukings",
      "address": {{
        "@type": "PostalAddress",
        "addressCountry": "CN",
        "addressRegion": "Guangdong",
        "addressLocality": "Guangzhou"
      }}
    }},
    "category": "{p['category']}",
    "offers": {{"@type": "Offer", "priceCurrency": "USD", "minOrderQuantity": "100", "availability": "https://schema.org/InStock"}}
  }}
  </script>"""

    breadcrumb_schema = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{DOMAIN}"}},
      {{"@type": "ListItem", "position": 2, "name": "Products", "item": "{DOMAIN}/products"}},
      {{"@type": "ListItem", "position": 3, "name": "{breadcrumb_label}", "item": "{DOMAIN}/products/{p['slug']}"}},
      {{"@type": "ListItem", "position": 4, "name": "{p['name']}"}}
    ]
  }}
  </script>"""

    faq_main = ",\n      ".join(
        f"""{{
        "@type": "Question",
        "name": "{q}",
        "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}
      }}"""
        for q, a in p["faqs"]
    )
    faq_schema = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {faq_main}
    ]
  }}
  </script>"""

    item_list = ",\n      ".join(
        f"""{{"@type": "ListItem", "position": {i+1}, "name": "{title}", "url": "{PRODUCTS_ROOT}/{SLUGS[num]}/product-{num:02d}"}}"""
        for i, (num, title, _, _) in enumerate(p["related"])
    )
    itemlist_schema = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "{p['related_title']}",
    "itemListElement": [
      {item_list}
    ]
  }}
  </script>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p['page_title']}</title>
  <meta name="description" content="{p['description']}">
  <meta name="keywords" content="{p['keywords']}">
  <meta name="robots" content="index, follow">
  <meta property="og:title" content="{p['page_title']}">
  <meta property="og:description" content="{p['og_description']}">
  <meta property="og:type" content="product">
  <meta property="og:url" content="{page_url}">
  <link rel="canonical" href="{page_url}">
  <link rel="alternate" hreflang="en" href="{page_url}">
  <link rel="alternate" hreflang="x-default" href="{page_url}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@Yukings">
  <meta name="twitter:title" content="{p['page_title']}">
  <meta name="twitter:description" content="{p['twitter_description']}">
  <meta name="twitter:image" content="{p['og_image']}">
  <link rel="stylesheet" href="{PUBLIC_CSS}">
</head>
<body>
  <header class="rsb-hero">
    <nav class="rsb-breadcrumb rsb-container" aria-label="Breadcrumb">
      <a href="{DOMAIN}/" class="rsb-breadcrumb__item">Home</a>
      <span class="rsb-breadcrumb__separator">/</span>
      <a href="{DOMAIN}/products" class="rsb-breadcrumb__item">Products</a>
      <span class="rsb-breadcrumb__separator">/</span>
      <a href="{DOMAIN}/products/{p['slug']}" class="rsb-breadcrumb__item">{breadcrumb_label}</a>
      <span class="rsb-breadcrumb__separator">/</span>
      <span class="rsb-breadcrumb__current">{p['name']}</span>
    </nav>
    <div class="rsb-container">
      <h1>{p['h1']}</h1>
      <p class="rsb-hero__lead">{p['lead']}</p>
    </div>
  </header>
  <main>
{sections_html}
  </main>
  <div id="rsb-cookie-banner" style="position: fixed; left: 16px; right: 16px; bottom: 16px; max-width: 720px; margin: 0 auto; padding: 20px 24px; background: white; border-radius: 12px; box-shadow: 0 8px 32px rgba(8,36,87,0.20); display: flex; flex-wrap: wrap; gap: 16px; align-items: center; justify-content: space-between; z-index: 9999; font-size: 14px; color: #4a5568;">
    <div style="flex: 1; min-width: 240px;">
      <strong style="color: #082457;">We value your privacy.</strong>
      <p style="margin: 4px 0 0;">This site uses cookies for analytics and to improve your experience. By clicking Accept, you agree to our <a href="{DOMAIN}/privacy" style="color: #082457; font-weight: 600;">Privacy Policy</a>.</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <button onclick="document.getElementById('rsb-cookie-banner').style.display='none'" style="padding: 10px 18px; background: transparent; border: 1px solid #d8dde8; border-radius: 6px; color: #4a5568; font-weight: 600; cursor: pointer;">Reject</button>
      <button onclick="document.getElementById('rsb-cookie-banner').style.display='none'" style="padding: 10px 18px; background: #082457; color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer;">Accept</button>
    </div>
  </div>
{product_schema}
{breadcrumb_schema}
{faq_schema}
{itemlist_schema}
  <script src="{PUBLIC_JS}"></script>
</body>
</html>
"""


# ===========================================================================
# PRODUCTS 09-20  (defined concisely)
# ===========================================================================
CERT_IMG = img("Professional certificate wall display showing three official certificates arranged side by side in elegant dark wood frames mounted on a neutral white wall, museum quality photography, sharp focus")
TEAM_PHOTO = img("Professional engineering support team of three engineers in a modern bright office, wearing business casual attire, friendly smiles, sitting at a conference table with engineering drawings and laptops, photorealistic corporate photography, warm lighting")


def _common_dict(slug, name, short, category, page_title, desc, kw, og_desc, tw_desc, lead, h1, h2_why, h2_lead, pains, values, specs, apps, spec_image, apps_image, dim_prompts, dim_alts, details, install_lead, install_steps, certs, projects, customs, faqs, team_title, team_text, related_title, related_lead, related, pain_image, adv_image, custom_image):
    return {
        "slug": slug, "name": name, "page_title": page_title, "short_name": short,
        "category": category, "description": desc, "og_description": og_desc,
        "twitter_description": tw_desc, "keywords": kw, "lead": lead, "h1": h1,
        "h2_why": h2_why, "h2_lead": h2_lead, "pain_points": pains,
        "pain_image": pain_image, "adv_image": adv_image, "values": values, "specs": specs,
        "apps": apps, "spec_image": spec_image, "apps_image": apps_image,
        "details_image_prompts": dim_prompts, "details_image_alts": dim_alts,
        "details": details, "install_lead": install_lead, "install_steps": install_steps,
        "certs": certs, "projects": projects, "customs": customs, "faqs": faqs,
        "team_title": team_title, "team_text": team_text,
        "related_title": related_title, "related_lead": related_lead, "related": related,
        "cert_image": CERT_IMG,
        "custom_image": custom_image,
        "og_image": f"https://yukings.net/img/og-{slug}.webp",
    }


# ----------- Group B: Industrial / Plant (9-12) -----------
PRODUCTS = {
    9: _common_dict(
        "factory-noise-barriers", "Factory Plant Noise Barrier", "Factory Plant Barrier",
        "Factory Plant Noise Barriers",
        "Factory Plant Noise Barrier | Yukings",
        "Heavy-duty factory plant noise barrier with 28-38dB reduction. Anti-vibration, anti-corrosion steel structure. Ideal for factory perimeters, equipment enclosures, and industrial parks.",
        "factory noise barrier, plant noise barrier, industrial sound wall, equipment noise enclosure, anti-vibration barrier",
        "Factory plant noise barrier. 28-38dB reduction. Anti-vibration steel structure. Equipment enclosure ready.",
        "Heavy-duty factory plant noise barrier with 28-38dB reduction. Anti-vibration, anti-corrosion steel structure. Ideal for factory perimeters and industrial parks.",
        "Heavy-duty factory plant noise barrier with 28-38dB reduction, anti-vibration steel structure, and acid-alkali resistant coating. Engineered for factory perimeters, equipment enclosures, and industrial park boundaries.",
        "Factory Plant Noise Barrier", "Why Heavy-Duty Factory Plant Noise Barriers Are Critical",
        "Yukings Factory Plant Noise Barriers deliver 28-38dB reduction with anti-vibration steel structure, protecting workers and surrounding communities from industrial noise.",
        [("🏭", "Industrial Noise Complaints", "Factories above 75dB trigger community noise complaints and regulatory action, halting production."),
         ("🌀", "Equipment Vibration Transfer", "Compressors and generators transmit structural vibration through standard barriers, reducing 30% noise reduction effectiveness."),
         ("🛢️", "Chemical Atmosphere Corrosion", "Plant atmospheres contain acid/alkali mist that degrades standard panels in 5-7 years, far below service life targets."),
         ("🔥", "Heat-Generating Equipment Proximity", "Generators and boilers create 60-80°C ambient zones, warping standard acoustic panels within months.")],
        [("28-38", "dB Reduction", "Heavy Attenuation"), ("Q355B", "Steel Frame", "Heavy Gauge"), ("+80", "°C Rated", "Heat Resistant"), ("25+", "Years", "Service Life"), ("Anti", "Vibration", "Isolator Mounts")],
        [("Frame Material", "Q355B Hot-Dip Galvanized Steel", "-"), ("Panel Material", "Perforated Steel + 100mm Rock Wool", "-"),
         ("Panel Thickness", "100 / 120 / 150", "mm"), ("Panel Height", "2000 - 6000", "mm"),
         ("Rock Wool Density", "100 - 128 (acoustic core)", "kg/m³"), ("Surface Treatment", "Hot-Dip Galvanized + Epoxy Powder Coating", "-"),
         ("Anti-Vibration Mount", "EPDM isolator, 95% vibration damping", "-"), ("Acid/Alkali Resistance", "pH 2-12 coating, salt-spray 5000h+", "-"),
         ("Post Style", "H-Beam 200x200 / I-Beam 250x250", "-"), ("Fire Rating", "Class A (EN 13501-1)", "-"),
         ("Noise Reduction", "28 - 38", "dB"), ("Wind Resistance", "Grade 9 (1200 Pa)", "-"),
         ("Temperature Range", "-40 to +80", "°C"), ("Service Life", "25 - 30", "Years")],
        [("🏭", "Factory Perimeter", "Industrial park boundary walls", "#e6f0fa"),
         ("⚙️", "Equipment Enclosure", "Compressors, generators, chillers", "#f0faeb"),
         ("🛢️", "Refinery Boundary", "Oil & gas facility perimeter walls", "#fff3e6"),
         ("❄️", "Cooling Tower", "HVAC and cooling tower enclosures", "#fae6f0")],
        img("Technical engineering cross-section blueprint of a factory plant noise barrier showing Q355B steel frame, rock wool core, anti-vibration mount, dimension lines, clean white background, professional CAD style technical illustration"),
        img("Photorealistic panoramic composite of factory plant noise barriers installed at factory perimeter, equipment enclosure, refinery boundary, and cooling tower, daylight industrial photography"),
        ["Photorealistic close-up cross-section of a factory plant noise barrier showing Q355B steel frame, 100mm rock wool core, perforated steel face, anti-vibration EPDM mount, technical industrial photography, clean background, high detail",
         "Photorealistic close-up of a reinforced anti-vibration isolator mount connecting steel post to concrete foundation, industrial product photography, clean white background, high detail",
         "Photorealistic close-up of a heavy-gauge steel post and frame node with epoxy powder coating, industrial product photography, clean background, high detail"],
        ["Factory plant barrier cross-section with rock wool", "Anti-vibration isolator mount detail", "Heavy-gauge steel frame and node"],
        [("🏭", "Q355B Heavy-Gauge Steel Structure", "Q355B high-strength steel frame (1.5-3.0mm thickness) with welded reinforcement provides 2x the load capacity of standard barriers, ideal for tall factory perimeter walls and equipment enclosures."),
         ("🌀", "Anti-Vibration EPDM Isolator Mounts", "EPDM vibration isolators between posts and panels damp 95% of structure-borne vibration, preventing equipment noise from being amplified through the barrier wall."),
         ("🛢️", "Acid/Alkali Resistant Epoxy Coating", "Epoxy powder coating over hot-dip galvanizing provides pH 2-12 chemical resistance and 5000+ hours salt-spray rating for refinery and chemical plant environments."),
         ("🔥", "+80°C Heat-Resistant Design", "Mineral wool core and ceramic-filled coating withstand continuous +80°C ambient temperatures from generators, boilers, and hot process equipment without degradation.")],
        "Engineered for industrial environments. Crane-assisted panel lift, welded reinforcement, and isolator-mount posts ensure long-term vibration-free performance.",
        [("Factory plant barrier foundation", "Foundation Work", "Pour reinforced concrete foundations with anchor bolt set at 2m intervals. Isolator-mount plate pre-installed.", "Photorealistic construction site showing reinforced concrete foundations with anchor bolt plates being poured for a factory plant noise barrier, workers in safety helmets, daylight documentary photography"),
         ("Post installation with isolators", "Post Installation", "Mount H-beam posts on isolator plates. Bolt to anchor plates with EPDM vibration dampers.", "Photorealistic construction workers installing H-beam posts on isolator plates with EPDM vibration dampers for a factory plant noise barrier, daylight industrial documentary photography"),
         ("Reinforcement and panel mounting", "Reinforcement & Panel Mounting", "Weld reinforcement gussets, then mount acoustic panels with security fasteners. Verify panel alignment.", "Photorealistic construction workers welding reinforcement gussets and mounting acoustic panels on a factory plant noise barrier, daylight industrial documentary photography"),
         ("Inspection and testing", "Inspection & Testing", "Perform vibration and acoustic testing. Final inspection verifies isolator damping and acoustic seals.", "Photorealistic engineer performing vibration and acoustic testing on a completed factory plant noise barrier installation, daylight industrial documentary photography")],
        [("🇪🇺", "EN 14388", "CE", "European Conformity Certified for road traffic noise reducing devices.", "EU Mandatory Standard"),
         ("🏆", "ISO 9001:2015", "ISO 9001", "Quality Management System ensuring consistent product excellence.", "Since 2008"),
         ("🛢️", "ISO 12944", "C5-M", "ISO 12944 C5-M corrosion category for marine and industrial atmospheres.", "Industrial Certified"),
         ("🔬", "CMA / CNAS", "CMA/CNAS", "Third-party tested for acoustic, vibration, and structural performance.", "Lab Verified")],
        [("Factory perimeter noise barrier project", "Factory Perimeter", "Foxconn Zhengzhou Plant", "Henan, China", "4.5km heavy-duty factory perimeter noise barrier. 35dB reduction, anti-vibration mounts, 25+ year design life.", img("Photorealistic heavy-duty factory plant noise barrier along a large electronics manufacturing plant perimeter, modern industrial architecture, daylight architectural photography")),
         ("Equipment enclosure noise barrier project", "Equipment Enclosure", "BASF Ludwigshafen Plant", "Germany", "1.8km noise barrier enclosing 12 compressor stations. 38dB reduction at receiver, acid-alkali resistant coating.", img("Photorealistic factory plant noise barrier enclosing industrial compressor equipment, chemical plant background, daylight industrial photography"))],
        [("🎨", "Custom Heights to 8m", "Extra-tall panels up to 8m for tall equipment enclosures. Reinforced steel post options."),
         ("📐", "Integrated Access Doors", "Custom access doors, ventilation louvers, and cable penetrations integrated into barrier structure."),
         ("⚙️", "Engineering Support for Industrial Sites", "Vibration analysis, structural engineering, CAD drawings, and on-site installation guidance for industrial projects.")],
        [("What is a factory plant noise barrier?", "A factory plant noise barrier is a heavy-duty industrial acoustic wall designed for factory perimeters and equipment enclosures. Yukings factory plant barriers deliver 28-38dB reduction with anti-vibration steel structure and chemical-resistant coating."),
         ("How much noise do factory plant barriers reduce?", "Yukings factory plant barriers achieve 28-38dB reduction, sufficient to bring 95-110dB industrial noise down to 57-72dB at the property line, meeting most regulatory limits."),
         ("Are factory plant barriers vibration-resistant?", "Yes! Yukings factory plant barriers use EPDM isolator mounts that damp 95% of structure-borne vibration from compressors, generators, and heavy machinery, preserving acoustic performance."),
         ("What is the minimum order quantity for factory plant barriers?", "Yukings standard MOQ is 100㎡ for factory plant noise barriers. Custom heights or integrated doors may require 200㎡ minimum order quantity."),
         ("Can factory plant barriers withstand chemical atmospheres?", "Yes! Yukings epoxy powder coating over hot-dip galvanizing provides pH 2-12 chemical resistance and 5000+ hours salt-spray rating per ISO 12944 C5-M for industrial and marine atmospheres."),
         ("How tall can factory plant barriers be?", "Standard Yukings factory plant barriers reach 6m. Custom designs with reinforced Q355B steel posts can reach 8m+ for tall equipment enclosures and process structures.")],
        "24/7 Engineering Support for Industrial Plant Projects",
        "Our industrial, structural, and acoustic engineers respond within 24 hours with vibration analysis, structural calculation, CAD drawings, and on-site installation guidance for your factory plant noise barrier project.",
        "Related Factory Plant Noise Barrier Options",
        "Explore our complete range of related noise barrier systems for industrial and commercial applications, engineered as complementary solutions to the factory plant noise barrier.",
        [(10, "Power Plant Noise Barrier", "Heat-resistant barrier for power generation facilities.", img("Photorealistic power plant noise barrier near a power generation facility with cooling towers in background, daylight industrial photography")),
         (11, "Chemical Plant Noise Barrier", "Acid-alkali resistant barrier for chemical industry.", img("Photorealistic chemical plant noise barrier with acid-alkali resistant coating around chemical storage tanks, daylight industrial photography")),
         (12, "Construction Site Temporary Noise Barrier", "Modular reusable barrier for construction sites.", img("Photorealistic construction site temporary noise barrier with modular portable panels around an active construction site, daylight documentary photography")),
         (1, "Galvanized Steel Highway Noise Barrier", "Standard barrier for highway noise reduction.", img("Close-up product photograph of a galvanized steel highway noise barrier panel with perforated pattern, clean industrial photography"))],
        img("Photorealistic aerial view of a large industrial factory plant with heavy-duty noise barrier walls around the perimeter, factory buildings and chimneys in background, daylight documentary photography"),
        img("Close-up product photograph of a heavy-duty factory plant noise barrier panel with reinforced steel frame and anti-corrosion coating, clean industrial setting, professional industrial photography, sharp focus"),
        img("Photorealistic composite showing customized factory plant noise barriers with extra-tall heights, integrated access doors, and engineering support for industrial sites, professional industrial photography, daylight"),
    ),
}


# ----------- Products 10-20 follow a similar pattern. To keep the script
# size manageable, we generate compact entries for them. They use the same
# structure (pain_points, values, specs, apps, details, install_steps, certs,
# projects, customs, faqs, related). For compactness, we load them from a
# companion JSON file.
import json
DATA_FILE = OUT / "products_bcde_data.json"

# Whitelist of fields whose string values are image-generation prompts
# (long descriptive English text converted to URL by img()).
# All other long strings (description, lead, h2_lead, faq answers, etc.)
# must be left alone.
_IMAGE_PROMPT_FIELDS = {
    "pain_image", "adv_image", "spec_image", "apps_image",
    "custom_image", "cert_image", "og_image",
    "details_image_prompts", "install_steps", "projects", "related",
}


def replace_prompts(obj, field_name=None):
    """Recursively convert image-prompt strings to URLs.

    Only fields listed in _IMAGE_PROMPT_FIELDS are considered.  Within those
    fields:
      - a string of length > 30 that does not start with "http" is treated
        as an image prompt and converted via img();
      - a list is recursed into (each element inherits the field name);
      - a tuple / list of tuples: only the 4th element of an install_steps
        or projects tuple, or the 4th element of a related list, is treated
        as an image prompt.
    """
    if field_name in _IMAGE_PROMPT_FIELDS:
        if isinstance(obj, str) and not obj.startswith("http") and len(obj) > 30:
            return img(obj)
        if isinstance(obj, list):
            if field_name in ("install_steps", "projects"):
                return [replace_prompts_in_tuple(t, last_is_prompt=True) for t in obj]
            if field_name == "related":
                return [replace_prompts_in_tuple(t, last_is_prompt=True) for t in obj]
            return [replace_prompts(x, field_name) for x in obj]
    if isinstance(obj, list):
        # Lists whose first element is a string and length matches typical
        # image-bearing tuple are treated as tuples-with-prompt
        if obj and isinstance(obj[0], (list, tuple)):
            return [replace_prompts(x, field_name) for x in obj]
        return [replace_prompts(x, field_name) for x in obj]
    if isinstance(obj, dict):
        return {k: replace_prompts(v, k) for k, v in obj.items()}
    return obj


def replace_prompts_in_tuple(t, last_is_prompt=True):
    """Recursively process a tuple, converting its last element if it's an
    image prompt string."""
    if not isinstance(t, (list, tuple)):
        return replace_prompts(t)
    items = list(t)
    if last_is_prompt and items and isinstance(items[-1], str) \
            and not items[-1].startswith("http") and len(items[-1]) > 30:
        items[-1] = img(items[-1])
    return tuple(replace_prompts(x) for x in items)


if DATA_FILE.exists():
    with open(DATA_FILE) as f:
        extra = json.load(f)
    for num, data in extra.items():
        num = int(num)
        # Backfill fields that JSON omits but renderers require
        if "cert_image" not in data:
            data["cert_image"] = CERT_IMG
        if "og_image" not in data:
            data["og_image"] = f"https://yukings.net/img/og-{data.get('slug', 'product')}.webp"
        PRODUCTS[num] = replace_prompts(data)
else:
    print(f"WARNING: {DATA_FILE} not found. Only product 09 will be generated.")


def main():
    for num, p in PRODUCTS.items():
        html = build_page(num, p)
        path = OUT / f"product-{num:02d}.html"
        path.write_text(html, encoding="utf-8")
        print(f"Wrote {path}  ({len(html.splitlines())} lines, {len(html)} bytes)")


if __name__ == "__main__":
    main()
