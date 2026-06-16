#!/usr/bin/env python3
"""Yukings static site generator - helpers (part 1)."""
import os

OUT = "/workspace/html"
os.makedirs(OUT, exist_ok=True)

with open(os.path.join(OUT, "_css.txt"), "r", encoding="utf-8") as f:
    SHARED_CSS = f.read()

def topbar():
    return """<div class="rsb-topbar">
  <div class="rsb-container">
    <div class="rsb-topbar__inner">
      <div class="rsb-topbar__links">
        <a href="tel:+8675586366707"><span>&#9742;</span> +86-755-86366707</a>
        <a href="mailto:weilai04525@163.com"><span>&#9993;</span> weilai04525@163.com</a>
        <span><span>&#9881;</span> Mon-Sat 8:30-18:30 (Beijing Time)</span>
      </div>
      <div class="rsb-topbar__links">
        <a href="faqs.html">FAQs</a>
        <a href="get-quote.html">Request a Quote &rarr;</a>
        <span><span>&#127758;</span> EN / Ship to Worldwide</span>
      </div>
    </div>
  </div>
</div>"""

def header(active_file):
    items = [("Home","index.html"),("Products","products.html"),("Solutions","solutions.html"),
             ("Projects","projects.html"),("Blog","blog.html"),("FAQs","faqs.html"),
             ("About Us","about.html"),("Get Quote","get-quote.html"),("Contact Us","contact.html")]
    nav = "".join(f'<a href="{h}" class="rsb-nav__item rsb-nav__item--active" aria-current="page">{n}</a>' if h==active_file
                  else f'<a href="{h}" class="rsb-nav__item">{n}</a>' for n,h in items)
    return f"""<header class="rsb-header">
  <div class="rsb-container">
    <div class="rsb-header__inner">
      <a href="index.html" class="rsb-logo" aria-label="Yukings home">
        <span class="rsb-logo__mark">Y</span>
        <span class="rsb-logo__name">Yukings<small>Noise Barrier Manufacturer</small></span>
      </a>
      <nav class="rsb-nav" aria-label="Primary">{nav}</nav>
      <a href="get-quote.html" class="rsb-btn rsb-btn--primary rsb-btn--sm">Get a Quote</a>
    </div>
  </div>
</header>"""

def breadcrumb(items):
    parts = []
    for label, href in items:
        if href is None:
            parts.append(f'<li><span class="rsb-breadcrumb__current">{label}</span></li>')
        else:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
            parts.append('<li class="rsb-breadcrumb__sep">/</li>')
    return f"""<nav class="rsb-breadcrumb" aria-label="Breadcrumb">
  <div class="rsb-container">
    <ol class="rsb-breadcrumb__list">{"".join(parts)}</ol>
  </div>
</nav>"""

def imgurl(prompt):
    return f"https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt={prompt}&image_size=landscape_16_9"

def hero(h1, span_word, lede, bg_prompt, chips=None, actions=None, stats=None):
    if chips is None:
        chips = ["ISO 9001 / CE Certified","18+ Years OEM Experience","42,000 m\u00b2 Factory","60+ Export Countries"]
    if actions is None:
        actions = [("primary","Request a Free Quote","get-quote.html"),("ghost","Browse Our Products","products.html")]
    actions_html = "".join(f'<a href="{h}" class="rsb-btn rsb-btn--{s} rsb-btn--lg">{l}</a>' for s,l,h in actions)
    chips_html = "".join(f'<span class="rsb-hero__chip">{c}</span>' for c in chips)
    stats_html = ""
    if stats:
        inner = "".join(f'<div class="rsb-hero__stat"><strong>{s[0]}</strong><span>{s[1]}</span></div>' for s in stats)
        stats_html = f'<div class="rsb-hero__stats">{inner}</div>'
    title_html = h1.replace("__SPAN__", f"<span>{span_word}</span>")
    return f"""<section class="rsb-hero" aria-labelledby="hero-title">
  <div class="rsb-hero__bg" style="background-image:url('{imgurl(bg_prompt)}')"></div>
  <div class="rsb-container">
    <div class="rsb-hero__content">
      <span class="rsb-hero__eyebrow">Yukings  \u00b7 Noise Barrier Manufacturer Since 2006</span>
      <h1 id="hero-title">{title_html}</h1>
      <p class="lede">{lede}</p>
      <div class="rsb-hero__actions">{actions_html}</div>
      <div class="rsb-hero__quick">{chips_html}</div>
      {stats_html}
    </div>
  </div>
</section>"""

def section_head(eyebrow, title, desc=None):
    desc_html = f"<p>{desc}</p>" if desc else ""
    return f"""<div class="rsb-section__head">
  <span class="rsb-eyebrow">{eyebrow}</span>
  <h2>{title}</h2>
  <div class="rsb-divider rsb-divider--center"></div>
  {desc_html}
</div>"""

def footer():
    return """<footer class="rsb-footer">
  <div class="rsb-container">
    <div class="rsb-footer__grid">
      <div class="rsb-footer__about">
        <div class="rsb-footer__logo"><span class="rsb-logo__mark">Y</span><span>Yukings</span></div>
        <p>Shenzhen Yukings Industrial Co., Ltd. is a professional manufacturer of noise barriers, sound walls and acoustic barriers. 42,000 m\u00b2 factory, 18+ years OEM experience, ISO 9001 / ISO 14001 / CE certified. Exported to 60+ countries across North America, Europe, Australia, Southeast Asia and the Middle East.</p>
        <p>Room 1405, Building B2, Yunzhi Tech Park, Guangming District, Shenzhen, Guangdong, China</p>
      </div>
      <div><h4>Products</h4><ul>
        <li><a href="railway-noise-barriers.html">Railway Noise Barriers</a></li>
        <li><a href="highway-noise-barriers.html">Highway Noise Barriers</a></li>
        <li><a href="solar-noise-barriers.html">Solar Noise Barriers</a></li>
        <li><a href="industrial-noise-barriers.html">Industrial Noise Barriers</a></li>
        <li><a href="residential-noise-barriers.html">Residential Noise Barriers</a></li>
        <li><a href="products.html">All Product Lines</a></li>
      </ul></div>
      <div><h4>Solutions &amp; Projects</h4><ul>
        <li><a href="railway-noise-reduction.html">Railway Noise Reduction</a></li>
        <li><a href="highway-noise-control.html">Highway Noise Control</a></li>
        <li><a href="industrial-factory-noise-barriers.html">Industrial Factory Solutions</a></li>
        <li><a href="residential-community-noise-protection.html">Residential Community Protection</a></li>
        <li><a href="solar-energy-noise-barrier-solutions.html">PV / Solar Noise Barriers</a></li>
        <li><a href="projects.html">Project Case Studies</a></li>
      </ul></div>
      <div><h4>Contact Yukings</h4><ul class="rsb-footer__contact">
        <li><i>&#9742;</i><span>Tel: +86-755-86366707</span></li>
        <li><i>&#9993;</i><span>Email: weilai04525@163.com</span></li>
        <li><i>&#9990;</i><span>Miss Tang (Sales): +86 17727812004</span></li>
        <li><i>&#9990;</i><span>Mr. Yu (Engineering): +86 13828819804</span></li>
      </ul></div>
    </div>
    <div class="rsb-footer__bottom">
      <span>&copy; 2006-2026 Shenzhen Yukings Industrial Co., Ltd. Noise Barrier Manufacturer. ISO 9001/14001/45001. CE. EN 14388.</span>
      <div class="rsb-footer__social">
        <a href="contact.html">Contact</a><a href="privacy-policy.html">Privacy</a><a href="terms-of-service.html">Terms</a><a href="faqs.html">FAQs</a>
      </div>
    </div>
  </div>
</footer>"""

def cookie_bar():
    return """<div class="rsb-cookie" role="dialog" aria-label="Cookie consent">
  <p>Yukings.net uses cookies to improve your browsing experience and analyze anonymized traffic. By continuing to use this site you agree to our <a href="privacy-policy.html">privacy policy</a> and <a href="terms-of-service.html">terms</a>.</p>
  <button type="button">Accept</button>
</div>"""

def page_head(title, description, canonical):
    og_img = imgurl("modern-industrial-noise-barrier-factory-site-aerial")
    org_ld = '{"@context":"https://schema.org","@type":"Organization","name":"Shenzhen Yukings Industrial Co., Ltd.","alternateName":"Yukings","url":"https://www.yukings.net","logo":"https://www.yukings.net/img/yukings-logo.svg","image":"https://www.yukings.net/img/yukings-factory.webp","description":"Noise barrier manufacturer based in Shenzhen, China. 18+ years OEM experience, 42,000 m\u00b2 factory, ISO 9001/14001/45001 and CE certified.","foundingDate":"2006","foundingLocation":"Shenzhen, Guangdong, China","hasOfferCatalog":{"@type":"OfferCatalog","name":"Yukings Noise Barrier Catalog","itemListElement":["Railway Noise Barriers","Highway Noise Barriers","Industrial Noise Barriers","Residential Noise Barriers","Solar Noise Barriers"]},"slogan":"Engineered Acoustic Barriers for a Quieter World","telephone":"+86-755-86366707","email":"weilai04525@163.com","address":{"@type":"PostalAddress","streetAddress":"Room 1405, Building B2, Yunzhi Tech Park, Guangming District","addressLocality":"Shenzhen","addressRegion":"Guangdong","postalCode":"518106","addressCountry":"CN"},"geo":{"@type":"GeoCoordinates","latitude":22.7673,"longitude":113.9696},"sameAs":["https://www.linkedin.com/company/yukings","https://www.facebook.com/yukings","https://www.youtube.com/@yukings"],"contactPoint":[{"@type":"ContactPoint","telephone":"+86-755-86366707","contactType":"customer service","availableLanguage":["English","Chinese"]}]}'
    bread_ld = '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.yukings.net/index.html"}]}'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="noise barrier, sound barrier, acoustic barrier, galvanized steel noise barrier, aluminum noise barrier, concrete sound wall, PC transparent noise barrier, highway noise barrier, railway noise barrier, industrial noise control, residential acoustic fence, solar noise barrier, Yukings manufacturer, OEM noise barrier, China noise barrier factory">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="Shenzhen Yukings Industrial Co., Ltd.">
<link rel="canonical" href="https://www.yukings.net/{canonical}">
<link rel="alternate" hreflang="en" href="https://www.yukings.net/{canonical}">
<link rel="alternate" hreflang="x-default" href="https://www.yukings.net/{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title.split('|')[0].strip()} | Yukings">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://www.yukings.net/{canonical}">
<meta property="og:site_name" content="Yukings - Noise Barrier Manufacturer">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title.split('|')[0].strip()} | Yukings">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_img}">
<style>
{SHARED_CSS}
</style>
<script type="application/ld+json">
{org_ld}
</script>
<script type="application/ld+json">
{bread_ld}
</script>
</head>
<body>
{topbar()}
{header(canonical)}
"""

def page_close():
    return f"""{footer()}
{cookie_bar()}
</body>
</html>"""

def write_page(filename, html_text):
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_text)
    print(f"  [wrote] {path} ({len(html_text)} chars)")

def cta_section(title_text, subtitle):
    return f"""<section class="rsb-cta">
  <div class="rsb-container">
    <div class="rsb-cta__inner">
      <span class="rsb-eyebrow">Ready to Take the Next Step?</span>
      <h2>{title_text}</h2>
      <p>{subtitle}</p>
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
</section>"""

def faq_section(faqs, eyebrow="Frequently Asked Questions", title="Answers to common questions", desc="Explore answers to common questions about our noise barrier products, certifications, lead times, OEM customization and logistics. Our team responds to detailed inquiries within 24 hours."):
    items = "".join(f'<div class="rsb-faq__item"><div class="rsb-faq__q">{q}</div><div class="rsb-faq__a">{a}</div></div>' for q,a in faqs)
    return f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head(eyebrow, title, desc)}
    <div class="rsb-faq">{items}</div>
  </div>
</section>"""

def stat_section(stats, eyebrow="At a Glance", title="Manufacturing capacity, quality data and export footprint", desc="Numbers matter in industrial procurement. Here is a transparent overview of Yukings capacity, certifications, experience and global reach to support your due diligence."):
    items = "".join(f'<div class="rsb-stat"><strong>{s[0]}</strong><span>{s[1]}</span></div>' for s in stats)
    return f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head(eyebrow, title, desc)}
    <div class="rsb-stats">{items}</div>
  </div>
</section>"""

def feature_section(features, eyebrow="Core Capabilities", title="What makes Yukings the preferred noise barrier partner", desc="From raw material sourcing through acoustic testing and containerized shipping, Yukings controls every stage of the noise barrier production chain."):
    items = "".join(f'<div class="rsb-feature"><i class="rsb-feature__icon">{f[0]}</i><h3>{f[1]}</h3><p>{f[2]}</p></div>' for f in features)
    return f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head(eyebrow, title, desc)}
    <div class="rsb-features">{items}</div>
  </div>
</section>"""

def card(title, meta, text, link_label, href, prompt, tag):
    return f"""<div class="rsb-card">
  <div class="rsb-card__media">
    <div class="rsb-card__img" style="background-image:url('{imgurl(prompt)}')"></div>
    <span class="rsb-card__tag">{tag}</span>
  </div>
  <div class="rsb-card__body">
    <span class="rsb-card__meta">{meta}</span>
    <h3 class="rsb-card__title">{title}</h3>
    <p class="rsb-card__text">{text}</p>
    <a href="{href}" class="rsb-card__link">{link_label} &rarr;</a>
  </div>
</div>"""

def split_block(prompt, eyebrow, heading, paragraphs, bullets, actions=None, reverse=False):
    rev = " rsb-split--reverse" if reverse else ""
    li = "".join(f"<li>{b}</li>" for b in bullets)
    para = "".join(f"<p>{p}</p>" for p in paragraphs)
    act = ""
    if actions:
        act = f'<div class="rsb-split__actions">{"".join(f"<a href=\"{a[2]}\" class=\"rsb-btn rsb-btn--{a[0]}\">{a[1]}</a>" for a in actions)}</div>'
    return f"""<div class="rsb-split{rev}">
  <div class="rsb-split__media"><div class="rsb-split__img" style="background-image:url('{imgurl(prompt)}')"></div></div>
  <div class="rsb-split__body">
    <span class="rsb-split__eyebrow">{eyebrow}</span>
    <h2>{heading}</h2>
    <div class="rsb-divider"></div>
    {para}
    <ul class="rsb-split__list">{li}</ul>
    {act}
  </div>
</div>"""

def specs_table(title, headers, rows):
    head = "".join(f"<th>{h}</th>" for h in headers)
    body_rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"""<div class="rsb-tablewrap">
  <div class="rsb-table-head"><h3>{title}</h3></div>
  <div class="rsb-table-body">
    <table class="rsb-table">
      <thead><tr>{head}</tr></thead>
      <tbody>{body_rows}</tbody>
    </table>
  </div>
</div>"""

def cert_block(certs):
    items = "".join(f'<div class="rsb-cert"><div class="rsb-cert__badge">{c[0]}</div><h3>{c[1]}</h3><p>{c[2]}</p></div>' for c in certs)
    return f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Certifications", "Accredited by leading industry standards worldwide", "Yukings noise barriers meet European, North American, and Chinese industrial standards. Every shipment leaves with a full technical dossier and third-party test reports.")}
    <div class="rsb-certs">{items}</div>
  </div>
</section>"""

print("helpers.py loaded successfully.")
