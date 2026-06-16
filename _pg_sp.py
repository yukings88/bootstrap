#!/usr/bin/env python3
"""Yukings site generator - pages (part 6): 5 solutions + 5 projects pages."""
import sys
sys.path.insert(0, "/workspace")
from _helpers import *

def make_solution_page(filename, title_short, core_keyword, bg_prompt,
                        hero_h1, lede, stats, chips, overview_paragraph,
                        categories_rows, process_rows, deliverables):
    b=[]
    b.append(page_head(
        f"{title_short} | Yukings Noise Barrier Solutions",
        lede, filename))
    b.append(breadcrumb([("Home","index.html"),("Solutions","solutions.html"),(title_short,None)]))
    b.append(hero(hero_h1, core_keyword, lede, bg_prompt, chips=chips, stats=stats))
    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Solution Overview", f"{title_short} end-to-end")}
    {split_block(bg_prompt, "About This Solution", f"Engineered {title_short.lower()} from feasibility to commissioning.",
                  [overview_paragraph],
                  ["Feasibility study and acoustic simulation","Structural design, AutoCAD and Revit drawings","CNC / roll-formed panel manufacture with ISO 9001 quality","Containerized shipping with full documentation","Site supervision and / or turnkey installation"],
                  [("primary","Request a Free Quotation","get-quote.html"),("ghost-alt","Contact Our Engineers","contact.html")])}
  </div>
</section>""")
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Application Coverage","Where we apply this solution")}
    {specs_table(f"{title_short} - Typical Applications",
                  ["Use Case","Barrier Type","Panel Depth","Typical Insertion Loss"],
                  categories_rows)}
  </div>
</section>""")
    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Our Four-Step Process","From initial enquiry through to commissioning")}
    {specs_table(f"{title_short} - Project Process",
                  ["Stage","Activity","Deliverables","Lead Time"],
                  process_rows)}
  </div>
</section>""")
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Standards & Certifications","Full compliance dossier delivered with every project")}
    {specs_table(f"{title_short} - Standards and Certifications",
                  ["Standard","Area","Coverage"],
                  deliverables)}
  </div>
</section>""")
    b.append(stat_section([
        ("42,000 m2","Yukings factory floor"),
        ("18 yr","engineering track record"),
        ("15 years","structural warranty"),
        ("60+","countries served"),
    ]))
    b.append(cta_section(
        f"Ready to discuss your {title_short} project? Contact Yukings engineering today.",
        f"Contact Yukings for a free {title_short} feasibility overview and project quotation within 24 hours, including preliminary acoustic simulation and structural design guidance."))
    b.append(page_close())
    return "".join(b)

def make_project_page(filename, title_short, core_keyword, bg_prompt,
                       hero_h1, lede, stats, chips, category_rows,
                       featured_cases):
    b=[]
    b.append(page_head(
        f"{title_short} Projects | Yukings - Noise Barrier Project Portfolio",
        lede, filename))
    b.append(breadcrumb([("Home","index.html"),("Projects","projects.html"),(title_short,None)]))
    b.append(hero(hero_h1, core_keyword, lede, bg_prompt, chips=chips, stats=stats))
    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head(f"{title_short} Project Portfolio","Selected case studies delivered by Yukings")}
    {specs_table(f"{title_short} - Selected Projects",
                  ["Project","Location","Client","Highlights"],
                  category_rows)}
  </div>
</section>""")
    # Featured case studies
    sections = ""
    for title, location, client, description in featured_cases:
        sections += f"""<section class="rsb-section">
  <div class="rsb-container">
    <div class="rsb-container">
      <h2 style="font-size:28px;color:#082457;margin-bottom:14px">{title}</h2>
      <p style="color:#E4662A;font-weight:700;margin-bottom:14px">{location} &nbsp;|&nbsp; {client}</p>
      <p style="font-size:15px;color:#4a5568;line-height:1.7;margin-bottom:18px">{description}</p>
    </div>
  </div>
</section>"""
    b.append(sections)
    b.append(stat_section([
        ("2,400,000+","m2 installed"),
        ("60+","countries"),
        ("150+","major projects"),
        ("18 years","engineering track record"),
    ]))
    b.append(cta_section(
        f"Looking for similar {title_short} projects? Contact Yukings today for a free reference dossier.",
        f"Send us your {title_short} project details - our team responds within 24 hours with project guidance, technical overview and a formal quotation."))
    b.append(page_close())
    return "".join(b)

# ---------- SOLUTIONS ----------

s_railway = make_solution_page(
    "railway-noise-reduction.html","Railway Noise Reduction","railway noise reduction",
    "railway-noise-reduction-high-speed-corridor",
    "Railway noise reduction solutions for high-speed rail, metro and __SPAN__ corridors.",
    "End-to-end railway noise reduction solutions covering feasibility study, acoustic simulation, panel design, H-post support system design, containerized delivery and site supervision.",
    [("25-45 dB","insertion loss"),("350 km/h","rated speed"),("2.0-8.0 m","barrier heights"),("25 yr","design service life")],
    ["EN 1793 / 1794","Aerodynamic pulse tested","Elastomeric vibration isolation","CNOSSOS-EU simulation"],
    "Yukings railway noise reduction solutions are engineered for heavy-vibration, high-aerodynamic-pulse rail corridor environments - from high-speed rail through to metro and light-rail transit systems.",
    [
        ["High-speed rail corridor (up to 350 km/h)","Metal-louvered absorption panel","80-140 mm","35-45 dB"],
        ["Metro / light-rail transit lines","Metal-louvered + PC transparent window","80-120 mm","25-35 dB"],
        ["Commuter rail corridors","Louvered absorption + mineral wool core","80-120 mm","25-35 dB"],
        ["Freight rail corridors","Heavy-duty louvered absorption panel","100-140 mm","30-40 dB"],
        ["Railway viaducts / bridges","Bridge-parapet mounted noise barrier","100 mm","30-40 dB"],
    ],
    [
        ["01 \u2014 Enquiry","Client submits project scope, location and drawings","Feasibility note & indicative budget","24 hours"],
        ["02 \u2014 Design Engineering","Acoustic simulation, structural design, CAD/BIM","Full engineering package","10-15 working days"],
        ["03 \u2013 Manufacturing","CNC fabrication, inspection and CE documentation","Standard panels 20 working days, custom-engineered 40 days"],
        ["04 \u2014 Delivery & Commissioning","Containerized shipping, site supervision / turnkey installation","Project-specific, quoted on request"],
    ],
    [
        ["EN 1793-1 / -2 / -5","Acoustic performance","Insertion loss (DL), absorption and insulation"],
        ["EN 1794-1 / -2","Mechanical performance / durability","Impact, wind load, UV resistance, aging"],
        ["EN 1991-1-4","Wind load","Wind load and suction design"],
        ["DIN 4150-2 / 3","Vibration","Railway vibration isolation pad design"],
        ["CE","CE Marking","Full Technical Construction File (TCF) on request"],
        ["ISO 9001 / 14001 / 45001","Factory management","Yukings production facility certified"],
    ])

s_highway = make_solution_page(
    "highway-noise-control.html","Highway Noise Control","highway noise control",
    "highway-noise-control-expressway-ringroad",
    "Highway noise control solutions from feasibility to turnkey __SPAN__.",
    "Highway noise control solutions for expressways, ring roads, interchanges, bridge parapets and tunnels - from initial noise mapping through to turnkey delivery.",
    [("25-42 dB","insertion loss"),("80-140 mm","panel depths"),("2.0-5.0 m","typical heights"),("1.2 kN/m2","wind load")],
    ["EN 1793 / 1794","ASTM E90","Hot-dip galvanized","Powder coat RAL custom"],
    "Yukings delivers highway noise control solutions for new-build highways, retrofit projects and bridge-parapet installations across six continents.",
    [
        ["Urban expressways","Metal-louvered absorption panel","80-140 mm","30-42 dB"],
        ["Intercity highways","Metal-louvered or concrete panel","80-120 mm / 50-120 mm","25-40 dB"],
        ["Ring roads and urban bypasses","Metal-louvered + PC transparent window","80-140 mm","28-38 dB"],
        ["Bridge parapets","Special bridge-parapet noise barrier","80-120 mm","25-35 dB"],
        ["Interchanges and toll plazas","Modular noise barrier","80-140 mm","28-42 dB"],
    ],
    [
        ["01 \u2014 Noise Mapping","CNOSSOS-EU or local noise map with predicted levels","Noise map report","24-hour overview + detailed study on request"],
        ["02 \u2014 Acoustic Design","Insertion loss target, panel type selection, heights and layout","Acoustic report + drawings","7-15 working days"],
        ["03 \u2014 Manufacturing & Delivery","Containerized fabrication and delivery","20-40 working days"],
        ["04 \u2014 Installation","Turnkey installation or site supervision","Project-specific"],
    ],
    [
        ["EN 1793-1 / -2 / -5","Acoustic performance","Insertion loss, absorption and sound insulation"],
        ["EN 1794-1 / -2","Mechanical performance","Impact, wind and durability testing"],
        ["EN 1991-1-4","Wind load","Wind load on noise barriers"],
        ["ASTM E90 / C423","US standards","Laboratory airborne sound transmission loss"],
        ["CE","CE Declaration of Performance","CE DoP with each noise barrier system"],
        ["ISO 9001 / 14001 / 45001","Factory management systems","Yukings Shenzhen factory"],
    ])

s_industrial = make_solution_page(
    "industrial-factory-noise-barriers.html","Industrial Noise Barriers","industrial factory noise barriers",
    "industrial-factory-noise-barriers-power-plant",
    "Industrial perimeter walls and machine enclosures for factories, power stations and energy __SPAN__.",
    "Industrial plant noise barrier solutions delivering heavy-duty perimeter acoustic walls, rooftop absorption baffle arrays and custom machine enclosures for factories, power stations, data centers and energy plants.",
    [("30-45 dB","insertion loss"),("100-180 mm","panel depth"),("12 m","max height"),("C5-M","corrosion rating")],
    ["ISO 12944 C5-M","Class A fire rating","15-year warranty","Heavy-gauge steel"],
    "Yukings industrial noise barrier solutions are engineered for heavy industrial environments including combined-cycle gas turbine (CCGT) power plants, oil and gas facilities, data center cooling systems, pumping stations and manufacturing plants.",
    [
        ["Plant perimeter acoustic walls","Heavy-gauge steel-faced absorption panel","100-180 mm","35-45 dB"],
        ["Power station / CCGT plant","Heavy-duty absorption + mass barrier","120-180 mm","38-45 dB"],
        ["Data center cooling systems","Modular absorption panel","100-140 mm","30-40 dB"],
        ["Rooftop baffle array","Absorption baffle","80-120 mm","15-25 dB (insertion loss) reduction"],
        ["Machine enclosure","Custom modular enclosure","100-180 mm","30-45 dB"],
    ],
    [
        ["01 \u2014 Noise Survey","Plant noise survey and frequency analysis","Noise map + equipment listing","Project-specific"],
        ["02 \u2014 Engineering","Structural + acoustic design with drawing package","CAD / Revit drawings","10-20 working days"],
        ["03 \u2014 Manufacturing","CNC fabrication, quality inspection, containerization","40 working days standard"],
        ["04 \u2014 Installation","Site supervision or turnkey installation","Project-specific"],
    ],
    [
        ["EN 1793-1 / -2 / -5","Acoustic performance","Insertion loss, absorption and insulation"],
        ["EN 1794-1 / -2","Mechanical performance","Impact, wind and durability"],
        ["EN 13501-1","Fire classification","Class A fire rating"],
        ["ISO 12944","Corrosion resistance","C3 to C5-M depending on environment"],
        ["ISO 9001 / 14001 / 45001","Factory management systems","Yukings Shenzhen factory certified"],
    ])

s_residential = make_solution_page(
    "residential-community-noise-protection.html","Residential Community Noise Protection","residential community noise protection",
    "residential-community-noise-protection-housing",
    "Community-friendly noise barriers for housing estates, schools and __SPAN__.",
    "Residential noise protection solutions - community-grade acoustic screening walls with optional green-wall integration, wood-grain or custom RAL finishes.",
    [("20-32 dB","insertion loss"),("2.0-4.0 m","typical heights"),("15 yr","structural warranty"),("Class B-s1,d0","fire rated")],
    ["Community aesthetics","Green-wall integration","Custom RAL / wood-grain","PC transparent windows"],
    "Yukings residential community noise protection solutions are specifically designed for housing estates, schools, kindergartens, universities, hospitals and retirement villages, delivering good acoustic performance while blending into the surrounding environment.",
    [
        ["Housing estate boundary walls","Metal-louvered + mineral wool","80-100 mm","22-32 dB"],
        ["Schools and universities","Metal-louvered + PC transparent window","80-120 mm","20-30 dB"],
        ["Hospitals and healthcare facilities","Residential-grade absorption panel","80-120 mm","22-32 dB"],
        ["Retirement villages and community buildings","Decorative screening + green-wall option","80-120 mm","20-28 dB"],
        ["Road-adjacent residential gardens","Residential decorative noise barrier","80-100 mm","20-30 dB"],
    ],
    [
        ["01 \u2014 Consultation","Initial consultation, site visit, acoustic target","Project brief & acoustic target","24-48 hours"],
        ["02 \u2014 Design & Visualization","Panel selection, heights, finish options, optional green-wall","Concept drawings + indicative budget","10 working days"],
        ["03 \u2014 Manufacturing & Delivery","Fabrication and containerized shipping","20 working days standard"],
        ["04 \u2014 Installation","Turnkey installation or site supervision","Project-specific"],
    ],
    [
        ["EN 1793-1 / -2 / -5","Acoustic performance","Insertion loss, absorption, insulation"],
        ["EN 13501-1","Fire classification","Class B-s1,d0 standard (Class A on request)"],
        ["ISO 12944 C3","Corrosion resistance","Suburban / typical residential"],
        ["CE","CE Marking","CE DoP for EU projects on request"],
        ["ISO 9001 / 14001 / 45001","Factory management","Yukings Shenzhen factory"],
    ])

s_solar = make_solution_page(
    "solar-energy-noise-barrier-solutions.html","Solar Energy Noise Barrier Solutions","solar energy noise barrier solutions",
    "solar-energy-noise-barrier-pv-infrastructure",
    "Noise barriers that turn road traffic noise into clean __SPAN__.",
    "Bifacial PV-integrated solar noise barrier solutions - an infrastructure-as-a-service noise barrier that attenuates highway noise and generates renewable electricity.",
    [("25-35 dB","insertion loss"),("420-540 W","bifacial PV module"),("120-180 kWh/m/yr","electricity output"),("25 yr","PV power warranty")],
    ["EN 1793 tested","IEC 61215 / IEC 61730","25-year linear warranty","Grid-tie ready"],
    "Yukings solar energy noise barrier solutions combine EN 1793-tested acoustic absorption on the road-facing side with a monocrystalline bifacial PV module on the rear. The result is a noise barrier that also generates clean electricity for the highway authority, infrastructure developer or the local grid.",
    [
        ["Highway median solar noise barrier","Bifacial PV-integrated acoustic panel","120-160 mm","25-35 dB"],
        ["Roadside south-facing noise barrier","Bifacial PV + absorption panel","120-160 mm","25-35 dB"],
        ["New-build highway solar noise barrier","Design, procurement and construction","120-160 mm","25-35 dB"],
        ["Retrofit solar noise barrier","H-beam retrofit with PV panel","120 mm","25-32 dB"],
        ["Infrastructure-as-a-service (IaaS)","Build-own-operate-transfer","120-160 mm","25-35 dB"],
    ],
    [
        ["01 \u2014 Feasibility","Site layout, solar resource assessment, CNOSSOS-EU noise map","Feasibility report + indicative budget","Project-specific"],
        ["02 \u2014 EPC Package","Engineering, procurement, construction of solar noise barrier","Full engineering, EPC quotation","15-30 working days"],
        ["03 \u2014 Manufacturing & PV Procurement","Fabrication of panels + PV module procurement","40 working days (custom-engineered)"],
        ["04 \u2014 Commissioning","Grid-tie connection and performance monitoring","Project-specific"],
    ],
    [
        ["EN 1793-1 / -2 / -5","Acoustic performance","Insertion loss, absorption and insulation"],
        ["EN 1794-1 / -2","Mechanical performance","Impact, wind and durability"],
        ["IEC 61215 / IEC 61730","PV module","Module qualification and safety"],
        ["IEC 62548","Inverter / system","Inverter requirements"],
        ["CE","CE Marking","Full TCF on request"],
        ["ISO 9001 / 14001 / 45001","Factory management systems","Yukings Shenzhen facility"],
    ])

# ---------- PROJECTS ----------

p_railway = make_project_page(
    "railway-noise-barrier-projects.html","Railway Noise Barrier","railway noise barrier projects",
    "railway-noise-barrier-projects-high-speed-rail",
    "Selected railway noise barrier projects from Yukings' global __SPAN__ portfolio.",
    "A selection of railway noise barrier projects delivered by Yukings: high-speed rail corridors, metro lines, light-rail transit and commuter rail systems.",
    [("2,400,000+","m2 installed globally"),("60+","countries"),("45 dB","max insertion loss"),("350 km/h","rated speed")],
    ["EN 1793 / EN 1794","High-speed rail","Metro and light rail","Freight rail","Bridge-parapet"],
    [
        ["42 km high-speed rail corridor","Southeast Asia","National railway authority","Noise barrier design, manufacture, supply and site supervision for a 42 km high-speed rail corridor. Metal-louvered 100-140 mm galvanized steel panels on H-posts at 2.0 m and 2.5 m bays. Insertion loss up to 38 dB at sensitive receivers."],
        ["Urban metro line (28 stations)","East Asia","Municipal metro operator","Modular metal-louvered noise barrier panels along 17 km of at-grade metro corridor. Optional transparent polycarbonate windows at station-adjacent sections to maintain passenger visibility."],
        ["Light-rail transit (LRT) line","Middle East","Municipal transit authority","Light-rail transit noise barrier package combining metal-louvered panels with decorative powder-coat finish to match the city architectural palette."],
        ["Commuter rail corridor noise barrier","Europe","National railway","Retrofit noise barrier package along a busy commuter rail corridor with insertion loss up to 32 dB at residential receivers."],
    ],
    [("42 km High-Speed Rail Noise Barrier Package","Southeast Asia","National railway authority","Yukings designed, manufactured, shipped and supervised the installation of a 42 km noise barrier package along a high-speed rail corridor. The barrier includes metal-louvered mineral-wool core absorption panels in 80/100/120/140 mm depths on H 100 x 100 and H 125 x 125 hot-dip galvanized posts at 2.0 m and 2.5 m bays.")])

p_highway = make_project_page(
    "highway-noise-barrier-projects.html","Highway Noise Barrier","highway noise barrier projects",
    "highway-noise-barrier-projects-expressway",
    "Selected highway noise barrier projects from Yukings' global __SPAN__ portfolio.",
    "Selected highway noise barrier projects delivered by Yukings: expressways, ring roads, bridge-parapet retrofits and interchanges.",
    [("18 km","longest single-project run"),("42 dB","insertion loss"),("2.0-2.5 m","bay spacing"),("60+","countries")],
    ["Expressways","Ring roads","Bridges","Interchanges","Tunnels / underpasses"],
    [
        ["18 km urban expressway","East Asia","Municipal highway authority","New-build 18 km metal-louvered highway noise barrier, with mixed transparent polycarbonate window segments to minimize visual tunnel effect on drivers."],
        ["Ring-road retrofits","Europe","Municipal highways","Retrofit highway noise barrier packages along multiple ring-road segments, including non-standard H-post modifications to meet existing foundation constraints."],
        ["Bridge-parapet noise barrier","Middle East","Ministry of transport","Bridge-parapet mounted noise barrier package for multiple intercity bridges, including anti-vibration elastomeric isolation pad for structure-borne noise mitigation."],
        ["Toll plaza and interchange noise barrier","Asia","Toll operator","Noise barrier package around a major toll plaza and interchange including modular metal-louvered panels on curved alignment."],
    ],
    [("18 km Urban Expressway Sound Wall","East Asia","Municipal highway authority","Yukings designed, manufactured and supervised installation of an 18 km urban expressway noise barrier combining metal-louvered absorption panels with transparent polycarbonate windows at sensitive landscape locations. Panels in 80/100/120 mm depths with RAL 7030 powder-coat finish.")])

p_industrial = make_project_page(
    "industrial-noise-control-projects.html","Industrial Noise Control","industrial noise control projects",
    "industrial-noise-control-projects-power-plant",
    "Selected industrial plant noise barrier projects delivered by __SPAN__.",
    "Selected industrial noise barrier case studies: power stations, factories, data centers and oil & gas facilities.",
    [("45 dB","max insertion loss"),("12 m","barrier height"),("60+","countries"),("18 yr","experience")],
    ["CCGT power","Factory","Data center","Oil & gas","Pumping station"],
    [
        ["Combined-cycle gas turbine (CCGT) power plant","Southeast Asia","Independent power producer","12 m high heavy-gauge industrial acoustic perimeter wall around a CCGT power plant, delivering up to 45 dB insertion loss at plant boundary."],
        ["Manufacturing plant perimeter wall","North America","Manufacturing group","Perimeter acoustic wall around a heavy manufacturing facility, including rooftop absorption baffle arrays for internal plant noise control and equipment enclosures for key machinery."],
        ["Data center cooling system noise barrier","Europe","Data center operator","Custom noise barrier package around an air-cooled data center, including modular absorption panels and ventilation-friendly acoustic baffles."],
        ["Oil and gas facility noise package","Middle East","Oil and gas operator","Heavy-duty industrial noise barrier package designed for an oil and gas facility in a C5-M coastal industrial environment."],
    ],
    [("12 m CCGT Power Plant Perimeter Wall","Southeast Asia","Independent power producer","Yukings designed, manufactured and supervised installation of a 12 m high heavy-gauge industrial acoustic perimeter wall around a combined-cycle gas turbine power plant, delivering up to 45 dB insertion loss at residential receivers beyond the plant boundary.")])

p_residential = make_project_page(
    "residential-noise-reduction-projects.html","Residential Noise Reduction","residential noise reduction projects",
    "residential-noise-reduction-projects-community",
    "Selected residential community noise barrier projects delivered by __SPAN__.",
    "Selected residential community noise barrier projects: housing estates, schools, hospitals and community buildings.",
    [("32 dB","max insertion loss"),("2.0-4.0 m","typical heights"),("60+","countries"),("15 yr","structural warranty")],
    ["Housing estates","Schools","Universities","Hospitals","Retirement villages"],
    [
        ["Housing estate perimeter noise wall","Asia","Housing developer","Community-grade noise barrier along a housing estate boundary with custom wood-grain finish on the residential side to blend into the surrounding gardens."],
        ["School playground noise protection","Europe","Municipal school board","Noise barrier along a busy road adjacent to a primary school, combining acoustic absorption panel with transparent polycarbonate windows to maintain natural daylight to the playground."],
        ["University campus acoustic screening","North America","University campus","Campus-wide acoustic screening package along multiple roads, with metal-louvered absorption panels and custom landscape-finish powder-coat colors to match the campus architectural palette."],
        ["Hospital courtyard noise barrier","Australia","Hospital operator","Noise barrier around a hospital courtyard, with a combination of absorption panels and PC transparent windows to maintain natural daylight."],
    ],
    [("Housing Estate Perimeter Acoustic Screening Wall","Asia","Housing developer","Yukings designed, manufactured and supervised installation of a 2.8 km community-grade noise barrier along the perimeter of a major housing estate. The barrier uses metal-louvered absorption panels in 80-100 mm depths with custom wood-grain RAL powder-coat finish on the residential-facing side to blend into the surrounding environment.")])

p_solar = make_project_page(
    "new-energy-solar-barrier-projects.html","New Energy Solar Barrier","new energy solar barrier projects",
    "new-energy-solar-noise-barrier-projects-pv",
    "Selected solar PV-integrated noise barrier projects delivered by __SPAN__.",
    "Selected bifacial PV-integrated solar noise barrier projects delivered by Yukings, generating clean electricity from the rear side of road-traffic noise barriers.",
    [("35 dB","insertion loss"),("120-160 mm","panel depth"),("180 kWh/m/yr","electricity output"),("25 yr","PV linear warranty")],
    ["Highway median","Roadside","New-build highway","Retrofit","IaaS"],
    [
        ["2 km pilot bifacial PV solar noise barrier","Europe","Highway authority + renewables developer","A 2 km pilot solar noise barrier combining EN 1793-tested acoustic absorbers with 540 W bifacial PV modules on the rear side. Yukings delivered engineering design, panel fabrication, shipping and site supervision."],
        ["New-build highway solar noise barrier","Asia","Infrastructure investor","Turnkey solar noise barrier package along a new-build highway. The barrier uses a pre-engineered H-post system with integrated PV mounts and grid-tie string inverters."],
        ["Retrofit solar noise barrier","Australia","State highway authority","Retrofit solar PV panel package added to an existing highway noise barrier. The retrofitted PV panels deliver a net addition of approximately 150 kWh/m/yr per linear meter."],
        ["Median solar noise barrier","Middle East","Infrastructure developer","Median-mounted solar noise barrier along a major intercity highway, with bifacial PV panels facing both directions to maximize albedo-driven bifacial gain."],
    ],
    [("2 km Pilot Bifacial PV Solar Noise Barrier","Europe","Highway authority + renewable energy developer","Yukings designed, manufactured and supervised the installation of a 2 km pilot solar noise barrier combining EN 1793-tested acoustic absorption panels on the road-facing side with bifacial 540 W PV modules on the rear. Grid-tie string inverters connect to the local medium-voltage network. Project estimated output of approximately 180 kWh per linear meter per year depending on site-specific solar irradiance.")])

# Write all files
pages = {
    "railway-noise-reduction.html": s_railway,
    "highway-noise-control.html": s_highway,
    "industrial-factory-noise-barriers.html": s_industrial,
    "residential-community-noise-protection.html": s_residential,
    "solar-energy-noise-barrier-solutions.html": s_solar,
    "railway-noise-barrier-projects.html": p_railway,
    "highway-noise-barrier-projects.html": p_highway,
    "industrial-noise-control-projects.html": p_industrial,
    "residential-noise-reduction-projects.html": p_residential,
    "new-energy-solar-barrier-projects.html": p_solar,
}
for name, html in pages.items():
    write_page(name, html)
print("pages part 6 (5 solutions + 5 projects) done.")
