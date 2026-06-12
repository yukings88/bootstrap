#!/usr/bin/env python3
"""Yukings product page generator for product-02..08.

Reuses /workspace/public/yukings-noise-barrier.css and the shared
public/yukings-noise-barrier.js (no inline styles, no inline scripts).
"""
from pathlib import Path
from urllib.parse import quote

OUT = Path("/workspace")
DOMAIN = "https://yukings.net"
PUBLIC_CSS = "public/yukings-noise-barrier.css"
PUBLIC_JS = "public/yukings-noise-barrier.js"
IMG_API = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
PRODUCTS_ROOT = f"{DOMAIN}/products"
BREADCRUMB_HUB = "Highway Noise Barriers"

# URL slug for every product (1-8), used to build related-product links.
SLUGS = {
    1: "highway-noise-barrier",
    2: "aluminum-noise-barriers",
    3: "louver-noise-barriers",
    4: "arc-top-noise-barriers",
    5: "full-enclosure-noise-barriers",
    6: "pc-transparent-noise-barriers",
    7: "solar-noise-barriers",
    8: "hybrid-noise-barriers",
}


def img(prompt: str, size: str = "landscape_4_3") -> str:
    return f"{IMG_API}?prompt={quote(prompt)}&image_size={size}"


# Common product cards shown in the inquiry form dropdown
PRODUCT_DROPDOWN = """                <option value="">Select product type</option>
                <option value="galvanized">Galvanized Steel Barrier</option>
                <option value="aluminum">Aluminum Barrier</option>
                <option value="pc">PC Transparent Barrier</option>
                <option value="louver">Louver Barrier</option>
                <option value="arc">Arc Top Barrier</option>
                <option value="enclosure">Full Enclosure</option>
                <option value="solar">Solar Barrier</option>
                <option value="hybrid">Hybrid Barrier</option>"""


# All 8 products - product 01 is left untouched (template).
# Each entry contains every piece of product-specific content.
PRODUCTS = {
    2: {
        "slug": "aluminum-noise-barriers",
        "name": "Aluminum Highway Noise Barrier",
        "page_title": "Aluminum Highway Noise Barrier | Yukings",
        "short_name": "Aluminum Highway Barrier",
        "category": "Aluminum Highway Noise Barriers",
        "description": "Lightweight aluminum highway noise barrier with 30-40dB reduction, 60% lighter than steel, ideal for bridges. CE certified Yukings.",
        "og_description": "Lightweight aluminum highway noise barrier. 30-40dB reduction. 60% lighter than steel. Marine-grade corrosion resistance.",
        "twitter_description": "Lightweight aluminum highway noise barrier with 30-40dB reduction, 60% lighter than steel, ideal for bridges. CE certified Yukings.",
        "keywords": "aluminum highway noise barrier, lightweight noise barrier, aluminum sound wall, bridge noise barrier, marine grade noise barrier",
        "og_image": "https://yukings.net/img/og-aluminum-noise-barrier.webp",
        "lead": "Lightweight 5052-H32 aluminum highway noise barrier for bridges and elevated expressways, 30-40dB attenuation, 60% lighter than steel, CE & ISO 9001 certified.",
        "h1": "Aluminum Highway Noise Barrier",
        "h2_why": "Why Lightweight Aluminum Highway Noise Barriers Matter",
        "h2_lead": "Yukings Aluminum Highway Noise Barriers reduce traffic noise by 30-40dB while cutting structural load by 60%, perfect for bridges, elevated highways, and coastal applications.",
        "pain_points": [
            ("⚖️", "Heavy Steel Panel Loads", "Steel barriers weigh 12-18kg/㎡, exceeding structural limits on aging bridges and elevated road decks."),
            ("🌊", "Coastal Corrosion", "Highway corridors near oceans face salt-spray corrosion, halving steel barrier service life to 8-10 years."),
            ("🏗️", "Complex Installation", "Cranes, heavy lifting gear, and lane closures inflate installation cost by 30-40% on elevated sections."),
            ("📏", "Limited Design Flexibility", "Standard sizes rarely fit curved bridge sections or architectural specifications on landmark projects."),
        ],
        "pain_image": img("Photorealistic side view of a long elevated highway bridge with lightweight aluminum noise barriers installed along the deck, coastal background with ocean, golden hour lighting, documentary photography, high resolution"),
        "adv_image": img("Close-up product photograph of a lightweight perforated aluminum highway noise barrier panel standing in clean industrial setting, white background, professional industrial photography, sharp focus, high detail, showcasing metallic aluminum texture and perforations"),
        "values": [
            ("30-40", "dB Reduction", "Noise Attenuation"),
            ("60%", "Lighter", "Vs Steel Panel"),
            ("5052", "H32 Alloy", "Marine Grade"),
            ("25+", "Years", "Service Life"),
            ("5M", "mm Length", "Standard Span"),
        ],
        "specs": [
            ("Material", "5052-H32 Marine-Grade Aluminum Alloy", "-"),
            ("Panel Thickness", "0.8 / 1.0 / 1.2 / 1.5", "mm"),
            ("Panel Length", "5000 (standard, custom up to 8000)", "mm"),
            ("Panel Height", "500 - 4000", "mm"),
            ("Hole Type", "Perforated / Louvered / Solid / Micro-Perforated", "-"),
            ("Perforation Ratio", "20 - 35", "%"),
            ("Surface Treatment", "Anodized / PVDF Coating / Powder Coated / Mill Finish", "-"),
            ("Weight", "60% lighter than equivalent galvanized steel", "-"),
            ("Corrosion Resistance", "Marine-grade, salt-spray tested 3000+ hours", "-"),
            ("Post Style", "H-Beam / I-Beam / C-Channel Aluminum", "-"),
            ("Fire Rating", "Class A (non-combustible)", "-"),
            ("Noise Reduction", "30 - 40", "dB"),
            ("Wind Resistance", "Grade 8 (960 Pa)", "-"),
            ("Temperature Range", "-50 to +80", "°C"),
            ("Service Life", "25 - 30", "Years"),
        ],
        "apps": [
            ("🌉", "Highway Bridges", "Long-span bridges with weight load limits", "#e6f0fa"),
            ("🏗️", "Elevated Roads", "Viaducts and elevated expressway sections", "#f0faeb"),
            ("🌊", "Coastal Highways", "Salt-spray exposed marine environments", "#fff3e6"),
            ("⛰️", "Mountain Roads", "Curved alignments and steep grades", "#fae6f0"),
        ],
        "spec_image": img("Technical engineering blueprint cross-section diagram of a lightweight aluminum highway noise barrier panel with dimension lines, measurements in millimeters, annotations for thickness height width and perforation ratio, clean white background, professional CAD style technical illustration"),
        "apps_image": img("Photorealistic wide panoramic composite of aluminum noise barriers installed in four different scenarios side by side: long-span bridge, elevated highway viaduct, coastal expressway, and mountain tunnel approach, all with realistic aluminum panels installed, daylight photography"),
        "details_image_prompts": [
            "Photorealistic close-up cross-section view of a 5052-H32 marine-grade aluminum noise barrier panel, showing alloy substrate, acoustic mineral wool core, and perforated face, technical industrial photography, clean neutral background, high detail, sharp focus",
            "Photorealistic close-up of a perforated aluminum noise barrier panel with uniform circular holes and acoustic fill visible behind, technical product photography, studio lighting, high detail, sharp focus",
            "Photorealistic engineering close-up of a modular aluminum panel connector joint with H-shaped aluminum post, rubber gasket seal, and stainless steel fasteners, industrial product photography, clean white background, high detail",
        ],
        "details_image_alts": [
            "Aluminum noise barrier panel cross-section",
            "Perforated aluminum panel structure",
            "Aluminum panel connector detail",
        ],
        "details": [
            ("⚖️", "Lightweight 5052 Alloy Construction", "5052-H32 marine-grade aluminum alloy weighs only 4-6kg/㎡, 60% lighter than equivalent galvanized steel. Reduces structural load on bridges and elevated sections by half."),
            ("🔇", "Highway Noise Reduction Barrier with Aluminum Panel", "Multi-layer acoustic core with 30% perforation ratio delivers 30-40dB noise reduction. NRC rating 0.90 ensures superior sound absorption over traditional steel panels."),
            ("🌊", "Marine-Grade Corrosion Resistance", "Salt-spray tested 3000+ hours per ASTM B117. Naturally corrosion-resistant aluminum alloy eliminates paint peeling and rust streaks in coastal highway projects."),
            ("⚡", "Quick Installation System", "Lightweight panels enable 2-person manual installation. Cuts labor cost 30% and installation time 40% compared to heavy steel barriers on elevated highways."),
        ],
        "install_lead": "Two-person crew installation, no heavy cranes required. Modular aluminum design fits curved alignments with minimal tools.",
        "install_steps": [
            ("Aluminum noise barrier foundation", "Foundation Work", "Pour concrete foundations at 2.5m intervals. Lighter aluminum post reduces foundation size 25% vs steel.",
             "Photorealistic construction site showing concrete foundation footings being poured at regular intervals for an aluminum highway noise barrier installation, workers in safety helmets, rebar visible, industrial documentary photography, daylight"),
            ("Aluminum post installation", "Post Installation", "Manually mount aluminum H-beam posts. Vertical alignment tolerance ±1mm. Two-person crew, no crane.",
             "Photorealistic construction scene of lightweight aluminum H-beam posts being installed vertically on concrete footings along a highway, two workers manually aligning posts without crane, industrial documentary photography, daylight"),
            ("Aluminum panel mounting", "Panel Mounting", "Slide aluminum panels between posts using rubber isolation mounts. Lock with stainless fasteners.",
             "Photorealistic two workers manually inserting lightweight aluminum noise barrier panels between H-shaped aluminum posts on a highway construction site, industrial documentary photography, daylight"),
            ("Sealing and inspection", "Sealing & Inspection", "Apply weather sealant at all joints. Final inspection verifies alignment, anchorage, and acoustic seals.",
             "Photorealistic engineer inspecting sealed joints on a completed aluminum highway noise barrier installation, applying weather sealant, clipboard in hand, industrial documentary photography, daylight"),
        ],
        "cert_image": img("Professional certificate wall display showing three official certificates arranged side by side in elegant dark wood frames mounted on a neutral white wall: CE European Conformity certificate for EN 14388 on left, ISO 9001:2015 quality management certificate in center, and ASTM B117 salt-spray corrosion test report on right, all with official red and gold seals, museum quality photography"),
        "certs": [
            ("🇪🇺", "EN 14388", "CE", "European Conformity Certified for road traffic noise reducing devices.", "EU Mandatory Standard"),
            ("🏆", "ISO 9001:2015", "ISO 9001", "Quality Management System ensuring consistent product excellence.", "Since 2008"),
            ("🌊", "ASTM B117", "Marine Grade", "3000+ hour salt-spray tested for marine and coastal highway use.", "Salt-spray Verified"),
            ("🔬", "AASHTO", "AASHTO", "American Association of State Highway and Transportation Officials compliant.", "Highway Standard"),
        ],
        "projects": [
            ("Coastal bridge aluminum noise barrier project", "Bridge", "Hong Kong-Zhuhai Bridge Approach", "Guangdong, China", "12km aluminum noise barrier installation on coastal bridge approach. 35dB noise reduction with 50% weight savings vs steel.",
             img("Photorealistic long-span coastal bridge with lightweight aluminum noise barriers installed along both sides, ocean background, golden hour sunset, architectural photography, high resolution")),
            ("Elevated viaduct aluminum noise barrier project", "Viaduct", "Oslo Elevated Expressway", "Oslo, Norway", "8km lightweight aluminum sound wall on elevated expressway. Reduced deck load 60% and installed in 4 months.",
             img("Photorealistic elevated urban highway viaduct with aluminum noise barriers on both sides, residential buildings below, clear day, architectural photography, high resolution")),
        ],
        "custom_image": img("Photorealistic composite showing customized aluminum noise barriers with curved bridge geometry, special anodized colors like bronze and silver, and architectural patterns installed at distinctive bridge and coastal highway locations, professional architectural photography, daylight"),
        "customs": [
            ("🎨", "Anodized Color Matching", "Full RAL anodized color palette available. PVDF and powder-coat finishes for architectural projects."),
            ("📐", "Custom Curved Geometry", "CNC-formed panels for curved bridge alignments. Custom lengths up to 8000mm and variable heights."),
            ("⚙️", "Engineering Support for Bridge Projects", "Load calculation, structural analysis, CAD drawings, and on-site installation guidance for bridge projects."),
        ],
        "faqs": [
            ("Why choose aluminum for highway noise barriers?", "Aluminum is 60% lighter than steel, naturally corrosion-resistant, and ideal for bridges, elevated highways, and coastal projects. Yukings 5052-H32 alloy delivers 25+ years of service life with minimal maintenance."),
            ("How effective are aluminum noise barriers compared to steel?", "Yukings aluminum noise barriers achieve 30-40dB noise reduction, outperforming standard galvanized steel panels. Multi-layer acoustic core with perforated aluminum face delivers NRC 0.90 ratings."),
            ("Are aluminum noise barriers suitable for coastal environments?", "Yes! 5052-H32 marine-grade aluminum alloy is salt-spray tested 3000+ hours per ASTM B117. Natural oxide layer provides superior corrosion resistance in marine and coastal highway environments."),
            ("What is the minimum order quantity for aluminum barriers?", "Yukings standard MOQ is 100㎡ for aluminum highway noise barriers. For custom sizes, MOQ may be 200㎡. Flexible terms available for first-time buyers and bridge retrofit projects."),
            ("How much weight can aluminum barriers save on bridges?", "Aluminum panels weigh 4-6kg/㎡ versus 12-18kg/㎡ for galvanized steel, reducing structural load 60%. This allows installation on bridges with weight restrictions or retrofit projects without deck reinforcement."),
            ("Can aluminum noise barriers be customized for curved bridges?", "Yes! Yukings offers CNC-formed curved aluminum panels for bridge alignments. Custom radii from 5m to 100m+ supported, with full engineering support including CAD drawings and structural analysis."),
        ],
        "team_title": "24/7 Engineering Support for Aluminum Bridge Projects",
        "team_text": "Our structural and acoustic engineers respond within 24 hours with weight analysis, wind-load calculations, CAD drawings, and on-site installation guidance for your aluminum highway noise barrier project.",
        "related_title": "Related Aluminum Highway Noise Barrier Options",
        "related_lead": "Explore our complete range of related highway noise barrier systems, engineered as complementary solutions to the aluminum highway noise barrier for diverse acoustic and structural requirements.",
        "related": [
            (1, "Galvanized Steel Highway Noise Barrier", "Heavy-duty galvanized steel panel for standard highway projects.",
             img("Close-up product photograph of a galvanized steel highway noise barrier panel with perforated pattern, clean industrial background, professional industrial photography")),
            (3, "Louver Highway Noise Barrier", "Angled louver design for optimal noise reduction with ventilation.",
             img("Close-up product photograph of louver highway noise barrier panels with angled louvers for ventilation, clean industrial photography")),
            (4, "Arc Top Highway Noise Barrier", "Curved profile for enhanced noise diffusion and aesthetic appeal.",
             img("Close-up of arc top highway noise barrier with curved steel frame and transparent PC panel, photorealistic industrial photography")),
            (5, "Full Enclosure Highway Noise Barrier", "Complete noise encapsulation for maximum attenuation.",
             img("Photorealistic full enclosure highway noise barrier tunnel with steel structure and sound-absorbing panels, clean industrial photography")),
        ],
    },
    3: {
        "slug": "louver-noise-barriers",
        "name": "Louver Highway Noise Barrier",
        "page_title": "Louver Highway Noise Barrier | Yukings",
        "short_name": "Louver Highway Barrier",
        "category": "Louver Highway Noise Barriers",
        "description": "Louver highway noise barrier with 20-30dB noise reduction and ventilation design, ideal for tunnels and semi-enclosed areas. CE certified manufacturer Yukings.",
        "og_description": "Louver highway noise barrier. 20-30dB reduction. Airflow control. Tunnel and semi-enclosed applications.",
        "twitter_description": "Louver highway noise barrier with 20-30dB noise reduction and ventilation design, ideal for tunnels and semi-enclosed areas. CE certified manufacturer Yukings.",
        "keywords": "louver highway noise barrier, louvered sound barrier, ventilation noise wall, tunnel noise barrier, semi-enclosed noise barrier",
        "og_image": "https://yukings.net/img/og-louver-noise-barrier.webp",
        "lead": "Louvered highway noise barrier with 20-30dB reduction and 30% airflow design, ideal for tunnels, semi-enclosed sections, and acoustic ventilation. CE & ISO 9001 certified.",
        "h1": "Louver Highway Noise Barrier",
        "h2_why": "Why Louvered Highway Noise Barriers with Ventilation Matter",
        "h2_lead": "Yukings Louver Highway Noise Barriers reduce noise by 20-30dB while preserving natural airflow, ideal for tunnels, depressed road sections, and semi-enclosed highway corridors.",
        "pain_points": [
            ("🌬️", "Trapped Stale Air", "Fully enclosed barriers create stagnant air pockets, raising tunnel temperatures and reducing driver comfort."),
            ("🚗", "Tunnel Noise Build-up", "Closed corridors amplify engine and tire noise by 3-5dB without absorptive louver geometry."),
            ("💧", "Moisture & Condensation", "Solid barrier walls trap humidity, accelerating corrosion of steel posts and reducing service life."),
            ("📉", "Low Visual Quality", "Flat monolithic walls block sight lines and create driver fatigue on long highway corridors."),
        ],
        "pain_image": img("Photorealistic view inside a highway tunnel entrance with louvered noise barriers installed on the side walls, cool blue lighting, documentary photography"),
        "adv_image": img("Close-up product photograph of a louver highway noise barrier panel with angled louvers for ventilation, clean white background, professional industrial photography, sharp focus"),
        "values": [
            ("20-30", "dB Reduction", "Noise Attenuation"),
            ("30%", "Airflow", "Open Louver Ratio"),
            ("30°", "Louver Angle", "Optimal Diffraction"),
            ("25+", "Years", "Service Life"),
            ("60K", "㎡/month", "Production"),
        ],
        "specs": [
            ("Louver Blade", "Q235 Galvanized Steel / 5052 Aluminum", "-"),
            ("Panel Thickness", "80 / 100 / 120", "mm"),
            ("Louver Spacing", "50 / 75 / 100", "mm"),
            ("Panel Height", "500 - 4000", "mm"),
            ("Louver Angle", "20° - 45° (default 30°)", "deg"),
            ("Open Area Ratio", "25 - 35", "%"),
            ("Surface Treatment", "Hot-Dip Galvanized / PVDF / Powder Coating", "-"),
            ("Acoustic Infill", "Mineral Wool / Glass Wool / Rock Wool", "-"),
            ("Post Style", "Upright / Folded-Angle / Top-Arc", "-"),
            ("Fire Rating", "Class A (non-combustible core)", "-"),
            ("Noise Reduction", "20 - 30", "dB"),
            ("Wind Resistance", "Grade 7 (720 Pa)", "-"),
            ("Temperature Range", "-30 to +60", "°C"),
            ("Service Life", "25 - 30", "Years"),
        ],
        "apps": [
            ("🚇", "Highway Tunnels", "Entrance and exit portal louver walls", "#e6f0fa"),
            ("🏞️", "Depressed Roads", "Below-grade highway sections needing airflow", "#f0faeb"),
            ("🌉", "Bridge Approaches", "Ventilated side walls under elevated sections", "#fff3e6"),
            ("🏭", "Industrial Sites", "Acoustic louvers around factories and plants", "#fae6f0"),
        ],
        "spec_image": img("Technical engineering blueprint showing a louver highway noise barrier panel with dimension lines, blade angle, spacing and open area ratio annotations, clean white background, professional CAD style technical illustration"),
        "apps_image": img("Photorealistic panoramic composite of louver highway noise barriers installed in tunnel entrance, depressed highway section, bridge approach, and industrial plant perimeter, daylight photography"),
        "details_image_prompts": [
            "Photorealistic close-up view of horizontal louver blades with acoustic mineral wool infill behind them, technical product photography, clean neutral background, sharp focus",
            "Photorealistic close-up of a single louver blade profile showing 30 degree angled geometry and acoustic backing, industrial product photography, sharp focus, high detail",
            "Photorealistic close-up of a louver panel mounting frame with H-shaped post and security fasteners, industrial product photography, clean white background, high detail",
        ],
        "details_image_alts": [
            "Louver noise barrier panel with acoustic infill",
            "Single louver blade profile detail",
            "Louver panel mounting hardware",
        ],
        "details": [
            ("🌬️", "30% Open Area for Natural Ventilation", "Louver geometry maintains 25-35% open area, allowing free airflow that reduces tunnel temperatures by 6-8°C and prevents humidity build-up in highway corridors."),
            ("🔇", "Highway Noise Reduction with Louver Diffraction", "30° angled blades break up sound waves through diffraction, delivering 20-30dB attenuation. NRC 0.75 absorbs incident energy across 500-4000Hz traffic spectrum."),
            ("💧", "Self-Draining Anti-Condensation Design", "Open louver channels drain rainwater and dissipate moisture, extending steel post life by 40% versus solid walls in coastal and humid highway conditions."),
            ("🪟", "Visual Permeability for Driver Comfort", "30% louver openness preserves sight lines, reducing driver fatigue and improving safety on long monotonous highway stretches."),
        ],
        "install_lead": "Modular louver panels bolt to standard posts, no special tools required. Maintenance-friendly design with replaceable individual blades.",
        "install_steps": [
            ("Louver barrier foundation", "Foundation Work", "Pour concrete foundations at 2m intervals. Posts aligned to ±1mm vertical tolerance.",
             "Photorealistic construction site showing concrete foundation footings being poured at regular intervals for a louver highway noise barrier installation, workers in safety helmets, daylight documentary photography"),
            ("Louver post installation", "Post Installation", "Mount galvanized H-beam posts with anchor bolts. Two-person crew, no crane required for low heights.",
             "Photorealistic construction scene of galvanized H-beam posts being installed vertically on concrete footings along a highway, workers aligning posts, daylight documentary photography"),
            ("Louver panel mounting", "Louver Panel Mounting", "Insert louver panels between posts, fix with security fasteners. Spacer brackets maintain 30° angle.",
             "Photorealistic construction workers installing louver noise barrier panels between H-shaped posts on a highway construction site, daylight industrial documentary photography"),
            ("Sealing and inspection", "Sealing & Inspection", "Apply weather sealant at joints. Final inspection verifies louver alignment and acoustic seals.",
             "Photorealistic engineer inspecting sealed joints on a completed louver highway noise barrier installation, clipboard in hand, daylight industrial documentary photography"),
        ],
        "cert_image": img("Professional certificate wall display showing three official certificates arranged side by side in elegant dark wood frames: CE European Conformity for EN 14388, ISO 9001:2015 quality management, and EN 1794 acoustic test report, museum quality photography"),
        "certs": [
            ("🇪🇺", "EN 14388", "CE", "European Conformity Certified for road traffic noise reducing devices.", "EU Mandatory Standard"),
            ("🏆", "ISO 9001:2015", "ISO 9001", "Quality Management System ensuring consistent product excellence.", "Since 2008"),
            ("🔊", "EN 1794-1", "Acoustic", "Acoustic performance verified to EN 1794 series for highway noise walls.", "Acoustic Verified"),
            ("🔬", "CMA / CNAS", "CMA/CNAS", "Third-party tested for ventilation, acoustic and structural performance.", "Lab Verified"),
        ],
        "projects": [
            ("Tunnel louver noise barrier project", "Tunnel", "Milan M4 Metro Tunnel", "Milan, Italy", "3.5km louver wall installation on tunnel approaches. 25dB reduction with 30% airflow retained for ventilation.",
             img("Photorealistic highway tunnel entrance with louver noise barriers lining the side walls, modern concrete architecture, daylight architectural photography")),
            ("Depressed highway louver project", "Depressed", "Singapore PIE Expressway", "Singapore", "5km louvered noise barrier on depressed PIE section. Reduced noise complaints by 65% while keeping stormwater drainage.",
             img("Photorealistic below-grade depressed highway section with louver noise barriers on both sides, tropical vegetation, daylight architectural photography")),
        ],
        "custom_image": img("Photorealistic composite showing customized louver highway noise barriers with variable blade angles, special RAL colors, and architectural integration at distinctive tunnel and bridge locations, professional architectural photography, daylight"),
        "customs": [
            ("🎨", "RAL Color Matching", "Full RAL palette available. Multi-color louver + frame combinations on request with low MOQ."),
            ("📐", "Custom Louver Angles", "Variable blade angles 20°-45° for site-specific noise mapping. CNC-formed blades for tight tolerances."),
            ("⚙️", "Engineering Support for Tunnel Projects", "Acoustic modeling, airflow CFD, and CAD drawings provided for tunnel approach and depressed section projects."),
        ],
        "faqs": [
            ("Why use louvered highway noise barriers?", "Louver walls reduce noise 20-30dB while preserving 25-35% open area for natural ventilation. Yukings louver panels prevent humidity build-up in tunnels and depressed highway sections."),
            ("What is the airflow rate of louver noise barriers?", "Yukings standard louver panels offer 25-35% open area, with custom ratios up to 45% available. Open area can be specified per project ventilation requirements."),
            ("Are louver noise barriers effective for tunnel entrances?", "Yes! Louvered geometry breaks up standing waves in tunnel portals, reducing echo by 6-10dB versus solid walls. Ventilation also removes 70% of CO2 build-up at peak traffic."),
            ("What is the minimum order quantity for louver barriers?", "Yukings standard MOQ is 100㎡ for louver highway noise barriers. Custom angles or colors may require 200㎡ minimum order quantity."),
            ("How are louver blades maintained?", "Individual louver blades are replaceable without dismantling the entire panel. Annual inspection and panel-by-panel replacement keeps lifecycle cost 30% lower than solid walls."),
            ("Can louver barriers be combined with transparent panels?", "Yes! Yukings offers hybrid louver + PC transparent top sections for noise walls needing daylight penetration and driver visibility."),
        ],
        "team_title": "24/7 Engineering Support for Louver Tunnel Projects",
        "team_text": "Our acoustic and HVAC engineers respond within 24 hours with airflow CFD, acoustic modeling, CAD drawings, and on-site installation guidance for your louver highway noise barrier project.",
        "related_title": "Related Louver Highway Noise Barrier Options",
        "related_lead": "Explore our complete range of related highway noise barrier systems, engineered as complementary solutions to the louver highway noise barrier for diverse acoustic and ventilation requirements.",
        "related": [
            (1, "Galvanized Steel Highway Noise Barrier", "Standard absorptive panel for general highway corridors.",
             img("Close-up product photograph of a galvanized steel highway noise barrier panel with perforated pattern, clean industrial background, professional industrial photography")),
            (2, "Aluminum Highway Noise Barrier", "Lightweight aluminum construction for elevated and bridge sections.",
             img("Close-up product photograph of a lightweight aluminum highway noise barrier panel with perforated pattern, clean white background, professional industrial photography")),
            (4, "Arc Top Highway Noise Barrier", "Curved profile for enhanced noise diffusion and aesthetics.",
             img("Close-up of arc top highway noise barrier with curved steel frame and transparent PC panel, photorealistic industrial photography")),
            (6, "PC Transparent Highway Noise Barrier", "Transparent panel for driver visibility on scenic highways.",
             img("Close-up of PC transparent highway noise barrier panel with clear polycarbonate sheet, clean industrial photography")),
        ],
    },
    4: {
        "slug": "arc-top-noise-barriers",
        "name": "Arc Top Highway Noise Barrier",
        "page_title": "Arc Top Highway Noise Barrier | Yukings",
        "short_name": "Arc Top Highway Barrier",
        "category": "Arc Top Highway Noise Barriers",
        "description": "Arc top highway noise barrier with PC transparent panel, 25-35dB reduction, and aesthetic curved design for landmark highway projects. CE certified Yukings.",
        "og_description": "Arc top highway noise barrier. 25-35dB reduction. PC transparent top panel. Aesthetic curved design for landmark projects.",
        "twitter_description": "Arc top highway noise barrier with PC transparent panel, 25-35dB reduction, and aesthetic curved design for landmark highway projects. CE certified Yukings.",
        "keywords": "arc top highway noise barrier, curved sound barrier, PC transparent panel, aesthetic noise wall, landmark highway barrier",
        "og_image": "https://yukings.net/img/og-arc-top-noise-barrier.webp",
        "lead": "Arc-top highway noise barrier with curved steel frame and PC transparent top panel, 25-35dB attenuation, anti-climb design, ideal for urban and scenic highway projects.",
        "h1": "Arc Top Highway Noise Barrier",
        "h2_why": "Why Arc Top Highway Noise Barriers Combine Form and Function",
        "h2_lead": "Yukings Arc Top Highway Noise Barriers deliver 25-35dB noise reduction with a curved profile that diffuses sound waves, prevents climbing, and enhances urban aesthetics.",
        "pain_points": [
            ("🏙️", "Visual Impact on Cities", "Standard straight-top noise walls create monotonous concrete corridors, lowering property values near urban highways."),
            ("🧗", "Anti-Climb Safety Gaps", "Flat-top barriers provide handholds for trespassers, posing safety and liability risks near pedestrian zones."),
            ("🌳", "Loss of Scenic Views", "Solid noise walls block sight lines to mountains, water, and architecture, hurting tourism and resident wellbeing."),
            ("📢", "Sound Wave Reflection", "Flat surfaces reflect traffic noise upward, missing the receiver zone and creating echo at ground level."),
        ],
        "pain_image": img("Photorealistic urban highway scene with elegant arc top noise barriers, modern city skyline in background, golden hour, documentary photography"),
        "adv_image": img("Close-up of an arc top highway noise barrier with curved steel frame and transparent PC panel, photorealistic industrial photography, sharp focus, high detail"),
        "values": [
            ("25-35", "dB Reduction", "Noise Attenuation"),
            ("88%", "Light Trans.", "PC Top Panel"),
            ("R300", "mm Radius", "Standard Arc"),
            ("25+", "Years", "Service Life"),
            ("Anti", "Climb", "Curved Top"),
        ],
        "specs": [
            ("Curved Frame", "Q235 Hot-Dip Galvanized Steel, CNC-formed", "-"),
            ("Panel Material", "Perforated Steel / Aluminum / PC Transparent", "-"),
            ("Panel Thickness", "80 / 100 / 120", "mm"),
            ("Arc Radius", "R250 / R300 / R400 (custom available)", "mm"),
            ("Panel Height", "500 - 4000 (with arc 3500 effective + 500 arc)", "mm"),
            ("Top Section", "PC Transparent / Acrylic / Tempered Glass", "-"),
            ("Surface Treatment", "Hot-Dip Galvanized / Powder Coating / PVDF", "-"),
            ("Light Transmission", "88 (PC top section)", "%"),
            ("Post Style", "Y-Type / Top-Arc / Dome-Top", "-"),
            ("Acoustic Infill", "Mineral Wool / Glass Wool (50mm-100mm)", "-"),
            ("Noise Reduction", "25 - 35", "dB"),
            ("Wind Resistance", "Grade 8 (960 Pa)", "-"),
            ("Temperature Range", "-30 to +60", "°C"),
            ("Service Life", "25 - 30", "Years"),
        ],
        "apps": [
            ("🏙️", "Urban Highways", "City ring roads and elevated expressways", "#e6f0fa"),
            ("🌄", "Scenic Corridors", "Mountain and coastal highways with views", "#f0faeb"),
            ("🏛️", "Landmark Projects", "Architectural signature walls for plazas", "#fff3e6"),
            ("🏘️", "Residential Districts", "Anti-climb boundary near schools and parks", "#fae6f0"),
        ],
        "spec_image": img("Technical engineering blueprint of an arc top highway noise barrier showing the curved frame geometry, PC top section, dimension lines and arc radius annotation, clean white background, professional CAD style technical illustration"),
        "apps_image": img("Photorealistic panoramic composite of arc top highway noise barriers installed in urban ring road, scenic coastal highway, landmark plaza, and residential district, daylight photography"),
        "details_image_prompts": [
            "Photorealistic close-up cross-section view of an arc top highway noise barrier with curved steel frame, PC transparent top, perforated steel lower panel and mineral wool acoustic core, technical industrial photography, clean background, high detail",
            "Photorealistic close-up of a curved steel arc frame with PC transparent panel mounted on top, studio lighting, sharp focus, high detail, industrial product photography",
            "Photorealistic close-up of an arc top barrier anti-climb curved profile, showing the smooth transition from straight wall to arc, clean white background, high detail industrial product photography",
        ],
        "details_image_alts": [
            "Arc top noise barrier cross-section with PC panel",
            "Curved steel arc frame and PC top",
            "Anti-climb curved profile detail",
        ],
        "details": [
            ("🏛️", "Curved Profile for Architectural Appeal", "CNC-formed R300 arc creates a flowing silhouette that integrates with urban architecture. Pairs with PC transparent top to soften visual mass and enhance streetscape."),
            ("🔇", "Diffraction-Enhanced Noise Reduction", "Curved geometry diffuses sound waves into multiple paths, adding 3-5dB attenuation versus equivalent straight barriers. NRC 0.80 with mineral wool core."),
            ("🧗", "Anti-Climb Smooth Profile", "Continuous arc eliminates handholds, preventing trespassing and improving safety near pedestrian zones, schools, and residential districts."),
            ("🌞", "PC Transparent Top for Daylight", "88% light-transmitting PC panel on arc top section preserves natural light, reducing lighting costs and creating brighter, more open highway corridors."),
        ],
        "install_lead": "Pre-assembled arc modules reduce on-site work. Standard H-beam posts accept Y-type and dome-top variants for flexible installation.",
        "install_steps": [
            ("Arc top barrier foundation", "Foundation Work", "Pour concrete foundations at 2m intervals. Y-type post base requires 1.2m minimum depth.",
             "Photorealistic construction site showing concrete foundation footings being poured at regular intervals for an arc top highway noise barrier, workers in safety helmets, daylight documentary photography"),
            ("Y-type post installation", "Post Installation", "Mount Y-type or dome-top H-beam posts with vertical alignment tolerance ±1mm.",
             "Photorealistic construction scene of Y-type galvanized H-beam posts being installed vertically on concrete footings, workers aligning posts, daylight industrial documentary photography"),
            ("Arc panel and PC mounting", "Panel & PC Mounting", "Bolt curved steel panel modules, then snap-fit PC transparent top arc sections with EPDM gasket seal.",
             "Photorealistic construction workers installing curved arc top steel panels and PC transparent top on a highway construction site, daylight industrial documentary photography"),
            ("Sealing and inspection", "Sealing & Inspection", "Apply weather sealant at all joints. Final inspection verifies arc alignment, PC seal, and acoustic performance.",
             "Photorealistic engineer inspecting sealed joints on a completed arc top highway noise barrier installation, daylight industrial documentary photography"),
        ],
        "cert_image": img("Professional certificate wall display showing three official certificates arranged side by side in elegant dark wood frames: CE European Conformity, ISO 9001:2015, and ISO 14001:2015 environmental management, museum quality photography"),
        "certs": [
            ("🇪🇺", "EN 14388", "CE", "European Conformity Certified for road traffic noise reducing devices.", "EU Mandatory Standard"),
            ("🏆", "ISO 9001:2015", "ISO 9001", "Quality Management System ensuring consistent product excellence.", "Since 2008"),
            ("🌿", "ISO 14001:2015", "ISO 14001", "Environmental Management System for sustainable manufacturing.", "Eco Compliance"),
            ("🔬", "CMA / CNAS", "CMA/CNAS", "Third-party tested for acoustic and structural performance.", "Lab Verified"),
        ],
        "projects": [
            ("Urban arc top barrier project", "Urban Expressway", "Tokyo Metropolitan Expressway", "Tokyo, Japan", "8km arc top noise barrier along central Tokyo expressway. Anti-climb design and PC top reduced noise complaints by 55%.",
             img("Photorealistic Tokyo-style urban elevated expressway with elegant arc top noise barriers and PC transparent top section, modern cityscape, daylight architectural photography")),
            ("Scenic highway arc top project", "Scenic Highway", "California Highway 1 Retrofits", "California, USA", "12km arc top barrier with PC top on scenic Highway 1. Preserved 88% of ocean view, 30dB reduction achieved.",
             img("Photorealistic scenic coastal highway with arc top noise barriers and PC transparent top section overlooking the Pacific Ocean, sunset, architectural photography")),
        ],
        "custom_image": img("Photorealistic composite showing customized arc top highway noise barriers with R400 large radius, special anodized colors, and architectural integration at distinctive urban and scenic highway locations, professional architectural photography"),
        "customs": [
            ("🎨", "Custom RAL Color & PC Tint", "Full RAL palette plus PC tinting options (bronze, blue, grey) for architectural integration."),
            ("📐", "Variable Arc Radius", "Custom CNC-formed arcs from R150 to R800 to match architectural drawings and sight-line studies."),
            ("⚙️", "Engineering Support for Landmark Projects", "3D modeling, sight-line analysis, CAD drawings, and on-site installation guidance for landmark projects."),
        ],
        "faqs": [
            ("What is an arc top noise barrier?", "An arc top noise barrier uses a curved upper section that diffuses sound waves via diffraction, increasing attenuation by 3-5dB versus straight walls. Yukings also adds PC transparent top for daylight and aesthetics."),
            ("How much extra noise reduction does the arc top provide?", "Yukings arc top noise barriers deliver 25-35dB reduction, gaining 3-5dB over equivalent straight walls through curved-surface diffraction. NRC 0.80 with mineral wool acoustic core."),
            ("Are arc top barriers anti-climb?", "Yes! The continuous smooth curve eliminates handholds and footholds, preventing trespassing. Preferred for schools, residential districts, and pedestrian-adjacent highways."),
            ("What is the minimum order quantity for arc top barriers?", "Yukings standard MOQ is 100㎡ for arc top highway noise barriers. Custom radii or PC tints may require 200㎡ minimum order quantity."),
            ("Can arc tops be combined with PC transparent panels?", "Yes! All Yukings arc top barriers support PC transparent top sections, available in clear, bronze, blue, and grey tints with 75-88% light transmission."),
            ("How long does arc top barrier installation take?", "Pre-assembled arc modules install in 1-1.5 days per kilometer. Two-person crew with light crane for arc lift. Detailed installation guides and video tutorials included."),
        ],
        "team_title": "24/7 Engineering Support for Arc Top Landmark Projects",
        "team_text": "Our architectural and acoustic engineers respond within 24 hours with 3D modeling, sight-line analysis, CAD drawings, and on-site installation guidance for your arc top highway noise barrier project.",
        "related_title": "Related Arc Top Highway Noise Barrier Options",
        "related_lead": "Explore our complete range of related highway noise barrier systems, engineered as complementary solutions to the arc top highway noise barrier for diverse acoustic and architectural requirements.",
        "related": [
            (1, "Galvanized Steel Highway Noise Barrier", "Standard absorptive panel for general highway corridors.",
             img("Close-up product photograph of a galvanized steel highway noise barrier panel with perforated pattern, clean industrial background, professional industrial photography")),
            (2, "Aluminum Highway Noise Barrier", "Lightweight aluminum construction for elevated and bridge sections.",
             img("Close-up product photograph of a lightweight aluminum highway noise barrier panel with perforated pattern, clean white background, professional industrial photography")),
            (6, "PC Transparent Highway Noise Barrier", "Full transparent panel for maximum driver visibility.",
             img("Close-up of PC transparent highway noise barrier panel with clear polycarbonate sheet, clean industrial photography")),
            (8, "Hybrid Highway Noise Barrier", "Combined absorptive + reflective hybrid barrier system.",
             img("Photorealistic hybrid highway noise barrier combining reflective steel top with absorptive mineral wool lower panel, clean industrial photography")),
        ],
    },
    5: {
        "slug": "full-enclosure-noise-barriers",
        "name": "Full Enclosure Highway Noise Barrier",
        "page_title": "Full Enclosure Highway Noise Barrier | Yukings",
        "short_name": "Full Enclosure Highway Barrier",
        "category": "Full Enclosure Highway Noise Barriers",
        "description": "Full enclosure highway noise barrier with 35-45dB noise reduction. Complete noise encapsulation for maximum attenuation. Fire-resistant design for tunnel sections and sensitive areas.",
        "og_description": "Full enclosure barrier. 35-45dB reduction. Maximum noise encapsulation. Fire-resistant design.",
        "twitter_description": "Full enclosure highway noise barrier with 35-45dB noise reduction. Complete noise encapsulation for maximum attenuation. Fire-resistant design for tunnel sections and sensitive areas.",
        "keywords": "full enclosure barrier, noise encapsulation, highway tunnel barrier, complete noise control, high attenuation barrier",
        "og_image": "https://yukings.net/img/og-full-enclosure-noise-barrier.webp",
        "lead": "Full enclosure highway noise barrier with 35-45dB attenuation, complete noise encapsulation, fire-resistant design, ideal for hospitals, schools, and tunnel-sensitive zones.",
        "h1": "Full Enclosure Highway Noise Barrier",
        "h2_why": "Why Full Enclosure Highway Noise Barriers Deliver Maximum Attenuation",
        "h2_lead": "Yukings Full Enclosure Highway Noise Barriers enclose the roadway to achieve 35-45dB reduction, the highest in our range, for hospitals, schools, and noise-sensitive urban zones.",
        "pain_points": [
            ("🏥", "Hospital & School Proximity", "Standard barriers cannot reduce noise enough near hospitals, schools, and research labs where 35-45dB attenuation is mandatory."),
            ("🌃", "Dense Urban Canyons", "Reflective walls bounce sound between buildings, amplifying rather than reducing noise in dense downtown corridors."),
            ("🚒", "Fire Safety Compliance", "Tunnel-grade noise enclosures must meet stringent fire ratings while maintaining structural integrity under heat load."),
            ("🌧️", "Weather Ingress", "Open-top enclosures allow rain, snow, and debris to fall on traffic below, creating safety hazards on highways."),
        ],
        "pain_image": img("Photorealistic full enclosure highway noise barrier tunnel over a city street, modern steel and glass structure, daylight architectural photography"),
        "adv_image": img("Photorealistic full enclosure highway noise barrier tunnel with steel structure and sound-absorbing panels, clean industrial photography"),
        "values": [
            ("35-45", "dB Reduction", "Maximum Attenuation"),
            ("Class A", "Fire Rated", "Non-combustible"),
            ("Span 30", "Meters", "Max Section"),
            ("25+", "Years", "Service Life"),
            ("EPDM", "Sealed", "Weather Tight"),
        ],
        "specs": [
            ("Frame Material", "Q355B Welded Steel Truss, Hot-Dip Galvanized", "-"),
            ("Roof Panel", "Perforated Steel / Aluminum / PC Transparent", "-"),
            ("Wall Panel", "100mm - 200mm Composite Acoustic Panel", "-"),
            ("Acoustic Infill", "100mm Rock Wool (128kg/m³)", "-"),
            ("Span", "10 - 30 (modular sections)", "m"),
            ("Clear Height", "5.0 - 7.5 (roadway clearance)", "m"),
            ("Surface Treatment", "Hot-Dip Galvanized / Powder Coating", "-"),
            ("Roof Drainage", "Integrated gutter + downspout", "-"),
            ("Sealing", "EPDM gasket at all panel joints", "-"),
            ("Fire Rating", "Class A (EN 13501-1)", "-"),
            ("Noise Reduction", "35 - 45", "dB"),
            ("Wind Resistance", "Grade 9 (1200 Pa)", "-"),
            ("Temperature Range", "-40 to +70", "°C"),
            ("Service Life", "25 - 30", "Years"),
        ],
        "apps": [
            ("🏥", "Hospital Zones", "Maximum attenuation near medical facilities", "#e6f0fa"),
            ("🏫", "School Districts", "Class A fire rated near educational campuses", "#f0faeb"),
            ("🏙️", "Dense Urban Areas", "Canyon effect mitigation in downtown cores", "#fff3e6"),
            ("🚇", "Tunnel Approaches", "Weather-tight covering for portal sections", "#fae6f0"),
        ],
        "spec_image": img("Technical engineering cross-section blueprint of a full enclosure highway noise barrier showing steel truss, acoustic panels, roof drainage, dimension lines, clean white background, professional CAD style technical illustration"),
        "apps_image": img("Photorealistic panoramic composite of full enclosure highway noise barriers over hospital zone, school district, urban canyon, and tunnel approach, daylight architectural photography"),
        "details_image_prompts": [
            "Photorealistic close-up cross-section view of a full enclosure highway noise barrier with steel truss, 100mm rock wool infill, perforated steel panels and EPDM seals, technical industrial photography, clean background, high detail",
            "Photorealistic close-up of full enclosure roof joint with EPDM gasket seal and integrated drainage gutter, clean white background, industrial product photography, high detail",
            "Photorealistic close-up of a full enclosure truss node showing welded steel structure, hot-dip galvanized coating, and bolted acoustic panel, industrial product photography, clean background, high detail",
        ],
        "details_image_alts": [
            "Full enclosure barrier cross-section with rock wool",
            "Roof joint EPDM seal and gutter detail",
            "Steel truss node with acoustic panel",
        ],
        "details": [
            ("🏥", "35-45dB Maximum Attenuation", "Fully enclosed structure achieves 35-45dB noise reduction, the highest in our range. Verified by EN 1794-2 acoustic testing for hospital, school, and research lab applications."),
            ("🔥", "Class A Fire-Resistant Design", "All structural and acoustic components meet EN 13501-1 Class A non-combustible rating. Rock wool infill has melting point above 1000°C for tunnel safety compliance."),
            ("🌧️", "EPDM Weather-Tight Sealing", "Continuous EPDM gaskets at every panel joint plus integrated roof drainage keep rain, snow, and debris off the roadway. Tested to 1500Pa wind-driven rain resistance."),
            ("🏗️", "Modular 30m Span Sections", "Pre-engineered 10-30m modular truss spans reduce on-site welding. Bolted assembly cuts installation time 50% versus traditional welded enclosures."),
        ],
        "install_lead": "Pre-engineered modular truss sections arrive ready to lift. Bolted assembly, integrated drainage, and weather-tight EPDM seals reduce on-site time by 50%.",
        "install_steps": [
            ("Full enclosure foundation", "Foundation Work", "Pour reinforced concrete foundations for trusses at 10-30m intervals. Anchor bolt set to ±1mm tolerance.",
             "Photorealistic construction site showing reinforced concrete foundations being poured for full enclosure highway noise barrier, workers in safety helmets, daylight documentary photography"),
            ("Truss installation", "Truss Installation", "Lift pre-assembled steel truss sections with crane. Bolt to anchor plates and align vertically.",
             "Photorealistic crane lifting pre-assembled steel truss sections onto anchor plates for a full enclosure noise barrier, workers guiding, daylight industrial documentary photography"),
            ("Acoustic panel mounting", "Acoustic Panel Mounting", "Bolt acoustic wall and roof panels with EPDM gaskets. Verify seal compression at every joint.",
             "Photorealistic construction workers bolting acoustic panels with EPDM gaskets to full enclosure steel truss, daylight industrial documentary photography"),
            ("Sealing and inspection", "Sealing & Inspection", "Apply weather sealant to all joints. Final inspection verifies acoustic performance and weather tightness.",
             "Photorealistic engineer inspecting sealed joints on a completed full enclosure highway noise barrier, daylight industrial documentary photography"),
        ],
        "cert_image": img("Professional certificate wall display showing three official certificates arranged side by side in elegant dark wood frames: CE European Conformity, ISO 9001:2015, and EN 13501-1 fire rating, museum quality photography"),
        "certs": [
            ("🇪🇺", "EN 14388", "CE", "European Conformity Certified for road traffic noise reducing devices.", "EU Mandatory Standard"),
            ("🏆", "ISO 9001:2015", "ISO 9001", "Quality Management System ensuring consistent product excellence.", "Since 2008"),
            ("🔥", "EN 13501-1", "Class A Fire", "Class A non-combustible fire rating for tunnel and urban applications.", "Fire Verified"),
            ("🔬", "CMA / CNAS", "CMA/CNAS", "Third-party tested for acoustic, fire, and structural performance.", "Lab Verified"),
        ],
        "projects": [
            ("Hospital enclosure barrier project", "Hospital Zone", "Beijing Tiantan Hospital Corridor", "Beijing, China", "1.8km full enclosure over hospital-adjacent section. 40dB reduction achieved, EN 13501-1 Class A fire rated.",
             img("Photorealistic full enclosure noise barrier over a hospital-adjacent urban highway, modern steel and glass architecture, daylight architectural photography")),
            ("Tunnel portal enclosure project", "Tunnel Portal", "Madrid M-30 South Tunnel", "Madrid, Spain", "600m full enclosure over tunnel approach. Weather-tight EPDM seals plus integrated drainage keep traffic dry.",
             img("Photorealistic full enclosure noise barrier at a highway tunnel portal, modern steel structure with integrated drainage, daylight architectural photography")),
        ],
        "custom_image": img("Photorealistic composite showing customized full enclosure highway noise barriers with PC transparent roof sections, integrated lighting, and architectural integration at distinctive hospital and urban locations, professional architectural photography"),
        "customs": [
            ("🎨", "RAL Color & Transparent Roof", "Full RAL palette plus PC transparent roof sections for daylight penetration and visual integration."),
            ("📐", "Custom Span & Clearance", "Custom spans 10-50m, custom clear heights 5-9m. Designed per project geometry and roadway clearance requirements."),
            ("⚙️", "Engineering Support for Sensitive Sites", "Acoustic modeling, fire engineering analysis, CAD drawings, and on-site installation guidance for hospital, school, and tunnel projects."),
        ],
        "faqs": [
            ("What is a full enclosure highway noise barrier?", "A full enclosure noise barrier is a tunnel-like structure that completely covers the roadway. Yukings full enclosures achieve 35-45dB reduction, the highest in our range, ideal for hospitals, schools, and dense urban zones."),
            ("How much noise do full enclosure barriers reduce?", "Yukings full enclosure barriers achieve 35-45dB noise reduction. EN 1794-2 verified, with NRC 0.95+ from 100mm rock wool acoustic infill."),
            ("Are full enclosure barriers fire-resistant?", "Yes! All Yukings full enclosure components meet EN 13501-1 Class A non-combustible rating. Rock wool acoustic infill has melting point above 1000°C."),
            ("What is the maximum span of a full enclosure?", "Standard Yukings full enclosure spans 10-30m per modular section. Custom designs up to 50m available for special projects."),
            ("What is the minimum order quantity for full enclosure barriers?", "Yukings full enclosure projects are typically 500㎡+ due to custom engineering. Smaller custom projects are negotiable with engineering review."),
            ("Can full enclosures include transparent roof sections?", "Yes! Yukings offers PC transparent or acrylic roof sections for daylight penetration. Light transmission 75-88% with full acoustic performance retained."),
        ],
        "team_title": "24/7 Engineering Support for Full Enclosure Sensitive Projects",
        "team_text": "Our structural, acoustic, and fire engineers respond within 24 hours with 3D modeling, fire engineering analysis, CAD drawings, and on-site installation guidance for your full enclosure highway noise barrier project.",
        "related_title": "Related Full Enclosure Highway Noise Barrier Options",
        "related_lead": "Explore our complete range of related highway noise barrier systems, engineered as complementary solutions to the full enclosure highway noise barrier for maximum acoustic performance in sensitive zones.",
        "related": [
            (1, "Galvanized Steel Highway Noise Barrier", "Standard absorptive panel for general highway corridors.",
             img("Close-up product photograph of a galvanized steel highway noise barrier panel with perforated pattern, clean industrial background, professional industrial photography")),
            (3, "Louver Highway Noise Barrier", "Ventilated louver design for tunnels and depressed sections.",
             img("Close-up product photograph of louver highway noise barrier panels with angled louvers for ventilation, clean industrial photography")),
            (7, "Solar Highway Noise Barrier", "Integrated solar PV for renewable energy generation.",
             img("Photorealistic solar highway noise barrier with integrated photovoltaic panels on the upper section, clean industrial photography")),
            (8, "Hybrid Highway Noise Barrier", "Combined absorptive + reflective hybrid barrier system.",
             img("Photorealistic hybrid highway noise barrier combining reflective steel top with absorptive mineral wool lower panel, clean industrial photography")),
        ],
    },
    6: {
        "slug": "pc-transparent-noise-barriers",
        "name": "PC Transparent Highway Noise Barrier",
        "page_title": "PC Transparent Highway Noise Barrier | Yukings",
        "short_name": "PC Transparent Highway Barrier",
        "category": "PC Transparent Highway Noise Barriers",
        "description": "PC transparent highway noise barrier with 88% light transmission, 20-30dB noise reduction. Polycarbonate panel for scenic highways. CE certified Yukings.",
        "og_description": "PC transparent highway noise barrier. 88% light transmission. 20-30dB reduction. Polycarbonate scenic panels.",
        "twitter_description": "PC transparent highway noise barrier with 88% light transmission, 20-30dB noise reduction. Polycarbonate panel for scenic highways. CE certified Yukings.",
        "keywords": "PC transparent noise barrier, polycarbonate sound wall, clear highway barrier, scenic noise wall, transparent acoustic panel",
        "og_image": "https://yukings.net/img/og-pc-transparent-noise-barrier.webp",
        "lead": "PC transparent highway noise barrier with 88% light transmission, 20-30dB reduction, UV-protected polycarbonate panels, ideal for scenic highways and urban view preservation.",
        "h1": "PC Transparent Highway Noise Barrier",
        "h2_why": "Why PC Transparent Highway Noise Barriers Preserve Sight Lines",
        "h2_lead": "Yukings PC Transparent Highway Noise Barriers reduce noise 20-30dB while preserving 88% light transmission, ideal for scenic highways, urban views, and architectural integration.",
        "pain_points": [
            ("🌄", "Blocked Scenic Views", "Solid noise walls obstruct mountain, water, and city views, hurting tourism and resident wellbeing along scenic highways."),
            ("🏙️", "Urban Canyon Effect", "Opaque barriers create dark, claustrophobic corridors that lower perceived safety and worsen driver fatigue."),
            ("🏘️", "Property Devaluation", "Homes behind solid noise walls lose 5-10% property value compared to transparent or open-view alternatives."),
            ("🔦", "Higher Lighting Costs", "Solid walls require 24/7 roadway lighting even in daytime, increasing municipal energy costs and light pollution."),
        ],
        "pain_image": img("Photorealistic scenic coastal highway with PC transparent noise barriers overlooking the ocean, golden hour, architectural photography"),
        "adv_image": img("Photorealistic close-up of a PC transparent highway noise barrier with clear polycarbonate panel, clean industrial photography, sharp focus"),
        "values": [
            ("88%", "Light Trans.", "PC Panel"),
            ("20-30", "dB Reduction", "Noise Attenuation"),
            ("UV", "Protected", "10yr Warranty"),
            ("25+", "Years", "Service Life"),
            ("200x", "Stronger", "vs Glass"),
        ],
        "specs": [
            ("Panel Material", "Polycarbonate (PC) UV-protected sheet", "-"),
            ("Panel Thickness", "8 / 10 / 12 / 15", "mm"),
            ("Panel Height", "500 - 3000 (single span)", "mm"),
            ("Light Transmission", "75 - 88 (clear), 50 (bronze), 30 (grey)", "%"),
            ("Impact Strength", "200x stronger than glass, 30x acrylic", "-"),
            ("UV Protection", "Co-extruded UV layer, 10-year warranty", "-"),
            ("Frame Material", "Aluminum Alloy 6063-T5", "-"),
            ("Surface Treatment", "Anodized / PVDF / Powder Coated", "-"),
            ("Acoustic Infill", "Optional 50mm mineral wool back panel", "-"),
            ("Post Style", "H-Beam / I-Beam / Special Clamp Frame", "-"),
            ("Noise Reduction", "20 - 30", "dB"),
            ("Wind Resistance", "Grade 8 (960 Pa)", "-"),
            ("Temperature Range", "-40 to +120", "°C"),
            ("Service Life", "20 - 25", "Years"),
        ],
        "apps": [
            ("🌊", "Scenic Highways", "Coastal and mountain routes with views", "#e6f0fa"),
            ("🏙️", "Urban View Preservation", "City ring roads with architectural integration", "#f0faeb"),
            ("🌳", "Park Adjacent Roads", "Preserve park views and natural light", "#fff3e6"),
            ("🏘️", "Premium Residential", "Maintain property values with sight lines", "#fae6f0"),
        ],
        "spec_image": img("Technical engineering cross-section blueprint of a PC transparent highway noise barrier showing the polycarbonate sheet, aluminum frame, dimension lines and acoustic infill option, clean white background, professional CAD style technical illustration"),
        "apps_image": img("Photorealistic panoramic composite of PC transparent highway noise barriers installed at scenic coastal highway, urban ring road, park edge, and premium residential, daylight architectural photography"),
        "details_image_prompts": [
            "Photorealistic close-up of a clear polycarbonate PC panel with aluminum frame showing 88% light transmission, studio product photography, sharp focus, high detail, clean background",
            "Photorealistic close-up of PC panel UV-protected surface texture and aluminum extrusion profile, technical product photography, clean background, high detail",
            "Photorealistic close-up of PC panel clamp frame joint with EPDM gasket and stainless fasteners, industrial product photography, clean background, high detail",
        ],
        "details_image_alts": [
            "PC transparent panel with aluminum frame",
            "PC panel UV surface and aluminum profile",
            "PC panel clamp frame and gasket",
        ],
        "details": [
            ("🌅", "88% Light Transmission", "Co-extruded UV-protected PC sheet transmits 88% of visible light, preserving scenic views and natural daylight on highways. Available in clear, bronze, and grey tints."),
            ("🔇", "Highway Noise Reduction with PC Panel", "Acoustic PC sheet with optional 50mm mineral wool back panel delivers 20-30dB noise reduction. STC 32 rating verified by EN 1794 acoustic testing."),
            ("💪", "200x Stronger Than Glass", "Polycarbonate panel offers 200x the impact strength of glass and 30x of acrylic, eliminating breakage risk from vehicle impacts, vandalism, or storm debris."),
            ("☀️", "10-Year UV Warranty", "Co-extruded UV protective layer prevents yellowing and embrittlement. Yukings PC panels come with a 10-year warranty against UV degradation."),
        ],
        "install_lead": "Lightweight PC panels enable fast manual installation. Aluminum clamp frame system with EPDM seals ensures weather-tight performance.",
        "install_steps": [
            ("PC barrier foundation", "Foundation Work", "Pour concrete foundations at 2m intervals. Posts aligned to ±1mm vertical tolerance.",
             "Photorealistic construction site showing concrete foundation footings being poured for a PC transparent highway noise barrier, workers in safety helmets, daylight documentary photography"),
            ("Aluminum post installation", "Post Installation", "Mount aluminum H-beam posts with anchor bolts. Two-person crew, no heavy crane required.",
             "Photorealistic construction scene of aluminum H-beam posts being installed vertically on concrete footings, workers aligning posts, daylight industrial documentary photography"),
            ("PC panel mounting", "PC Panel Mounting", "Insert PC panels into aluminum clamp frames. Tighten EPDM-gasketed clamps to specified torque.",
             "Photorealistic construction workers installing PC transparent panels into aluminum clamp frames on a highway, daylight industrial documentary photography"),
            ("Sealing and inspection", "Sealing & Inspection", "Verify EPDM seal compression. Final inspection confirms panel alignment, light transmission, and acoustic seals.",
             "Photorealistic engineer inspecting sealed PC transparent noise barrier installation, daylight industrial documentary photography"),
        ],
        "cert_image": img("Professional certificate wall display showing three official certificates arranged side by side in elegant dark wood frames: CE European Conformity, ISO 9001:2015, and UV protection test report, museum quality photography"),
        "certs": [
            ("🇪🇺", "EN 14388", "CE", "European Conformity Certified for road traffic noise reducing devices.", "EU Mandatory Standard"),
            ("🏆", "ISO 9001:2015", "ISO 9001", "Quality Management System ensuring consistent product excellence.", "Since 2008"),
            ("☀️", "UV Test Report", "10-Year UV", "UV resistance verified per ASTM G154. 10-year warranty against yellowing and embrittlement.", "UV Verified"),
            ("🔬", "CMA / CNAS", "CMA/CNAS", "Third-party tested for acoustic, optical, and structural performance.", "Lab Verified"),
        ],
        "projects": [
            ("Scenic PC barrier project", "Scenic Highway", "Amalfi Coast SS163", "Amalfi, Italy", "4km PC transparent noise barrier on scenic coastal SS163. 88% view preserved, 25dB noise reduction achieved.",
             img("Photorealistic scenic coastal highway with PC transparent noise barriers overlooking the Mediterranean, dramatic cliffs, daylight architectural photography")),
            ("Urban PC barrier project", "Urban View", "Seoul Namsan Circle Road", "Seoul, South Korea", "2.5km PC transparent noise barrier preserving city skyline view. 50% lighter than glass, 30dB reduction achieved.",
             img("Photorealistic urban highway with PC transparent noise barriers and modern city skyline in background, dusk lighting, architectural photography")),
        ],
        "custom_image": img("Photorealistic composite showing customized PC transparent highway noise barriers with bronze tint, anti-glare coating, and architectural integration at distinctive scenic and urban highway locations, professional architectural photography"),
        "customs": [
            ("🎨", "PC Tint & Anti-Glare Options", "Clear, bronze, blue, and grey tints available. Anti-glare matte coating option for high-sun-exposure highways."),
            ("📐", "Custom Panel Sizes", "Custom panel heights 500-3500mm and thicknesses 8-20mm. CNC cut to project geometry."),
            ("⚙️", "Engineering Support for Scenic Projects", "Sight-line analysis, acoustic modeling, CAD drawings, and on-site installation guidance for scenic highway projects."),
        ],
        "faqs": [
            ("What is a PC transparent noise barrier?", "A PC transparent noise barrier uses polycarbonate (PC) sheets with 88% light transmission. Yukings PC barriers reduce noise 20-30dB while preserving scenic views and natural daylight."),
            ("How much light do PC transparent barriers transmit?", "Yukings clear PC panels transmit 88% of visible light. Bronze tint transmits 50%, grey tint 30%. UV-protected with 10-year warranty against yellowing."),
            ("Are PC transparent panels strong enough for highways?", "Yes! Polycarbonate is 200x stronger than glass and 30x stronger than acrylic, withstanding vehicle impacts, vandalism, and storm debris. UL 94 V-0 fire-rated options available."),
            ("How effective are PC noise barriers at reducing sound?", "Yukings PC barriers achieve 20-30dB noise reduction. Optional 50mm mineral wool back panel adds 3-5dB. STC 32 rating verified by EN 1794 acoustic testing."),
            ("What is the minimum order quantity for PC barriers?", "Yukings standard MOQ is 100㎡ for PC transparent highway noise barriers. Custom tints or sizes may require 200㎡ minimum order quantity."),
            ("Can PC panels be combined with absorptive lower sections?", "Yes! Yukings offers hybrid PC top + perforated steel/aluminum lower panel combinations for projects needing maximum noise reduction with view preservation."),
        ],
        "team_title": "24/7 Engineering Support for PC Transparent Scenic Projects",
        "team_text": "Our optical, structural, and acoustic engineers respond within 24 hours with sight-line analysis, UV-weathering data, CAD drawings, and on-site installation guidance for your PC transparent highway noise barrier project.",
        "related_title": "Related PC Transparent Highway Noise Barrier Options",
        "related_lead": "Explore our complete range of related highway noise barrier systems, engineered as complementary solutions to the PC transparent highway noise barrier for diverse acoustic and aesthetic requirements.",
        "related": [
            (1, "Galvanized Steel Highway Noise Barrier", "Standard absorptive panel for general highway corridors.",
             img("Close-up product photograph of a galvanized steel highway noise barrier panel with perforated pattern, clean industrial background, professional industrial photography")),
            (3, "Louver Highway Noise Barrier", "Ventilated louver design for tunnels and depressed sections.",
             img("Close-up product photograph of louver highway noise barrier panels with angled louvers for ventilation, clean industrial photography")),
            (4, "Arc Top Highway Noise Barrier", "Curved profile for enhanced noise diffusion and aesthetics.",
             img("Close-up of arc top highway noise barrier with curved steel frame and transparent PC panel, photorealistic industrial photography")),
            (5, "Full Enclosure Highway Noise Barrier", "Maximum attenuation enclosure for sensitive zones.",
             img("Photorealistic full enclosure highway noise barrier tunnel with steel structure and sound-absorbing panels, clean industrial photography")),
        ],
    },
    7: {
        "slug": "solar-noise-barriers",
        "name": "Solar Highway Noise Barrier",
        "page_title": "Solar Highway Noise Barrier | Yukings",
        "short_name": "Solar Highway Barrier",
        "category": "Solar Highway Noise Barriers",
        "description": "Solar highway noise barrier with integrated photovoltaic panels. 25-35dB noise reduction plus renewable energy generation. Dual-purpose design for sustainable highway infrastructure.",
        "og_description": "Solar highway barrier. Noise reduction + energy generation. 400W/㎡ solar output. Sustainable infrastructure.",
        "twitter_description": "Solar highway noise barrier with integrated photovoltaic panels. 25-35dB noise reduction plus renewable energy generation. Dual-purpose design for sustainable highway infrastructure.",
        "keywords": "solar noise barrier, photovoltaic highway barrier, solar acoustic barrier, renewable energy barrier, solar panel sound wall",
        "og_image": "https://yukings.net/img/og-solar-noise-barrier.webp",
        "lead": "Solar highway noise barrier with integrated photovoltaic panels, 25-35dB noise reduction plus 400W/㎡ renewable energy generation, dual-purpose sustainable highway infrastructure.",
        "h1": "Solar Highway Noise Barrier",
        "h2_why": "Why Solar Highway Noise Barriers Turn Walls into Power Plants",
        "h2_lead": "Yukings Solar Highway Noise Barriers reduce noise 25-35dB while generating 400W/㎡ of clean solar energy, turning passive infrastructure into active renewable energy assets.",
        "pain_points": [
            ("⚡", "Underutilized Right-of-Way", "Highway corridors offer prime solar exposure but traditional noise walls waste this potential asset, generating zero energy."),
            ("🌱", "Sustainability Mandates", "Government infrastructure projects now require renewable energy integration, but separate solar farms consume additional land."),
            ("💰", "High Carbon Tax", "Conventional noise walls contribute embodied carbon and ongoing emissions, exposing projects to rising carbon taxes."),
            ("🛣️", "Land Use Conflicts", "Solar farms compete with agriculture and ecology for land, but solar-integrated noise walls use existing highway right-of-way."),
        ],
        "pain_image": img("Photorealistic solar highway noise barrier with integrated photovoltaic panels along a modern highway, clear blue sky, daylight architectural photography"),
        "adv_image": img("Photorealistic solar highway noise barrier with integrated photovoltaic panels on the upper section, clean industrial photography"),
        "values": [
            ("25-35", "dB Reduction", "Noise Attenuation"),
            ("400W", "Per ㎡", "Solar Output"),
            ("25yr", "PV Warranty", "Linear Power"),
            ("25+", "Years", "Barrier Life"),
            ("BIPV", "Certified", "Building-Integrated"),
        ],
        "specs": [
            ("PV Module", "Mono-crystalline silicon 400Wp", "-"),
            ("Module Efficiency", "20.5 - 21.5", "%"),
            ("Panel Material", "Q235 Galvanized Steel + Aluminum Frame", "-"),
            ("Panel Thickness", "100 / 120 / 150", "mm"),
            ("Panel Height", "500 - 4000", "mm"),
            ("Power Output", "400 (per ㎡ under STC)", "Wp/㎡"),
            ("Annual Yield", "480 - 560 (per ㎡, sunny region)", "kWh/㎡"),
            ("Inverter", "String inverter (centralized) included", "-"),
            ("Surface Treatment", "Hot-Dip Galvanized / Anodized Aluminum", "-"),
            ("Acoustic Infill", "Mineral Wool / Glass Wool", "-"),
            ("Noise Reduction", "25 - 35", "dB"),
            ("Wind Resistance", "Grade 8 (960 Pa)", "-"),
            ("Temperature Range", "-30 to +70", "°C"),
            ("Service Life", "25 - 30", "Years"),
        ],
        "apps": [
            ("🛣️", "Solar Highways", "Government sustainable infrastructure projects", "#e6f0fa"),
            ("🏭", "Industrial Solar Corridors", "Factory perimeter walls with energy generation", "#f0faeb"),
            ("🌞", "Sunny Region Networks", "Mediterranean, Middle East, and Australian highways", "#fff3e6"),
            ("🏘️", "Net-Zero Communities", "Residential districts with renewable energy targets", "#fae6f0"),
        ],
        "spec_image": img("Technical engineering cross-section blueprint of a solar highway noise barrier showing PV module, galvanized steel frame, acoustic infill, dimension lines and electrical conduit, clean white background, professional CAD style technical illustration"),
        "apps_image": img("Photorealistic panoramic composite of solar highway noise barriers installed at solar highway, industrial corridor, sunny region network, and net-zero community, daylight architectural photography"),
        "details_image_prompts": [
            "Photorealistic close-up of integrated solar PV module on highway noise barrier frame, mono-crystalline cells visible, technical industrial photography, clean background, high detail",
            "Photorealistic close-up of solar noise barrier cable management and junction box on the back, industrial product photography, clean white background, high detail",
            "Photorealistic close-up of solar noise barrier mounting bracket and clamp system, industrial product photography, clean background, high detail",
        ],
        "details_image_alts": [
            "Solar PV module on noise barrier frame",
            "Solar barrier cable management and junction",
            "Solar barrier mounting bracket detail",
        ],
        "details": [
            ("☀️", "400W/㎡ Solar Generation", "Mono-crystalline PV modules generate 400W per square meter under STC, producing 480-560kWh/㎡ annually in sunny regions. Dual-purpose design turns noise walls into income-generating assets."),
            ("🔇", "25-35dB Highway Noise Reduction", "Acoustic mineral wool core with perforated steel/aluminum face delivers 25-35dB noise reduction. PV modules add mass without sacrificing acoustic performance."),
            ("⚙️", "BIPV Certified Integration", "Building-Integrated Photovoltaic (BIPV) certified design. Junction boxes, cabling, and inverters integrated into barrier structure. Plug-and-play string inverter connection."),
            ("📅", "25-Year Linear Power Warranty", "PV modules come with 25-year linear power output warranty. Barrier structure warranted 25+ years against corrosion and structural failure."),
        ],
        "install_lead": "Standard noise barrier installation plus certified PV electrical connection. Turnkey delivery includes modules, inverters, and grid-tie certification.",
        "install_steps": [
            ("Solar barrier foundation", "Foundation Work", "Pour concrete foundations at 2m intervals. Conduit for DC cabling pre-installed.",
             "Photorealistic construction site showing concrete foundation footings being poured for a solar highway noise barrier, workers in safety helmets, daylight documentary photography"),
            ("Post & frame installation", "Post & Frame Installation", "Mount galvanized H-beam posts with integrated cable tray. Bolt PV-ready frames to posts.",
             "Photorealistic construction scene of galvanized H-beam posts with integrated cable tray being installed for a solar highway noise barrier, daylight industrial documentary photography"),
            ("Acoustic + PV mounting", "Acoustic + PV Mounting", "Mount acoustic panels, then install PV modules on top frame. Connect DC cabling to junction boxes.",
             "Photorealistic construction workers installing acoustic panels and photovoltaic modules on a solar highway noise barrier, daylight industrial documentary photography"),
            ("Electrical commissioning", "Electrical Commissioning", "Connect string inverters, perform IV curve test, and submit grid-tie certification paperwork.",
             "Photorealistic certified electrician commissioning solar highway noise barrier with string inverter, daylight industrial documentary photography"),
        ],
        "cert_image": img("Professional certificate wall display showing three official certificates arranged side by side in elegant dark wood frames: CE European Conformity, ISO 9001:2015, and IEC 61215 PV module certification, museum quality photography"),
        "certs": [
            ("🇪🇺", "EN 14388", "CE", "European Conformity Certified for road traffic noise reducing devices.", "EU Mandatory Standard"),
            ("🏆", "ISO 9001:2015", "ISO 9001", "Quality Management System ensuring consistent product excellence.", "Since 2008"),
            ("☀️", "IEC 61215", "PV Module", "Crystalline silicon PV module design qualification. 25-year linear power warranty.", "PV Certified"),
            ("🔬", "CMA / CNAS", "CMA/CNAS", "Third-party tested for acoustic, electrical, and structural performance.", "Lab Verified"),
        ],
        "projects": [
            ("Solar highway barrier project", "Solar Highway", "Saudi Arabia Riyadh Solar Highway", "Riyadh, Saudi Arabia", "5km solar-integrated noise barrier generating 2.4MWp. 30dB noise reduction plus grid-tied solar power for highway lighting.",
             img("Photorealistic solar highway noise barrier with integrated photovoltaic panels along a desert highway, clear blue sky, golden hour architectural photography")),
            ("Industrial solar barrier project", "Industrial", "UAE Industrial Corridor", "Dubai, UAE", "3km solar barrier perimeter around industrial zone. 1.4MWp solar generation, sustainable infrastructure showcase.",
             img("Photorealistic solar noise barrier perimeter around industrial facility, modern architecture, golden hour, architectural photography")),
        ],
        "custom_image": img("Photorealistic composite showing customized solar highway noise barriers with high-efficiency PV modules, integrated lighting, and architectural integration at distinctive solar highway and industrial corridor locations, professional architectural photography"),
        "customs": [
            ("☀️", "PV Module Wattage", "Standard 400Wp with options up to 600Wp bifacial modules. Mono and poly-crystalline choices."),
            ("📐", "Custom Layout & Angle", "Custom panel heights, PV tilt angles, and orientations to maximize yield per site sun-path study."),
            ("⚙️", "Engineering Support for Solar Projects", "Solar yield modeling, grid-tie certification, CAD drawings, and on-site installation guidance for solar highway projects."),
        ],
        "faqs": [
            ("What is a solar highway noise barrier?", "A solar noise barrier integrates photovoltaic (PV) modules into the noise wall structure, generating renewable energy while reducing traffic noise. Yukings solar barriers deliver 25-35dB reduction plus 400W/㎡ of solar power."),
            ("How much electricity can a solar noise barrier generate?", "Yukings solar barriers produce 400W per square meter under STC, equivalent to 480-560kWh/㎡ annually in sunny regions. A 1km stretch at 4m height can generate 2-3MWp of solar capacity."),
            ("Do solar noise barriers reduce noise as well as regular walls?", "Yes! Yukings solar barriers achieve 25-35dB noise reduction with NRC 0.80+ acoustic core. PV modules add mass without compromising acoustic performance."),
            ("What is the warranty on the solar panels?", "Yukings PV modules come with 25-year linear power output warranty, plus 10-year product warranty. The barrier structure itself is warranted 25+ years against corrosion."),
            ("Are solar noise barriers more expensive than regular walls?", "Initial cost is 30-50% higher than standard noise walls, but the solar generation creates a 6-10 year payback through energy sales or self-consumption savings. Yukings provides full ROI modeling."),
            ("Can solar noise barriers be grid-tied?", "Yes! Yukings solar barriers include string inverters and full grid-tie certification. We handle the paperwork for utility interconnection in most jurisdictions."),
        ],
        "team_title": "24/7 Engineering Support for Solar Highway Projects",
        "team_text": "Our solar, electrical, and structural engineers respond within 24 hours with yield modeling, grid-tie paperwork, CAD drawings, and on-site installation guidance for your solar highway noise barrier project.",
        "related_title": "Related Solar Highway Noise Barrier Options",
        "related_lead": "Explore our complete range of related highway noise barrier systems, engineered as complementary solutions to the solar highway noise barrier for sustainable dual-purpose infrastructure.",
        "related": [
            (1, "Galvanized Steel Highway Noise Barrier", "Standard absorptive panel for general highway corridors.",
             img("Close-up product photograph of a galvanized steel highway noise barrier panel with perforated pattern, clean industrial background, professional industrial photography")),
            (4, "Arc Top Highway Noise Barrier", "Curved profile for enhanced noise diffusion and aesthetics.",
             img("Close-up of arc top highway noise barrier with curved steel frame and transparent PC panel, photorealistic industrial photography")),
            (5, "Full Enclosure Highway Noise Barrier", "Maximum attenuation enclosure for sensitive zones.",
             img("Photorealistic full enclosure highway noise barrier tunnel with steel structure and sound-absorbing panels, clean industrial photography")),
            (8, "Hybrid Highway Noise Barrier", "Combined absorptive + reflective hybrid barrier system.",
             img("Photorealistic hybrid highway noise barrier combining reflective steel top with absorptive mineral wool lower panel, clean industrial photography")),
        ],
    },
    8: {
        "slug": "hybrid-noise-barriers",
        "name": "Hybrid Highway Noise Barrier",
        "page_title": "Hybrid Highway Noise Barrier | Yukings",
        "short_name": "Hybrid Highway Barrier",
        "category": "Hybrid Highway Noise Barriers",
        "description": "Hybrid highway noise barrier combining absorptive and reflective panels. 28-40dB noise reduction. Steel frame with multiple material facing options. Optimized cost-performance balance.",
        "og_description": "Hybrid highway barrier. 28-40dB reduction. Absorptive + reflective combination. Optimized cost-performance.",
        "twitter_description": "Hybrid highway noise barrier combining absorptive and reflective panels. 28-40dB noise reduction. Steel frame with multiple material facing options. Optimized cost-performance balance.",
        "keywords": "hybrid noise barrier, composite highway barrier, absorptive reflective barrier, multi-material sound barrier, steel acoustic wall",
        "og_image": "https://yukings.net/img/og-hybrid-noise-barrier.webp",
        "lead": "Hybrid highway noise barrier combining absorptive and reflective panels, 28-40dB reduction, optimized cost-performance balance for mainstream highway projects.",
        "h1": "Hybrid Highway Noise Barrier",
        "h2_why": "Why Hybrid Highway Noise Barriers Optimize Cost and Performance",
        "h2_lead": "Yukings Hybrid Highway Noise Barriers combine absorptive and reflective panels to deliver 28-40dB reduction at 15-20% lower cost than full absorptive systems, the optimal cost-performance balance.",
        "pain_points": [
            ("💸", "Premium Cost of Full Absorptive", "All-absorptive noise walls cost 25-40% more than hybrid alternatives, exceeding budget for mainstream highway projects."),
            ("📊", "Unbalanced Performance", "Pure reflective walls underperform near receivers; pure absorptive walls waste budget on the upper section where diffracted sound dominates."),
            ("🌡️", "Thermal Reflection Issues", "Solid reflective walls can re-radiate absorbed heat, creating thermal hotspots near sensitive receivers in hot climates."),
            ("🛠️", "Complex Maintenance", "Single-material walls require full panel replacement for any localized damage, multiplying lifecycle cost."),
        ],
        "pain_image": img("Photorealistic hybrid highway noise barrier combining reflective steel top and absorptive mineral wool lower panel, clean industrial photography"),
        "adv_image": img("Photorealistic close-up of hybrid highway noise barrier combining reflective steel top and absorptive mineral wool lower panel, clean industrial photography, sharp focus"),
        "values": [
            ("28-40", "dB Reduction", "Hybrid Attenuation"),
            ("-15%", "Cost", "vs Full Absorptive"),
            ("Q355B", "Steel Frame", "Heavy Duty"),
            ("25+", "Years", "Service Life"),
            ("3-in-1", "Design", "Reflect+Absorb+Frame"),
        ],
        "specs": [
            ("Frame", "Q355B Hot-Dip Galvanized Steel", "-"),
            ("Reflective Panel", "Solid Galvanized Steel / Aluminum", "-"),
            ("Absorptive Panel", "Perforated Steel + 50mm Mineral Wool", "-"),
            ("Panel Thickness", "80 / 100 / 120", "mm"),
            ("Panel Height", "500 - 4000", "mm"),
            ("Configuration", "Reflective top + Absorptive bottom (default)", "-"),
            ("Mineral Wool Density", "64 - 128 (acoustic core)", "kg/m³"),
            ("Surface Treatment", "Hot-Dip Galvanized / Powder Coating / PVDF", "-"),
            ("Perforation Ratio", "20 - 35 (absorptive section)", "%"),
            ("Post Style", "H-Beam / I-Beam / C-Channel", "-"),
            ("Noise Reduction", "28 - 40", "dB"),
            ("Wind Resistance", "Grade 8 (960 Pa)", "-"),
            ("Temperature Range", "-30 to +60", "°C"),
            ("Service Life", "25 - 30", "Years"),
        ],
        "apps": [
            ("🛣️", "Mainstream Highways", "Cost-effective solution for typical highway projects", "#e6f0fa"),
            ("🏘️", "Suburban Roads", "Balanced performance near residential areas", "#f0faeb"),
            ("🏗️", "Retrofit Projects", "Upgrading existing walls with hybrid panels", "#fff3e6"),
            ("🌍", "Multi-Climate Networks", "Hot and cold climate highway networks", "#fae6f0"),
        ],
        "spec_image": img("Technical engineering cross-section blueprint of a hybrid highway noise barrier showing reflective steel top, absorptive mineral wool bottom, dimension lines and configuration details, clean white background, professional CAD style technical illustration"),
        "apps_image": img("Photorealistic panoramic composite of hybrid highway noise barriers installed at mainstream highway, suburban road, retrofit project, and multi-climate network, daylight architectural photography"),
        "details_image_prompts": [
            "Photorealistic close-up cross-section of hybrid highway noise barrier showing reflective steel top panel, absorptive perforated steel lower panel with mineral wool core, technical industrial photography, clean background, high detail",
            "Photorealistic close-up of hybrid barrier joint between reflective top and absorptive bottom panels, showing clean transition, industrial product photography, clean white background, high detail",
            "Photorealistic close-up of hybrid barrier perforated steel absorptive panel with mineral wool visible behind, industrial product photography, clean background, high detail",
        ],
        "details_image_alts": [
            "Hybrid barrier cross-section reflective+absorptive",
            "Hybrid barrier reflective to absorptive joint",
            "Hybrid barrier perforated absorptive panel",
        ],
        "details": [
            ("💰", "15% Lower Cost than Full Absorptive", "Hybrid configuration places absorptive material only where it matters most (lower section near receivers), reducing material cost 15-20% with equivalent acoustic performance."),
            ("🔇", "28-40dB Balanced Attenuation", "Reflective top panel diffracts and breaks up high-frequency sound; absorptive bottom panel captures low-frequency traffic noise. Combined 28-40dB reduction at receiver."),
            ("🌡️", "Reduced Thermal Re-radiation", "Hybrid design limits reflective surface area, reducing heat re-radiation by 30% in hot climates and improving thermal comfort for nearby receivers."),
            ("🛠️", "Modular Section Replacement", "Reflective and absorptive sections are independently replaceable. Localized damage only requires replacing the affected section, cutting lifecycle cost 40%."),
        ],
        "install_lead": "Standard post + modular panel system. Reflective and absorptive sections pre-assembled off-site for fast installation.",
        "install_steps": [
            ("Hybrid barrier foundation", "Foundation Work", "Pour concrete foundations at 2m intervals. Posts aligned to ±1mm vertical tolerance.",
             "Photorealistic construction site showing concrete foundation footings being poured for a hybrid highway noise barrier, workers in safety helmets, daylight documentary photography"),
            ("Post installation", "Post Installation", "Mount galvanized H-beam posts with anchor bolts. Two-person crew with light crane.",
             "Photorealistic construction scene of galvanized H-beam posts being installed vertically on concrete footings for a hybrid highway noise barrier, daylight industrial documentary photography"),
            ("Panel mounting", "Panel Mounting", "Install reflective top panels first, then slide absorptive bottom panels between posts. Lock with security fasteners.",
             "Photorealistic construction workers installing reflective top and absorptive bottom panels on a hybrid highway noise barrier, daylight industrial documentary photography"),
            ("Sealing and inspection", "Sealing & Inspection", "Apply weather sealant at all joints. Final inspection verifies reflective-absorptive transition and acoustic seals.",
             "Photorealistic engineer inspecting sealed joints on a completed hybrid highway noise barrier installation, daylight industrial documentary photography"),
        ],
        "cert_image": img("Professional certificate wall display showing three official certificates arranged side by side in elegant dark wood frames: CE European Conformity, ISO 9001:2015, and ISO 14001:2015 environmental management, museum quality photography"),
        "certs": [
            ("🇪🇺", "EN 14388", "CE", "European Conformity Certified for road traffic noise reducing devices.", "EU Mandatory Standard"),
            ("🏆", "ISO 9001:2015", "ISO 9001", "Quality Management System ensuring consistent product excellence.", "Since 2008"),
            ("🌿", "ISO 14001:2015", "ISO 14001", "Environmental Management System for sustainable manufacturing.", "Eco Compliance"),
            ("🔬", "CMA / CNAS", "CMA/CNAS", "Third-party tested for acoustic and structural performance.", "Lab Verified"),
        ],
        "projects": [
            ("Mainstream hybrid barrier project", "Mainstream Highway", "Bangkok Outer Ring Road", "Bangkok, Thailand", "12km hybrid noise barrier along Bangkok outer ring road. 32dB reduction achieved at 18% lower cost than full absorptive design.",
             img("Photorealistic hybrid highway noise barrier along a busy urban ring road, tropical setting, daylight architectural photography")),
            ("Retrofit hybrid barrier project", "Retrofit", "Toronto QEW Retrofit", "Ontario, Canada", "8km hybrid barrier retrofit upgrading existing reflective walls with absorptive lower panels. 25dB additional reduction, 40% lifecycle cost saving.",
             img("Photorealistic hybrid highway noise barrier retrofit project with reflective top and absorptive lower panel, cool climate highway, daylight architectural photography")),
        ],
        "custom_image": img("Photorealistic composite showing customized hybrid highway noise barriers with variable reflective/absorptive ratios, RAL color matching, and architectural integration at distinctive mainstream and retrofit highway locations, professional architectural photography"),
        "customs": [
            ("🎨", "Reflective/Absorptive Ratio", "Custom 30/70 to 70/30 reflective/absorptive ratio based on project acoustic study. Single-material or mixed frame options."),
            ("📐", "Custom Configuration", "Reflective top, absorptive middle, or full-height absorptive — choose configuration per site acoustic model and budget."),
            ("⚙️", "Engineering Support for Retrofit Projects", "Acoustic modeling, existing wall audit, CAD drawings, and on-site installation guidance for retrofit and mainstream projects."),
        ],
        "faqs": [
            ("What is a hybrid highway noise barrier?", "A hybrid noise barrier combines reflective (solid) and absorptive (perforated + mineral wool) panels in one structure. Yukings hybrid barriers deliver 28-40dB reduction at 15-20% lower cost than full absorptive systems."),
            ("How much do hybrid noise barriers cost compared to full absorptive?", "Yukings hybrid barriers cost 15-20% less than full absorptive systems with equivalent acoustic performance. Material savings come from using absorptive material only where it matters most."),
            ("Are hybrid barriers as effective as full absorptive walls?", "Yes! Yukings hybrid barriers deliver 28-40dB reduction, comparable to full absorptive systems. EN 1794-2 verified. The combination of reflective top and absorptive bottom captures both diffracted and direct sound."),
            ("What is the minimum order quantity for hybrid barriers?", "Yukings standard MOQ is 100㎡ for hybrid highway noise barriers. Custom ratios may require 200㎡ minimum order quantity."),
            ("Can hybrid barriers be used for retrofit projects?", "Yes! Hybrid barriers are ideal for retrofitting existing reflective walls. Adding an absorptive lower section to existing reflective walls adds 10-15dB reduction at minimal cost."),
            ("How long does hybrid barrier installation take?", "Standard installation takes 1-1.5 days per kilometer. Pre-assembled reflective and absorptive sections reduce on-site time 30% compared to single-material walls."),
        ],
        "team_title": "24/7 Engineering Support for Hybrid Mainstream Projects",
        "team_text": "Our acoustic and structural engineers respond within 24 hours with cost-performance modeling, acoustic simulations, CAD drawings, and on-site installation guidance for your hybrid highway noise barrier project.",
        "related_title": "Related Hybrid Highway Noise Barrier Options",
        "related_lead": "Explore our complete range of related highway noise barrier systems, engineered as complementary solutions to the hybrid highway noise barrier for optimal cost-performance balance.",
        "related": [
            (1, "Galvanized Steel Highway Noise Barrier", "Standard absorptive panel for general highway corridors.",
             img("Close-up product photograph of a galvanized steel highway noise barrier panel with perforated pattern, clean industrial background, professional industrial photography")),
            (2, "Aluminum Highway Noise Barrier", "Lightweight aluminum construction for elevated and bridge sections.",
             img("Close-up product photograph of a lightweight aluminum highway noise barrier panel with perforated pattern, clean white background, professional industrial photography")),
            (5, "Full Enclosure Highway Noise Barrier", "Maximum attenuation enclosure for sensitive zones.",
             img("Photorealistic full enclosure highway noise barrier tunnel with steel structure and sound-absorbing panels, clean industrial photography")),
            (7, "Solar Highway Noise Barrier", "Integrated solar PV for renewable energy generation.",
             img("Photorealistic solar highway noise barrier with integrated photovoltaic panels on the upper section, clean industrial photography")),
        ],
    },
}


# Section index: 11 sections per page (gray/blue/white/gray/blue/white/gray/white/gray/white/dark)
SECTIONS = [
    # (mode, generator) — generator returns inner HTML
    ("gray", "_render_pain"),
    ("blue", "_render_advantages"),
    ("white", "_render_specs"),
    ("gray", "_render_apps"),
    ("blue", "_render_details"),
    ("white", "_render_install"),
    ("gray", "_render_certs"),
    ("white", "_render_projects"),
    ("gray", "_render_custom"),
    ("white", "_render_form"),
    ("dark", "_render_related"),
]


def _render_pain(p):
    pp = "\n".join(
        f"""          <div class="rsb-pain-point">
            <div class="rsb-pain-point__icon">{icon}</div>
            <div>
              <h3 class="rsb-pain-point__title">{title}</h3>
              <p class="rsb-pain-point__text">{text}</p>
            </div>
          </div>"""
        for icon, title, text in p["pain_points"]
    )
    return f"""
  <section class="rsb-section rsb-section--gray">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Highway Noise Challenges</span>
        <h2 class="rsb-section__title">{p["h2_why"]}</h2>
        <div class="rsb-divider"></div>
        <p style="color: #4a5568; font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">{p["h2_lead"]}</p>
      </div>
      <div class="rsb-pain-layout">
        <div class="rsb-pain-points">
{pp}
        </div>
        <div class="rsb-pain-layout__image">
          <img src="{p['pain_image']}" alt="{p['name']} highway noise challenge" loading="lazy">
        </div>
      </div>
    </div>
  </section>"""


def _render_advantages(p):
    vals = "\n".join(
        f"""        <div class="rsb-value">
          <div class="rsb-value__number">{num}</div>
          <div class="rsb-value__label">{lab}</div>
          <h3 class="rsb-value__title">{title}</h3>
        </div>"""
        for num, lab, title in p["values"]
    )
    return f"""
  <section class="rsb-section rsb-section--blue">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Core Advantages</span>
        <h2 class="rsb-section__title">Why Choose Yukings {p['name']}</h2>
        <div class="rsb-divider"></div>
        <p style="color: rgba(255,255,255,0.9); font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">{p['lead']}</p>
      </div>
      <div style="margin: 0 0 40px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(8,36,87,0.10);">
        <img src="{p['adv_image']}" alt="Yukings {p['short_name'].lower()} product close-up" loading="lazy" style="width: 100%; height: auto; display: block;">
      </div>
      <div class="rsb-values">
{vals}
      </div>
    </div>
  </section>"""


def _render_specs(p):
    rows = "\n".join(
        f'          <tr class="rsb-specs__row"><td>{name}</td><td>{spec}</td><td>{unit}</td></tr>'
        for name, spec, unit in p["specs"]
    )
    return f"""
  <section class="rsb-section" id="specifications">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Technical Data</span>
        <h2 class="rsb-section__title">{p['name']} Specifications</h2>
        <div class="rsb-divider"></div>
        <p style="color: #4a5568; font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">Engineered with high-grade materials, available in multiple sizes and surface treatments. All products meet ASTM, DIN, EN 14388, and GB standards for durability.</p>
      </div>
      <div style="margin: 0 0 32px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(8,36,87,0.10);">
        <img src="{p['spec_image']}" alt="{p['short_name']} technical dimension diagram" loading="lazy" style="width: 100%; height: auto; display: block;">
      </div>
      <table class="rsb-specs">
        <thead class="rsb-specs__header">
          <tr>
            <th>Parameter</th>
            <th>Specification</th>
            <th>Unit</th>
          </tr>
        </thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>
  </section>"""


def _render_apps(p):
    apps = "\n".join(
        f"""        <div class="rsb-application">
          <div class="rsb-application__icon-wrapper" style="background: {bg};">
            <span class="rsb-application__icon">{icon}</span>
          </div>
          <h3 class="rsb-application__title">{title}</h3>
          <p class="rsb-application__text">{text}</p>
        </div>"""
        for icon, title, text, bg in p["apps"]
    )
    return f"""
  <section class="rsb-section rsb-section--gray">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Application Scenarios</span>
        <h2 class="rsb-section__title">Where Our {p['name']} Protects</h2>
        <div class="rsb-divider"></div>
        <p style="color: #4a5568; font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">Yukings {p['name']} solutions are trusted by 2000+ projects across 20+ countries, with proven performance in the most demanding highway environments.</p>
      </div>
      <div style="margin: 0 0 40px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(8,36,87,0.10);">
        <img src="{p['apps_image']}" alt="{p['short_name']} applications across multiple scenarios" loading="lazy" style="width: 100%; height: auto; display: block;">
      </div>
      <div class="rsb-applications">
{apps}
      </div>
      <div style="text-align: center; margin-top: 40px;">
        <a href="{DOMAIN}/solutions" class="rsb-btn rsb-btn--primary">View All Solutions →</a>
      </div>
    </div>
  </section>"""


def _render_details(p):
    images = "\n".join(
        f"""            <div class="rsb-details__image{' rsb-details__image--active' if i==0 else ''}">
              <img src="{img(p['details_image_prompts'][i])}" alt="{p['details_image_alts'][i]}" loading="lazy" width="800" height="600">
            </div>"""
        for i in range(3)
    )
    details = "\n".join(
        f"""          <div class="rsb-detail-item">
            <div class="rsb-detail-item__icon">{icon}</div>
            <div>
              <h3 class="rsb-detail-item__title">{title}</h3>
              <p class="rsb-detail-item__text">{text}</p>
            </div>
          </div>"""
        for icon, title, text in p["details"]
    )
    return f"""
  <section class="rsb-section rsb-section--blue">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Product Features</span>
        <h2 class="rsb-section__title">{p['name']}: Acoustic Principle &amp; Structure</h2>
        <div class="rsb-divider"></div>
        <p style="color: rgba(255,255,255,0.9); font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">Advanced sound absorption and insulation technology. Modular design for easy installation and long-term performance in highway applications.</p>
      </div>
      <div class="rsb-details">
        <div>
          <div class="rsb-details__images" id="rsb-details-carousel">
{images}
          </div>
          <div class="rsb-details__dots">
            <button type="button" class="rsb-details__dot rsb-details__dot--active" aria-label="Show image 1"></button>
            <button type="button" class="rsb-details__dot" aria-label="Show image 2"></button>
            <button type="button" class="rsb-details__dot" aria-label="Show image 3"></button>
          </div>
        </div>
        <div>
{details}
        </div>
      </div>
    </div>
  </section>"""


def _render_install(p):
    steps = []
    for i, (alt, title, text, prompt) in enumerate(p["install_steps"], 1):
        steps.append(f"""        <div class="rsb-step">
          <div class="rsb-step__image-wrapper">
            <img src="{img(prompt)}" alt="{alt}" class="rsb-step__image" loading="lazy" width="600" height="450">
            <div class="rsb-step__badge">{i}</div>
            <div class="rsb-step__overlay">
              <div class="rsb-step__overlay-number">Step 0{i}</div>
              <h3 class="rsb-step__overlay-title">{title}</h3>
              <p class="rsb-step__overlay-text">{text}</p>
            </div>
          </div>
        </div>""")
    return f"""
  <section class="rsb-section">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Installation Process</span>
        <h2 class="rsb-section__title">{p['name']}: Easy Installation &amp; Maintenance</h2>
        <div class="rsb-divider"></div>
        <p style="color: #4a5568; font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">{p['install_lead']}</p>
      </div>
      <div class="rsb-installation">
{chr(10).join(steps)}
      </div>
    </div>
  </section>"""


def _render_certs(p):
    certs = []
    for icon, code, name, desc, meta in p["certs"]:
        certs.append(f"""        <div class="rsb-certification">
          <div class="rsb-certification__corner rsb-certification__corner--tl"></div>
          <div class="rsb-certification__corner rsb-certification__corner--tr"></div>
          <div class="rsb-certification__corner rsb-certification__corner--bl"></div>
          <div class="rsb-certification__corner rsb-certification__corner--br"></div>
          <span class="rsb-certification__ribbon">Verified</span>
          <div class="rsb-certification__seal">
            <span class="rsb-certification__icon">{icon}</span>
          </div>
          <span class="rsb-certification__code">{code}</span>
          <h3 class="rsb-certification__name">{name}</h3>
          <div class="rsb-certification__divider"></div>
          <p class="rsb-certification__desc">{desc}</p>
          <div class="rsb-certification__meta">
            <span class="rsb-certification__meta-dot"></span>
            <span>{meta}</span>
          </div>
        </div>""")
    return f"""
  <section class="rsb-section rsb-section--gray">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Engineering Projects</span>
        <h2 class="rsb-section__title">Quality Assurance &amp; Certifications</h2>
        <div class="rsb-divider"></div>
        <p style="color: #4a5568; font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">ISO 9001 certified manufacturer with 18+ years experience. All products meet international standards for quality, acoustics, and durability.</p>
      </div>
      <div class="rsb-cert-gallery">
        <figure class="rsb-cert-gallery__wall">
          <img src="{p['cert_image']}" alt="Yukings certification wall display" loading="lazy">
        </figure>
      </div>
      <div class="rsb-certifications">
{chr(10).join(certs)}
      </div>
      <div style="text-align: center; margin-top: 40px;">
        <a href="{DOMAIN}/certifications" class="rsb-btn rsb-btn--primary">View All Certifications →</a>
      </div>
    </div>
  </section>"""


def _render_projects(p):
    cards = []
    for alt, badge, title, loc, desc, src in p["projects"]:
        cards.append(f"""        <div class="rsb-project">
          <div class="rsb-project__image-wrapper">
            <img src="{src}" alt="{alt}" class="rsb-project__image" loading="lazy">
            <span class="rsb-project__badge">{badge}</span>
          </div>
          <div class="rsb-project__content">
            <h3 class="rsb-project__title">{title}</h3>
            <p class="rsb-project__location">{loc}</p>
            <p class="rsb-project__desc">{desc}</p>
          </div>
        </div>""")
    return f"""
  <section class="rsb-section">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Project Cases</span>
        <h2 class="rsb-section__title">Where Our {p['name']} Protects</h2>
        <div class="rsb-divider"></div>
        <p style="color: #4a5568; font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">Yukings {p['name']} solutions are trusted by 2000+ projects across 20+ countries, with proven performance in the most demanding highway environments.</p>
      </div>
      <div class="rsb-projects">
{chr(10).join(cards)}
      </div>
      <div style="text-align: center; margin-top: 40px;">
        <a href="{DOMAIN}/projects" class="rsb-btn rsb-btn--primary">View All Projects →</a>
      </div>
    </div>
  </section>"""


def _render_custom(p):
    customs = "\n".join(
        f"""        <div class="rsb-custom__item">
          <div class="rsb-custom__icon">{icon}</div>
          <h3 class="rsb-custom__title">{title}</h3>
          <p class="rsb-custom__text">{text}</p>
        </div>"""
        for icon, title, text in p["customs"]
    )
    return f"""
  <section class="rsb-section rsb-section--gray">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Custom Solutions</span>
        <h2 class="rsb-section__title">Custom {p['name']} Solutions</h2>
        <div class="rsb-divider"></div>
        <p style="color: #4a5568; font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">Yukings offers comprehensive customization for every {p['name']} project, meeting your most demanding specifications for materials, dimensions, finishes, and performance.</p>
      </div>
      <div style="margin: 0 0 40px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(8,36,87,0.10);">
        <img src="{p['custom_image']}" alt="Customized {p['short_name'].lower()} project showcase" loading="lazy" style="width: 100%; height: auto; display: block;">
      </div>
      <div class="rsb-custom">
{customs}
      </div>
    </div>
  </section>"""


def _render_form(p):
    faqs = "\n".join(
        f"""        <div class="rsb-faq__item">
          <h3 class="rsb-faq__question">{q}</h3>
          <div class="rsb-faq__answer">
            <p>{a}</p>
          </div>
        </div>"""
        for q, a in p["faqs"]
    )
    return f"""
  <section class="rsb-section">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">FAQ</span>
        <h2 class="rsb-section__title">Frequently Asked Questions</h2>
        <div class="rsb-divider"></div>
      </div>
      <div class="rsb-faq">
{faqs}
      </div>

      <div class="rsb-team-support">
        <img src="{img('Professional engineering support team of three engineers in a modern bright office, wearing business casual attire, friendly smiles, sitting at a conference table with engineering drawings and laptops, photorealistic corporate photography, warm lighting')}" alt="Yukings engineering support team available 24/7 for {p['short_name'].lower()} inquiries" loading="lazy" class="rsb-team-support__photo">
        <div class="rsb-team-support__body">
          <h3 class="rsb-team-support__title">{p['team_title']}</h3>
          <p class="rsb-team-support__text">{p['team_text']}</p>
        </div>
      </div>

      <div class="rsb-form">
        <div class="rsb-form__grid">
          <div class="rsb-form__visual">
            <div class="rsb-form__visual-content">
              <h3 class="rsb-form__visual-title">Start Your Project Today</h3>
              <p class="rsb-form__visual-text">18+ years of manufacturing expertise. 50,000㎡ monthly capacity. CE &amp; ISO 9001 certified {p['category'].lower()} for global projects.</p>
            </div>
          </div>
          <div class="rsb-form__body">
            <h3 class="rsb-form__title">Get a Quote</h3>
            <form action="{DOMAIN}/inquiry" method="POST">
              <div class="rsb-form__row">
                <div class="rsb-form__group">
                  <label class="rsb-form__label">Name *</label>
                  <input type="text" class="rsb-form__input" placeholder="Your name" required>
                </div>
                <div class="rsb-form__group">
                  <label class="rsb-form__label">Email *</label>
                  <input type="email" class="rsb-form__input" placeholder="your@email.com" required>
                </div>
              </div>
              <div class="rsb-form__row">
                <div class="rsb-form__group">
                  <label class="rsb-form__label">Company</label>
                  <input type="text" class="rsb-form__input" placeholder="Company name">
                </div>
                <div class="rsb-form__group">
                  <label class="rsb-form__label">Phone</label>
                  <input type="tel" class="rsb-form__input" placeholder="Your phone number">
                </div>
              </div>
              <div class="rsb-form__group">
                <label class="rsb-form__label">Product Interest</label>
                <select class="rsb-form__select">
{PRODUCT_DROPDOWN}
                </select>
              </div>
              <div class="rsb-form__group">
                <label class="rsb-form__label">Project Details</label>
                <textarea class="rsb-form__textarea" placeholder="Describe your project requirements, including dimensions, quantity, and special requirements..."></textarea>
              </div>
              <div class="rsb-form__group" style="text-align: center;">
                <button type="submit" class="rsb-btn rsb-btn--primary rsb-btn--large" style="min-width: 320px;">Submit Inquiry →</button>
              </div>
            </form>
            <p style="text-align: center; margin-top: 24px; color: #4a5568; font-size: 15px;">Prefer to speak with an engineer? <a href="{DOMAIN}/contact" style="font-weight: 600;">Contact Us →</a></p>
          </div>
        </div>
      </div>
    </div>
  </section>"""


def _render_related(p):
    cards = []
    for num, title, text, src in p["related"]:
        slug = SLUGS[num]
        cards.append(f"""        <a href="{PRODUCTS_ROOT}/{slug}/product-{num:02d}" class="rsb-card">
          <img src="{src}" alt="Yukings {title.lower()}" class="rsb-card__image" loading="lazy" width="600" height="400">
          <div class="rsb-card__content">
            <h3 class="rsb-card__title">{title}</h3>
            <p class="rsb-card__text">{text}</p>
          </div>
        </a>""")
    return f"""
  <section class="rsb-section rsb-section--dark">
    <div class="rsb-container">
      <div class="rsb-section__header">
        <span class="rsb-section__subtitle">Related Products</span>
        <h2 class="rsb-section__title">{p['related_title']}</h2>
        <div class="rsb-divider"></div>
        <p style="color: rgba(255,255,255,0.8); font-size: 16px; margin-top: 16px; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">{p['related_lead']}</p>
      </div>
      <div class="rsb-related">
{chr(10).join(cards)}
      </div>
    </div>
  </section>"""


RENDERERS = {
    "_render_pain": _render_pain,
    "_render_advantages": _render_advantages,
    "_render_specs": _render_specs,
    "_render_apps": _render_apps,
    "_render_details": _render_details,
    "_render_install": _render_install,
    "_render_certs": _render_certs,
    "_render_projects": _render_projects,
    "_render_custom": _render_custom,
    "_render_form": _render_form,
    "_render_related": _render_related,
}


def build_page(num: int, p: dict) -> str:
    url = f"{PRODUCTS_ROOT}/{p['slug']}/product-{num:02d}"
    breadcrumb_label = p["category"]
    page_url = url

    sections_html = "\n".join(RENDERERS[gen](p) for _, gen in SECTIONS)

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


def main():
    for num, p in PRODUCTS.items():
        html = build_page(num, p)
        path = OUT / f"product-{num:02d}.html"
        path.write_text(html, encoding="utf-8")
        print(f"Wrote {path}  ({len(html.splitlines())} lines, {len(html)} bytes)")


if __name__ == "__main__":
    main()
