#!/usr/bin/env python3
"""Yukings site generator - pages (part 3): products, solutions, projects."""
import sys
sys.path.insert(0, "/workspace")
from _helpers import *

def page_products():
    b=[]
    b.append(page_head(
        "Noise Barrier Products | Yukings - Galvanized Steel, Aluminum, Transparent, Solar",
        "Yukings manufactures galvanized steel, aluminum alloy, PC transparent, concrete, recycled-rubber and solar PV noise barriers. OEM custom engineered acoustic barriers for highway, railway, industrial and residential applications.",
        "products.html"))
    b.append(breadcrumb([("Home","index.html"),("Products",None)]))
    b.append(hero(
        "Complete noise barrier product __SPAN__.",
        "lineup",
        "Five acoustic barrier product categories - metal louvered, transparent acrylic, concrete, micro-perforated aluminum and PV-integrated solar noise barriers. All panels are performance-rated and engineered to EN 1793, EN 1794, ASTM E90, ASTM C423 and GB/T 34509.",
        "noise-barrier-product-lineup-modular-panels",
        chips=["ISO 9001/14001/45001 Certified","CE Marked per EN 1793/EN 1794","25-year design life","Custom OEM available"],
        actions=[("primary","Download Datasheet","get-quote.html"),("ghost","Request Sample","contact.html")],
        stats=[("5","core categories"),("20+","panel types"),("109+","patents"),("2.4M m\u00b2","installed worldwide")]))

    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Product Categories","Five engineered noise barrier families")}
    {split_block("railway-noise-barrier-product-panel","Railway Noise Barriers",
                  "Metal-louvered and transparent-acrylic rail noise barriers for high-speed rail, metro and commuter corridors (20-45 dB insertion loss).",
                  ["Yukings railway noise barriers are engineered to withstand heavy vibration, wheel-rail rolling noise and aero-acoustic impulse from passing high-speed trains up to 350 km/h.","Panels are 80-140 mm thick with galvanized steel or aluminum faces, mineral wool infill and optional PC transparent windows for landscape visibility.","Mounted on galvanized steel H-posts (100x100 or 125x125) spaced at 2.0 or 2.5 m bays. Typical height 2.0-5.0 m. Heights up to 8 m available upon project-specific structural engineering."],
                  ["Rolling noise and aero-acoustic noise suppression","Galvanized steel or aluminum alloy construction with mineral wool core","Optional polycarbonate transparent windows for landscape visibility","Up to 45 dB insertion loss (DL) per EN 1793-3"],
                  [("primary","View Railway Products","railway-noise-barriers.html"),("ghost-alt","View Railway Projects","railway-noise-reduction.html")])}
    {split_block("highway-noise-barrier-metal-louvered-product","Highway Noise Barriers",
                  "Metal-louvered, transparent and mixed-panel highway noise barriers engineered to EN 1793 (25-42 dB insertion loss).",
                  ["Yukings highway noise barriers are the workhorse of our product line. The classic louvered-metal panel with mineral wool absorption core delivers 25-42 dB insertion loss depending on panel depth, and is certified to EN 1793-1 / ASTM E90.","Standard panel sizes: 2,500 x 500 x 80/100/120/140 mm. Panels ship pre-drilled to site H-post spacing (2.0 or 2.5 m) for rapid, labor-saving installation."],
                  ["Certified insertion loss DL up to 42 dB per EN 1793-3","Hot-dip galvanized steel H-posts IPE / H-beam columns","Optional 80/100/120/140 mm panel depths","Full-color RAL powder coating available"],
                  [("primary","View Highway Products","highway-noise-barriers.html"),("ghost-alt","View Highway Projects","highway-noise-control.html")], reverse=True)}
    {split_block("solar-noise-barrier-product-bifacial-pv","Solar Noise Barriers",
                  "Bifacial PV-integrated acoustic barriers: turning noise into clean energy.",
                  ["The Yukings solar noise barrier combines an EN 1793-1 tested acoustic absorber on the road-facing side and a monocrystalline bifacial PV panel on the rear.","Standard panel: 2,000 x 1,000 x 160 mm. Bifacial PV modules 420-540 W. Typical output: 120-180 kWh per linear meter per year, depending on site conditions."],
                  ["Bifacial PV-integrated acoustic barrier","Up to 42 dB insertion loss","Monocrystalline silicon, 420-540 W bifacial modules","Grid-tie string inverter ready"],
                  [("primary","View Solar Products","solar-noise-barriers.html"),("ghost-alt","View Solar Projects","solar-energy-noise-barrier-solutions.html")])}
    {split_block("industrial-noise-barrier-plant-product","Industrial Noise Barriers",
                  "Industrial-grade acoustic enclosures and perimeter barriers for factories, power stations and energy hubs.",
                  ["Yukings industrial noise barriers combine heavy-gauge steel-faced absorption panels up to 140 mm with a fully-bolted modular H-beam support system capable of 45 dB insertion loss.","Panel heights up to 12 m available upon project-specific structural engineering. Available with rooftop absorption baffle options for plant-internal noise control."],
                  ["Up to 45 dB insertion loss per EN 1793-3 / ASTM E90","Heavy-gauge galvanized steel or aluminum alloy construction","Perimeter acoustic walls, rooftop absorption baffles, machine enclosures","IP65-IP66 rated, corrosion-resistant to ISO 12944 C4-H"],
                  [("primary","View Industrial Products","industrial-noise-barriers.html"),("ghost-alt","View Industrial Projects","industrial-factory-noise-barriers.html")], reverse=True)}
    {split_block("residential-noise-barrier-community-product","Residential Noise Barriers",
                  "Community-grade acoustic screening walls for housing estates, schools and hospitals.",
                  ["Yukings residential community noise barriers combine good acoustic performance with attractive, residential-friendly aesthetics, lower visual impact and optional green-wall integration. Heights from 2.0 m to 4.0 m, with optional transparent PC windows to avoid tunnel effect."],
                  ["20-32 dB insertion loss depending on panel depth and site conditions","Aluminum / galvanized steel faces, mineral wool core","Optional transparent acrylic windows","Available with wood-grain finish or green wall integration"],
                  [("primary","View Residential Products","residential-noise-barriers.html"),("ghost-alt","View Residential Projects","residential-community-noise-protection.html")])}
  </div>
</section>""")

    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Technical Comparison","Five noise barrier product families compared")}
    {specs_table("Panel Types and Performance",
                  ["Parameter","Railway Barriers","Highway Barriers","Solar Barriers","Industrial Barriers","Residential Barriers"],
                  [
                      ["Insertion Loss (EN 1793-3)","25-45 dB","25-42 dB","25-35 dB","30-45 dB","20-32 dB"],
                      ["Panel Depth","80-140 mm","80-140 mm","120-160 mm","100-180 mm","80-120 mm"],
                      ["Standard Panel Size","2,500 x 500 mm","2,500 x 500 mm","2,000 x 1,000 mm","2,000 x 500 mm","2,000 x 500 mm"],
                      ["Face Material","Galvanized steel / Al alloy","Galvanized steel / Al alloy","Aluminum alloy + bifacial PV","Heavy-gauge galvanized steel","Aluminum alloy / galvanized steel"],
                      ["Core Material","High-density mineral wool 80-140 kg/m\u00b3","High-density mineral wool 80-140 kg/m\u00b3","Mineral wool + PV module","High-density mineral wool + acoustic membrane","High-density mineral wool 80 kg/m\u00b3"],
                      ["H-post Spacing","2.0 m / 2.5 m bays","2.0 m / 2.5 m bays","2.0 m / 2.5 m bays","1.5 m / 2.0 m bays","2.0 m / 2.5 m bays"],
                      ["Design Service Life","25 years","25 years","25 years (PV: 25 year linear power warranty)","25 years","25 years"],
                      ["Structural Warranty","15 years","15 years","15 years","15 years","15 years"],
                      ["Coating / Finish","Hot-dip galvanized + optional powder coat","Hot-dip galvanized + optional powder coat","Anodized aluminum + PV module","Hot-dip galvanized + powder coat","Powder coated (RAL) or wood-grain"],
                      ["Corrosion Resistance","ISO 12944 C4-H","ISO 12944 C3-M / C4-H","ISO 12944 C4-H","ISO 12944 C5-M (severe industrial)","ISO 12944 C3"],
                      ["Transparent Window Option","Yes (PC 8/10/12 mm)","Yes (PC 8/10/12 mm)","No","Limited","Yes (PC or acrylic 8/10 mm)"],
                      ["Fire Rating","Class A (EN 13501-1)","Class A (EN 13501-1)","Class A (EN 13501-1)","Class A (EN 13501-1)","Class B-s1,d0"],
                      ["Wind Load Rating","1.0 kN/m\u00b2","1.2 kN/m\u00b2","1.2 kN/m\u00b2 plus PV snow/wind","1.5 kN/m\u00b2","0.8 kN/m\u00b2"],
                      ["Vibration Resistance","DIN 4150-2 / 3 (rail vibration)","DIN 4150-2 / 3","DIN 4150-2 / 3","DIN 4150-2 / 3","DIN 4150-2 / 3"],
                      ["Color Finish","RAL 7030 / custom","RAL 7030 / custom","Module black frame + Al silver / custom","RAL 7030 / custom","RAL custom or wood-grain"],
                  ])}
  </div>
</section>""")

    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Materials and Construction","Proven materials, controlled supply chain")}
    <div class="rsb-grid rsb-grid--4" style="grid-template-columns:repeat(4,1fr)">
      {card("Galvanized Steel Panels","Material \u00b7 DX51D+Z / S355","Continuous hot-dip galvanized steel sheet per EN 10346. Z275 minimum coating weight per EN ISO 1461. Excellent corrosion resistance in highway / railway service conditions.",
           "View specs","products.html","galvanized-steel-noise-barrier-sheet","STEEL")}
      {card("Aluminum Alloy Panels","Material \u00b7 EN AW-5754 / 6061-T6","Lightweight, non-corrosive aluminum alloy panels for coastal / solar noise barrier applications. Anodized or powder coated finishes available.",
           "View specs","products.html","aluminum-alloy-noise-barrier-sheet","ALUMINUM")}
      {card("PC Transparent Windows","Material \u00b7 Makrolon / Lexan","8 mm / 10 mm / 12 mm UV-stabilized polycarbonate sheets per ISO 12944 C3 environment. UV protected for 10+ years outdoor service.",
           "View specs","products.html","polycarbonate-transparent-noise-barrier","PC")}
      {card("Concrete & Recycled-Rubber Panels","Material \u00b7 Pre-cast concrete + recycled rubber","High-mass pre-cast concrete noise barrier panels available in 50, 80 and 120 mm thicknesses. UL94 V-0 fire-rated recycled-rubber composite for high-temperature industrial plant use.",
           "View specs","products.html","concrete-recycled-rubber-noise-barrier","COMPOSITE")}
    </div>
  </div>
</section>""")

    b.append(feature_section([
        ("01","In-House Tooling","Fully-owned CNC punching, roll-forming and laser cutting lines under one roof in Shenzhen."),
        ("02","Acoustic Testing","In-house acoustic lab delivers insertion loss, absorption and insulation curves per project."),
        ("03","CAD & BIM","AutoCAD, Revit and Tekla structural drawings for every noise barrier project."),
        ("04","Custom Colors & Finishes","Full RAL color palette, wood-grain, brick pattern, anodized finishes available."),
        ("05","Containerized Shipping","Full containerization (20ft / 40ft HC / 40ft OOG) with full shipping documentation."),
        ("06","OEM / ODM","OEM custom manufacturing programs for 18+ years to European and North American customers."),
        ("07","109+ Patents","Yukings holds 109 noise barrier related patents including railway, highway and solar panel designs."),
        ("08","24/7 Technical Support","Round-the-clock engineering and project support for international clients."),
    ]))
    b.append(cta_section(
        "Need a custom noise barrier quotation? Contact the Yukings engineering team today.",
        "Send us your project drawings, site noise assessment or just a description. Our engineering team will respond within 24 hours with technical data, drawings and firm quotation."))
    b.append(page_close())
    return "".join(b)

def page_solutions():
    b=[]
    b.append(page_head(
        "Noise Barrier Solutions | Yukings - Railway, Highway, Industrial, Solar, Residential",
        "Engineered noise barrier solutions for railway, highway, industrial, residential and solar-energy projects. EN 1793, EN 1794, ASTM E90, GB/T 34509. From feasibility to commissioning.",
        "solutions.html"))
    b.append(breadcrumb([("Home","index.html"),("Solutions",None)]))
    b.append(hero(
        "Tailored acoustic solutions from feasibility to __SPAN__.",
        "commissioning",
        "Yukings delivers turnkey noise barrier solutions. From initial acoustic simulation, structural design and project costing, through fabrication and site supervision \u2014 we support every stage of your project.",
        "noise-barrier-solutions-engineer-site-construction",
        chips=["End-to-End Project Delivery","CNOSSOS-EU / FHWA TNM 2.5","EN 1793 Test Reports","Turnkey Site Supervision"],
        actions=[("primary","Talk to a Solutions Engineer","contact.html"),("ghost","View Case Studies","projects.html")],
        stats=[("5","core solution areas"),("60+","countries delivered to"),("18 yr","engineering track record"),("42,000 m\u00b2","in-house factory")]))

    sols = [
        ("Railway Noise Reduction","Solution \u00b7 High-speed rail, metro, freight",
         "Comprehensive railway noise reduction solutions covering high-speed rail corridors, metro lines, light-rail transit and freight railways. Delivered from initial acoustic mapping through H-post installation.",
         "Explore railway solutions","railway-noise-reduction.html","railway-noise-reduction-corridor","RAIL"),
        ("Highway Noise Control","Solution \u00b7 Expressways, bridges, ring roads",
         "Highway noise control solutions including new-build sound walls, bridge-parapet retrofits and median barriers designed to EN 1793 and local highway authority specifications.",
         "Explore highway solutions","highway-noise-control.html","highway-noise-control-expressway","HIGHWAY"),
        ("Industrial Factory Noise Barriers","Solution \u00b7 Plant perimeter & enclosures",
         "Industrial plant perimeter noise barriers and machine enclosure solutions for factories, power stations, data centers, oil & gas facilities, and energy hubs.",
         "Explore industrial solutions","industrial-factory-noise-barriers.html","industrial-factory-noise-barrier-perimeter","INDUSTRIAL"),
        ("Residential Community Noise Protection","Solution \u00b7 Housing estates, schools, hospitals",
         "Residential-friendly noise protection solutions including community screening walls, school and hospital acoustic fences, and green-wall-integrated noise barriers.",
         "Explore residential solutions","residential-community-noise-protection.html","residential-community-noise-protection-garden","RESIDENTIAL"),
        ("Solar & Energy Noise Barrier Solutions","Solution \u00b7 PV-integrated acoustic barriers",
         "PV-integrated solar noise barrier solutions that deliver noise attenuation and clean energy generation for highway authorities, infrastructure developers and renewable energy companies.",
         "Explore solar solutions","solar-energy-noise-barrier-solutions.html","solar-energy-noise-barrier-pv-array","SOLAR"),
    ]
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Solution Areas","Five engineered acoustic-barrier solution areas")}
    <div class="rsb-grid rsb-grid--3" style="grid-template-columns:repeat(3,1fr)">
      {"".join(card(*s) for s in sols)}
    </div>
  </div>
</section>""")

    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Our Delivery Model","A four-stage approach to every project")}
    {split_block("noise-barrier-feasibility-acoustic-study","Stage 1 - Feasibility",
                  "Acoustic assessment and feasibility study.",
                  ["Before a single panel is specified, Yukings engineers run an acoustic assessment of your site, using CNOSSOS-EU or FHWA TNM 2.5 noise propagation models to establish required barrier heights, insertion loss targets and panel specification."],
                  ["Traffic / source noise measurement and modeling","Noise propagation simulation (CNOSSOS-EU, FHWA TNM 2.5)","Receiver analysis and environmental impact assessment","Feasibility report with budget-level cost estimate"],
                  [("primary","Request a Feasibility Study","get-quote.html"),("ghost-alt","See Our Process","about.html")])}
    {split_block("noise-barrier-cad-design-structural-engineering","Stage 2 - Design Engineering",
                  "Structural design, CAD drawings, BIM coordination.",
                  ["Yukings produces a full engineering design package including structural calculation for wind load and vibration, AutoCAD and Revit drawings, material specifications and a detailed testing and handover plan."],
                  ["Structural calculation for wind, vibration and seismic events","AutoCAD 2D + Revit BIM drawings","Material specifications and test certificates","Detailed installation plan and bill of materials"],
                  [("primary","Talk to our Design Team","contact.html"),("ghost-alt","Engineering Capabilities","about.html")], reverse=True)}
    {split_block("noise-barrier-factory-manufacturing-quality","Stage 3 - Manufacturing & Quality",
                  "In-house fabrication, testing, and QC inspection.",
                  ["Every Yukings noise barrier is manufactured in our own 42,000 m\u00b2 Shenzhen factory, fully inspected and tested to EN 1793 / ASTM standards before dispatch. Full quality dossier is available with every shipment."],
                  ["ISO 9001 / ISO 14001 / ISO 45001 factory management","Full CE Technical Construction File (TCF) on request","In-house acoustic lab (insertion loss testing)","Dedicated QC inspection and NDE (non-destructive evaluation)"],
                  [("primary","Tour Our Factory","about.html"),("ghost-alt","Quality Documents","contact.html")])}
    {split_block("noise-barrier-installation-site-supervision","Stage 4 - Installation & Handover",
                  "Installation supervision and as-built handover.",
                  ["Yukings supports turnkey installation or provides expert site supervision to your local installation crew, with full as-built documentation, operation and maintenance manuals and a 15-year structural warranty."],
                  ["Turnkey installation crews available internationally","Site supervision by certified Yukings engineers","As-built drawings, O&M manuals","15-year structural warranty, 25-year designed service life"],
                  [("primary","Discuss Your Project","contact.html"),("ghost-alt","Warranty & Support","faqs.html")], reverse=True)}
  </div>
</section>""")

    b.append(stat_section([
        ("5","core solution areas"),
        ("18 yr","engineering track record"),
        ("42,000 m\u00b2","factory floor"),
        ("60+","countries served"),
    ]))
    b.append(cta_section(
        "Need a tailored noise barrier solution? Contact Yukings engineering today.",
        "Whether you need a feasibility study for a new highway corridor, acoustic simulation around an industrial plant, or a turnkey solar noise barrier solution, Yukings delivers a fully-engineered answer."))
    b.append(page_close())
    return "".join(b)

def page_projects():
    b=[]
    b.append(page_head(
        "Noise Barrier Projects | Yukings - Railway, Highway, Industrial, Solar, Residential",
        "Selected noise barrier projects by Yukings: high-speed rail, highways, industrial plants, residential communities and solar PV noise barrier installations worldwide.",
        "projects.html"))
    b.append(breadcrumb([("Home","index.html"),("Projects",None)]))
    b.append(hero(
        "Selected noise barrier __SPAN__ from around the world.",
        "projects",
        "A curated selection of Yukings noise barrier projects delivered across five continents - from high-speed rail corridors in Asia to solar noise barrier pilots in Europe, and industrial plant enclosures in the Middle East.",
        "noise-barrier-projects-selection-global",
        chips=["Railway Projects","Highway Projects","Industrial Projects","Solar Projects","Residential Projects"],
        actions=[("primary","View Case Study Dossier","get-quote.html"),("ghost","Request a Reference List","contact.html")],
        stats=[("2,400,000+","m\u00b2 installed"),("60+","countries"),("150+","major projects"),("25 yr","design service life")]))

    # Project categories cards
    proj_cats = [
        ("Railway Noise Barrier Projects","Projects \u00b7 High-speed rail, metro",
         "High-speed rail, metro, light-rail and commuter rail noise barrier projects delivered by Yukings.",
         "Explore railway projects","railway-noise-barrier-projects.html","railway-noise-barrier-projects-high-speed","RAIL"),
        ("Highway Noise Barrier Projects","Projects \u00b7 Expressways & bridges",
         "New-build and retrofit highway sound wall projects across urban ring roads, expressways and bridges.",
         "Explore highway projects","highway-noise-barrier-projects.html","highway-noise-barrier-projects-expressway","HIGHWAY"),
        ("Industrial Noise Control Projects","Projects \u00b7 Plant & energy hubs",
         "Industrial plant perimeter walls, rooftop baffle arrays and machine enclosure noise control projects.",
         "Explore industrial projects","industrial-noise-control-projects.html","industrial-noise-control-projects-plant","INDUSTRIAL"),
        ("Residential Noise Reduction Projects","Projects \u00b7 Communities & schools",
         "Residential community screening walls, school and hospital acoustic protection projects.",
         "Explore residential projects","residential-noise-reduction-projects.html","residential-noise-reduction-projects-community","RESIDENTIAL"),
        ("New Energy Solar Barrier Projects","Projects \u00b7 PV-integrated barriers",
         "Solar PV-integrated noise barrier projects delivering both noise attenuation and clean energy.",
         "Explore solar projects","new-energy-solar-barrier-projects.html","new-energy-solar-barrier-projects-pv","SOLAR"),
    ]
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Project Categories","Browse our project portfolio by industry")}
    <div class="rsb-grid rsb-grid--3" style="grid-template-columns:repeat(3,1fr)">
      {"".join(card(*p) for p in proj_cats)}
    </div>
  </div>
</section>""")

    # Featured case studies
    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Featured Case Studies","A closer look at a few signature projects")}
    {split_block("railway-noise-barrier-project-high-speed-corridor","High-Speed Rail Corridor \u2014 42 km Acoustic Barrier",
                  "Rolling noise and aero-acoustic noise reduction for a 42 km high-speed rail corridor.",
                  ["Project scope: design, supply and site supervision of 42 km of 3.0 m high galvanized steel noise barrier with transparent PC window segments along a 350 km/h high-speed rail line.","Panel: 100 mm deep galvanized steel louvered panel with mineral wool core, H 125 x 125 steel posts at 2.0 m bays. Polycarbonate transparent windows at rail-station-adjacent sections."],
                  ["Client: National railway authority","Scope: Design, manufacture and supervision","Barrier height: 3.0 m standard, up to 5.0 m at sensitive receivers","Insertion loss: up to 38 dB at sensitive receivers"],
                  [("primary","Request Full Case Study","get-quote.html"),("ghost-alt","Railway Projects","railway-noise-barrier-projects.html")])}
    {split_block("highway-noise-barrier-project-urban-expressway","Urban Expressway Sound Wall \u2014 18 km New-Build",
                  "Modular 4.0 m high metal-louvered highway sound wall along an 18 km urban expressway.",
                  ["Project scope: detailed acoustic design, panel fabrication, containerized shipping and site supervision for an 18 km urban expressway noise barrier.","Mixed louvered and transparent panel sections to preserve driver visibility and minimize tunnel effect at interchanges. Full CE technical file and third-party test reports delivered."],
                  ["Client: Municipal highway authority","Scope: CNOSSOS-EU design, fabrication and supervision","Panel type: 80 mm + 100 mm mixed galvanized steel + PC window","Installed length: 18 km"],
                  [("primary","Request Full Case Study","get-quote.html"),("ghost-alt","Highway Projects","highway-noise-barrier-projects.html")], reverse=True)}
    {split_block("industrial-noise-barrier-project-power-plant","Combined-Cycle Power Plant \u2014 Perimeter Acoustic Wall",
                  "12 m high industrial acoustic perimeter wall for a combined-cycle gas turbine power plant.",
                  ["Project scope: structural design, fabrication and installation of a 12 m high heavy-gauge industrial acoustic wall around the turbine hall and auxiliary equipment of a combined-cycle gas turbine (CCGT) power plant.","Panels: 140 mm deep heavy-gauge galvanized steel, mineral wool core, with structural H-beam support system. Wind load engineered to EN 1991-1-4, local seismic code."],
                  ["Client: Independent power producer","Scope: Design, fabrication and turnkey installation","Panel: 140 mm galvanized steel, 12 m height","Rated insertion loss: up to 45 dB"],
                  [("primary","Request Full Case Study","get-quote.html"),("ghost-alt","Industrial Projects","industrial-noise-control-projects.html")])}
    {split_block("solar-noise-barrier-project-pv-highway","Solar PV Noise Barrier Pilot \u2014 2 km Pilot Installation",
                  "2 km bifacial PV-integrated solar noise barrier pilot on an operational highway.",
                  ["Project scope: engineering design of a 2 km bifacial PV-integrated noise barrier pilot on an existing highway, including structural H-post upgrade, bifacial PV module specification and grid-tie inverter design."],
                  ["Client: National highway authority + renewable energy developer","Panel: EN 1793-1 tested absorber + 540 W bifacial PV module","Rated output: ~180 kWh/m per year per linear meter","Grid: Medium-voltage grid-tie with remote monitoring"],
                  [("primary","Request Full Case Study","get-quote.html"),("ghost-alt","Solar Projects","new-energy-solar-barrier-projects.html")], reverse=True)}
  </div>
</section>""")

    b.append(stat_section([
        ("2,400,000+","m\u00b2 of noise barriers installed"),
        ("60+","countries with Yukings projects"),
        ("150+","major projects delivered"),
        ("18 years","of project engineering"),
    ]))
    b.append(cta_section(
        "Looking for a similar noise barrier project? Contact Yukings today.",
        "Whether you are planning a new corridor, a retrofit, or a PV-integrated solar noise barrier, Yukings delivers the full project package - from feasibility to handover."))
    b.append(page_close())
    return "".join(b)

write_page("products.html", page_products())
write_page("solutions.html", page_solutions())
write_page("projects.html", page_projects())
print("pages part 3 (products, solutions, projects) done.")
