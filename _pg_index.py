#!/usr/bin/env python3
"""Yukings site generator - pages (part 2): index, products."""
import sys
sys.path.insert(0, "/workspace")
from _helpers import *

def page_index():
    b = []
    b.append(page_head(
        "Yukings | Noise Barrier Manufacturer - Railway, Highway, Industrial, Solar",
        "Shenzhen Yukings is a professional noise barrier manufacturer. 42,000 m\u00b2 factory, 18+ years OEM experience, ISO 9001 / ISO 14001 / CE certified. Exporting to 60+ countries.",
        "index.html"))
    b.append(breadcrumb([("Home", None)]))
    b.append(hero(
        "Engineered acoustic barriers for a __SPAN__ world.",
        "quieter",
        "Yukings designs and manufactures performance-rated noise barriers for highways, railways, solar farms, industrial plants and residential communities. Up to 45 dB insertion loss, modular panels, fully custom engineered.",
        "highway-noise-barrier-sunset-industrial-silhouette",
        stats=[("45 dB","Max Insertion Loss"),("42,000 m\u00b2","Factory Floor"),("109+","Barrier Patents"),("60+","Export Countries")]))

    cats = [
        ("Railway Noise Barriers","Category \u00b7 20-45 dB","High-speed rail noise barriers for metro lines, commuter rail and freight corridors.",
         "Explore railway solutions","railway-noise-barriers.html","railway-noise-barrier-high-speed-train","RAIL"),
        ("Highway Noise Barriers","Category \u00b7 25-42 dB","Modular highway sound walls for expressways, ring roads and bridge parapets.",
         "Explore highway solutions","highway-noise-barriers.html","highway-noise-barrier-road-traffic","HIGHWAY"),
        ("Solar Noise Barriers","Category \u00b7 25-35 dB","Bifacial PV-integrated acoustic barriers that turn noise into clean energy.",
         "Explore solar solutions","solar-noise-barriers.html","solar-noise-barrier-photovoltaic-farm","SOLAR"),
        ("Industrial Noise Barriers","Category \u00b7 30-45 dB","Plant perimeter acoustic walls for factories, power stations and energy hubs.",
         "Explore industrial solutions","industrial-noise-barriers.html","industrial-noise-barrier-factory-plant","INDUSTRIAL"),
        ("Residential Noise Barriers","Category \u00b7 20-32 dB","Privacy and acoustic screening for housing estates, schools and hospitals.",
         "Explore residential solutions","residential-noise-barriers.html","residential-acoustic-barrier-community-garden","RESIDENTIAL"),
    ]
    cards_html = "".join(card(*c) for c in cats)
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Product Lines","Five engineered acoustic barrier categories",
                   "Each Yukings noise barrier product line is engineered around a specific application, tested to EN 1793 / ASTM E90, and offered with transparent, metal-louvered or micro-perforated acoustic faces.")}
    <div class="rsb-grid rsb-grid--3" style="grid-template-columns:repeat(3,1fr)">
      {cards_html}
    </div>
  </div>
</section>""")

    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Why Yukings","End-to-end noise barrier manufacturing under one roof")}
    {split_block("noise-barrier-factory-production-line","Own Factory",
                  "42,000 m\u00b2 of vertically-integrated manufacturing",
                  ["Yukings operates one of the largest purpose-built noise barrier factories in South China, with automated roll-forming, CNC perforation, electrostatic powder coating and acoustic test facilities on-site.","We hold raw-material inventory for galvanized steel, aluminum alloy, PC acrylic, concrete and recycled-rubber acoustic panels."],
                  ["In-house tooling and custom dies","Acoustic testing lab (ISO/IEC 17025)","Powder coating and hot-dip galvanizing lines","CNC perforation and laser cutting"],
                  [("primary","Tour Our Factory","about.html"),("ghost-alt","Download Datasheet","products.html")])}
    {split_block("noise-barrier-acoustic-testing-laboratory","Acoustic Performance",
                  "Up to 45 dB insertion loss, tested to EN 1793-1 / ASTM E90",
                  ["Every Yukings noise barrier panel is performance-tested in our accredited in-house acoustic laboratory. We publish insertion loss (DL), sound insulation (Rw), and absorption (alpha w) curves with each product."],
                  ["Up to 45 dB noise reduction (DL, 200 Hz \u2013 5 kHz)","Single-number ratings published per EN 1793-1 / ASTM E90 / GB/T 19889","Third-party test reports delivered with every PO"],
                  [("primary","View Technical Data","products.html"),("ghost-alt","Request Test Report","get-quote.html")], reverse=True)}
    {split_block("noise-barrier-installation-team-construction-site","Turnkey Installation",
                  "Modular bolted construction, delivered CKD or fully installed",
                  ["Our in-house engineering and installation crews have delivered more than 2,400,000 m\u00b2 of noise barriers across China and overseas. We ship CKD (completely knocked down) or install turnkey, depending on your project."],
                  ["Standard panels install 200 m/day with a 12-person crew","Pre-drilled H-post and splice connections","On-site supervision and technical support available globally"],
                  [("primary","See Project Examples","projects.html"),("ghost-alt","Talk to an Engineer","contact.html")])}
  </div>
</section>""")

    b.append(stat_section([
        ("2,400,000+","m\u00b2 of noise barriers installed"),
        ("18 years","of OEM / ODM manufacturing history"),
        ("45 dB","maximum insertion loss achieved"),
        ("60+","countries receiving Yukings products"),
    ]))
    b.append(cta_section(
        "Ready to spec your next noise barrier project? Contact the Yukings team today.",
        "Tell us about your project \u2014 whether it is a 2-km highway run, a high-speed rail corridor, a PV solar noise barrier, or an industrial plant enclosure. Our acoustic engineers will respond with a technical proposal within 24 hours."))
    b.append(faq_section([
        ("What is the typical lead time for standard noise barrier panels?",
         "Standard Yukings noise barrier panels (galvanized steel louvered panels in 2,500 x 500 x 80 mm format) ship within 20 working days from order confirmation. Custom-engineered panels, PV-integrated solar noise barriers and large-volume projects typically ship within 40 working days."),
        ("Do you provide acoustic simulations and CAD drawings?",
         "Yes. Our engineering team delivers acoustic simulation (CNOSSOS-EU / FHWA TNM 2.5), structural calculation, AutoCAD and Revit drawings, and BIM coordination for every noise barrier project at no extra cost when a formal PO is placed."),
        ("Can I request samples and test reports before ordering?",
         "Absolutely. Yukings ships acoustic barrier sample panels, typically 500 x 500 mm, together with CE / ISO test reports, acoustic insertion loss curves and material certificates to any project engineer or buyer upon request."),
        ("What certification do your noise barriers carry?",
         "Yukings noise barriers are produced in compliance with EN 1793-1/-2/-5 (acoustic performance), EN 1794-1/-2 (mechanical performance and durability), ASTM E90 and ASTM C423, plus the Chinese national noise barrier standard GB/T 34509. Our factory management system is ISO 9001, ISO 14001 and ISO 45001 certified."),
        ("Do you export and ship worldwide?",
         "Yes. Yukings ships noise barriers to 60+ countries across North America, Europe, Australia, Southeast Asia and the Middle East. We handle containerized FOB / CIF / DAP shipping and provide full shipping documents (packing list, commercial invoice, certificate of origin, test reports, CE declaration of conformity)."),
        ("What is the warranty on Yukings noise barrier products?",
         "All standard Yukings noise barrier panels carry a 15-year structural warranty against manufacturing defects under normal use, with a designed service life of 25 years. Acoustic performance is warranted to remain within +/- 2 dB of the published rating for the warranty period."),
    ], title="Answers to common questions"))
    b.append(page_close())
    return "".join(b)

# Write index
write_page("index.html", page_index())
print("pages part 2 (index) done.")
