#!/usr/bin/env python3
"""Yukings site generator - pages (part 5): 5 product category pages."""
import sys
sys.path.insert(0, "/workspace")
from _helpers import *

def make_product_page(filename, title_short, title_long, subtitle, core_keyword,
                       bg_prompt, hero_h1, stats, specs_rows, chips,
                       panel_material, depth_range, application_text,
                       category_items):
    b=[]
    b.append(page_head(
        f"{title_long} | Yukings Noise Barrier Manufacturer",
        subtitle, filename))
    b.append(breadcrumb([("Home","index.html"),("Products","products.html"),(title_short,None)]))
    b.append(hero(hero_h1, core_keyword, subtitle, bg_prompt,
                  chips=chips, stats=stats))

    # overview section
    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Product Overview", f"Yukings {title_short}")}
    {split_block(bg_prompt, "What is it", f"Engineered {title_short.lower()} for modern infrastructure projects.",
                  [application_text],
                  category_items,
                  [("primary","Request a Quote","get-quote.html"),("ghost-alt","Download Datasheet","products.html")])}
  </div>
</section>""")

    # specification table
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Technical Specification", f"Full specification for {title_short}")}
    {specs_table(f"{title_short} - Product Specification", ["Property", "Value"], specs_rows)}
  </div>
</section>""")

    # feature section
    b.append(feature_section([
        ("Q1","Quality Control","Every panel is inspected and tested before dispatch, with full quality dossier including CE and ISO test reports."),
        ("C1","Custom Design","Custom heights, finishes, colors (RAL), transparent window sections, perforation patterns and green-wall integration available."),
        ("M1",panel_material,"Panel face material with mineral wool core. Hot-dip galvanized steel posts with optional powder coat finish."),
        ("D1",f"{depth_range}","Typical panel depths from 80 to 140 mm depending on the insertion loss requirement of your project."),
        ("W1","25-Year Design Life","Designed for a 25-year service life with a 15-year structural warranty on Yukings-manufactured panels."),
        ("G1","Global Shipping","Full containerized shipping (20 ft / 40 ft HC / 40 ft OOG) with full shipping documents delivered with every shipment."),
    ], eyebrow="Why Yukings", title=f"What makes our {title_short} different"))

    b.append(cta_section(
        f"Need a {title_short} quotation for your project? Contact Yukings today.",
        f"Our {title_short} specialists will respond to your project inquiry within 24 hours, including technical guidance and pricing where applicable."))
    b.append(page_close())
    return "".join(b)

# 1. Railway
railway = make_product_page(
    "railway-noise-barriers.html", "Railway Noise Barriers",
    "Railway Noise Barriers for High-Speed Rail",
    "Yukings railway noise barriers for high-speed rail, metro, light-rail and commuter corridors. Metal-louvered panels with mineral wool core, optional PC transparent windows.",
    "railway noise barriers",
    "railway-noise-barriers-high-speed-rail",
    "Railway noise barriers for high-speed rail, metro, light rail and freight __SPAN__.",
    [("25-45 dB","insertion loss"),("80-140 mm","panel depth"),("2,500x500","standard size"),("350 km/h","rated speed")],
    [["Insertion Loss DL (EN 1793-3)","25 \u2013 45 dB"],["Sound Insulation Rw (EN ISO 717-1)","32 \u2013 52 dB"],["Panel Width","2,500 mm"],["Panel Height","500 mm"],["Panel Depth","80 / 100 / 120 / 140 mm"],["Panel Face Material","DX51D+Z galvanized steel or EN AW-5754 aluminum alloy"],["Panel Face Thickness","1.5 mm (standard) / 2.0 mm (heavy-duty)"],["Perforation","2.0-3.0 mm perforated metal, 25-35% open area"],["Core Material","Hydrophobic rock-wool, 80-140 kg/m3"],["H-post Column Size","H 100 x 100 x 6 x 8 mm or H 125 x 125 x 6.5 x 9 mm"],["H-post Spacing","2.0 m or 2.5 m (bay spacing)"],["Barrier Height Range","2.0 \u2013 8.0 m (heights >5.0 m on request)"],["Design Service Life","25 years"],["Structural Warranty","15 years"],["Corrosion Resistance","ISO 12944 C4-H"],["Fire Rating","Class A (EN 13501-1)"],["Wind Load Rating","1.0 kN/m2 (EN 1991-1-4)"],["Aerodynamic Pulse Resistance","Tested for train speed 350 km/h"],["Finish / Color","RAL 7030 stone grey or custom RAL color"],["Transparent Window Option","Yes - 8 / 10 / 12 mm polycarbonate sheet"]],
    ["EN 1793 / 1794 tested","ISO 9001 certified factory","Aerodynamic pulse tested","Hydrophobic mineral wool core","Custom heights"],
    "Galvanized Steel / Aluminum Alloy Face",
    "80 mm - 140 mm Depth",
    "Yukings railway noise barriers are designed for heavy-vibration and high-aerodynamic-pulse service conditions along high-speed rail, metro and commuter rail corridors. Panels combine metal-louvered absorption faces with hydrophobic rock-wool cores, optional PC transparent window sections for landscape visibility, and are mounted on galvanized steel H-posts with elastomeric vibration isolation pads.",
    ["High-speed rail up to 350 km/h","Metro and light-rail transit","Freight railway corridors","Bridge parapet and viaduct noise barriers"])

# 2. Highway
highway = make_product_page(
    "highway-noise-barriers.html","Highway Noise Barriers",
    "Highway Noise Barriers - Metal Louvered & Transparent",
    "Yukings highway noise barriers: metal-louvered absorption panels, transparent polycarbonate acrylic windows and concrete panels. EN 1793, EN 1794, CE certified.",
    "highway noise barriers",
    "highway-noise-barriers-expressway",
    "Highway noise barriers for expressways, ring roads and bridges - reduce road traffic noise by up to __SPAN__ dB.",
    [("25-42 dB","insertion loss"),("80-140 mm","panel depth"),("2.0-2.5 m","H-post bay"),("25 yr","design service life")],
    [["Insertion Loss DL (EN 1793-3)","25 \u2013 42 dB"],["Sound Insulation Rw (EN ISO 717-1)","30 \u2013 52 dB"],["Panel Width","2,500 mm standard"],["Panel Height","500 mm standard"],["Panel Depth","80 / 100 / 120 / 140 mm"],["Panel Face Material","DX51D+Z galvanized steel or EN AW-5754 aluminum alloy"],["Infill Material","High-density hydrophobic rock-wool 80-140 kg/m3"],["H-post Column Size","H 100 x 100 x 6 x 8 mm or H 125 x 125 x 6.5 x 9 mm or IPE 100/120"],["H-post Spacing","2.0 m or 2.5 m bays"],["Barrier Height","2.0 \u2013 5.0 m"],["Design Service Life","25 years"],["Structural Warranty","15 years"],["Corrosion Resistance","ISO 12944 C3-M / C4-H"],["Fire Rating","Class A (EN 13501-1)"],["Wind Load Rating","1.2 kN/m2 (EN 1991-1-4)"],["Finish","Hot-dip galvanized + optional RAL powder coating"],["Transparent Window","8 / 10 / 12 mm UV-stabilized polycarbonate sheet"],["Concrete Panel Option","50 / 80 / 120 mm pre-cast concrete"]],
    ["EN 1793 / 1794","CE Marked","ISO 9001 Factory","Containerized Shipping","Powder-Coat or Galvanized"],
    "Galvanized Steel / Aluminum Alloy Face", "80 mm - 140 mm Depth",
    "The classic Yukings highway noise barrier combines a galvanized steel louvered metal face with high-density mineral wool core, delivering strong road-traffic noise absorption with a clean, maintenance-free finish. Panels mount on standard hot-dip galvanized steel H-beam posts with pre-drilled fastener locations.",
    ["Expressways, intercity highways and ring roads","Bridge parapet noise barriers","Tunnels, underpasses and ramp entrances","Car park, toll plaza and interchange noise control"])

# 3. Solar
solar = make_product_page(
    "solar-noise-barriers.html","Solar Noise Barriers","Solar PV-Integrated Noise Barriers",
    "Yukings bifacial PV-integrated noise barriers: EN 1793 tested acoustic absorbers with monocrystalline bifacial PV modules on the rear. Generate electricity while reducing road noise.",
    "solar noise barriers",
    "solar-noise-barriers-bifacial-pv",
    "Noise barriers that turn road traffic noise into clean __SPAN__.",
    [("25-35 dB","insertion loss"),("420-540 W","bifacial PV module"),("~180 kWh/m/yr","electricity output"),("25 yr","power warranty")],
    [["Insertion Loss DL (EN 1793-3)","25 \u2013 35 dB"],["Acoustic Panel Depth","100 mm (road-facing absorption panel)"],["PV Module Type","Monocrystalline bifacial silicon"],["PV Module Power","420 \u2013 540 W"],["Panel Size","2,000 x 1,000 mm (standard, metric panels)"],["H-post","Hot-dip galvanized H-beam, pre-drilled"],["H-post Spacing","2.0 m or 2.5 m bays"],["Barrier Height","3.0 \u2013 5.0 m standard"],["Inverter","Grid-tie string inverter, project specified"],["Grid Connection","Medium-voltage (project specified)"],["Design Service Life","25 years (acoustic and PV structure)"],["PV Module Product Warranty","10-12 years (module manufacturer)"],["PV Linear Power Warranty","25 years (80% of rated power)"],["Structural Warranty","15 years on Yukings structural elements"],["Wind + Snow Load","Designed to EN 1991-1-3 / EN 1991-1-4"],["Fire Rating","Class A (EN 13501-1)"],["IEC Standard","IEC 61215, IEC 61730 (module level)"]],
    ["Bifacial PV","EN 1793 Tested","25-Year PV Warranty","Containerized","Grid-Tie Inverter Ready"],
    "Aluminum Alloy + PV Module Face","120 - 160 mm Panel Depth",
    "The Yukings solar noise barrier is a hybrid acoustic and photovoltaic panel. On the road-facing side, an EN 1793-1 tested acoustic absorber reduces road traffic noise. On the rear side, a monocrystalline bifacial PV panel generates electricity from both direct and reflected sunlight, converting a roadside noise barrier into a revenue-generating asset for highway authorities, developers and infrastructure investors.",
    ["Highway median noise barriers","Roadside noise barriers with south-facing rear","Solar + acoustic for new-build infrastructure","Infrastructure-as-a-service solar noise barriers"])

# 4. Industrial
industrial = make_product_page(
    "industrial-noise-barriers.html","Industrial Noise Barriers","Industrial Plant Perimeter Acoustic Barriers",
    "Yukings industrial noise barriers - heavy-gauge steel-faced absorption panels up to 140 mm with modular H-beam support system for factory, power station and energy plant projects.",
    "industrial noise barriers",
    "industrial-noise-barriers-plant-power",
    "Industrial acoustic barriers for factories, power stations and energy __SPAN__.",
    [("30-45 dB","insertion loss"),("100-180 mm","panel depth"),("1.5 kN/m2","wind load"),("12 m","max height")],
    [["Insertion Loss DL (EN 1793-3)","30 \u2013 45 dB"],["Sound Insulation Rw (EN ISO 717-1)","40 \u2013 55 dB"],["Panel Depth","100 / 120 / 140 / 160 / 180 mm"],["Panel Face Material","Heavy-gauge DX51D+Z galvanized steel or EN AW-5754 aluminum alloy"],["Panel Face Thickness","1.5 / 2.0 / 2.5 mm (heavy-duty option)"],["Core Material","High-density mineral wool + acoustic membrane (on request)"],["Support System","H-beam or I-beam posts, project designed"],["Post Spacing","1.5 m or 2.0 m (heavy-duty bays)"],["Barrier Height","3.0 m up to 12 m on request"],["Design Service Life","25 years"],["Structural Warranty","15 years"],["Corrosion Resistance","ISO 12944 C5-M (severe industrial / coastal)"],["Fire Rating","Class A (EN 13501-1)"],["Wind Load Rating","1.5 kN/m2 (EN 1991-1-4, project specific)"],["Optional Features","Roof absorption baffle arrays, machine enclosure panels"],["Finish","Hot-dip galvanized + optional RAL powder coat"]],
    ["Heavy-Gauge","ISO 12944 C5-M","Up to 12 m Height","Structurally Engineered","Acoustic Testing"],
    "Heavy-Gauge Galvanized Steel / Aluminum Alloy","100 mm - 180 mm Depth",
    "Yukings industrial noise barriers are designed for heavy-duty industrial environments, including power plants, oil & gas facilities, factories, data center cooling systems, pumping stations and process plants. Panels combine a heavy-gauge galvanized steel face with high-density mineral wool core and optional acoustic membrane to deliver up to 45 dB insertion loss at the plant perimeter.",
    ["Power plant and combined-cycle gas turbine (CCGT)","Oil and gas facilities","Manufacturing and process plant","Data center cooling systems and pumping stations"])

# 5. Residential
residential = make_product_page(
    "residential-noise-barriers.html","Residential Noise Barriers","Community and Residential Acoustic Barriers",
    "Yukings residential community noise barriers for housing estates, schools and hospitals - with optional green-wall integration, wood-grain finishes and transparent PC windows.",
    "residential noise barriers",
    "residential-noise-barriers-community-garden",
    "Community-friendly noise barriers for housing estates, schools and __SPAN__.",
    [("20-32 dB","insertion loss"),("2.0-4.0 m","typical heights"),("25 yr","design life"),("Optional","green-wall integration")],
    [["Insertion Loss DL (EN 1793-3)","20 \u2013 32 dB"],["Sound Insulation Rw (EN ISO 717-1)","28 \u2013 45 dB"],["Panel Width","2,000 mm"],["Panel Height","500 mm standard"],["Panel Depth","80 / 100 / 120 mm"],["Panel Face Material","Aluminum alloy or galvanized steel"],["Core Material","High-density mineral wool 80 kg/m3"],["Post System","Hot-dip galvanized H-post or decorative post on request"],["Barrier Height","2.0 \u2013 4.0 m"],["Finish Options","RAL powder coat, wood-grain finish, brick pattern, custom finish"],["Transparent Window Option","Yes - 8 / 10 / 12 mm polycarbonate acrylic"],["Green-Wall Integration","Optional - vertical garden panels on rear face"],["Design Service Life","25 years"],["Structural Warranty","15 years"],["Fire Rating","Class B-s1,d0 (EN 13501-1) for typical finishes"],["Corrosion Resistance","ISO 12944 C3"],["Wind Load Rating","0.8 kN/m2 (EN 1991-1-4, project specified)"]],
    ["Community-Friendly","Optional Green-Wall","Wood-Grain or RAL Finish","PC Windows to Avoid Tunnel Effect","Modular Installation"],
    "Aluminum Alloy or Galvanized Steel","80 mm - 120 mm Depth",
    "Yukings residential community noise barriers combine good acoustic performance with community-friendly aesthetics, lower visual impact and optional green-wall integration to blend into residential surroundings. Heights from 2.0 m to 4.0 m, with optional transparent PC windows to avoid the visual tunnel effect at housing estates, schools and hospitals.",
    ["Housing estates and residential neighborhoods","Schools, universities and kindergartens","Hospitals and healthcare facilities","Retirement villages and community buildings"])

for name, html in [("railway-noise-barriers.html", railway),
                    ("highway-noise-barriers.html", highway),
                    ("solar-noise-barriers.html", solar),
                    ("industrial-noise-barriers.html", industrial),
                    ("residential-noise-barriers.html", residential)]:
    write_page(name, html)
print("pages part 5 (5 product categories) done.")
