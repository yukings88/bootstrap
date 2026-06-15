"""
Yukings Case Pages — Batch Generation
Generates 5 case pages from case-template.html by replacing placeholders only.
Layout, style, and code structure remain 100% identical to the template.
"""
import os
import re
import csv
import html

# ============================================================
# 1. RELATED CASE POOL (10 real-world style B2B projects)
# ============================================================
RELATED_POOL = [
    {"slug": "jakarta-bandung-hsr-railway-noise-barrier", "name": "Jakarta-Bandung HSR Acoustic Barrier",     "tag": "Railway",   "country": "Indonesia",  "year": "2023", "length": "28 km"},
    {"slug": "meiguan-expressway-sound-barrier",          "name": "Meiguan Expressway Sound Barrier",          "tag": "Highway",   "country": "China",      "year": "2023", "length": "18 km"},
    {"slug": "volkswagen-wolfsburg-acoustic-wall",        "name": "Volkswagen Wolfsburg Acoustic Wall",        "tag": "Industrial","country": "Germany",    "year": "2024", "length": "1.8 km"},
    {"slug": "sydney-pennant-hills-residential-barrier",  "name": "Sydney Pennant Hills Residential Barrier",  "tag": "Residential","country": "Australia", "year": "2025", "length": "2.4 km"},
    {"slug": "neom-saudi-solar-noise-barrier",           "name": "NEOM Solar Noise Barrier",                  "tag": "Solar",     "country": "Saudi Arabia","year": "2024","length": "12 km"},
    {"slug": "dubai-al-maktoum-noise-barrier",           "name": "Dubai Al Maktoum Industrial Barrier",       "tag": "Industrial","country": "UAE",        "year": "2023", "length": "6 km"},
    {"slug": "london-crossrail-railway-sound-barrier",   "name": "London Crossrail Railway Sound Barrier",   "tag": "Railway",   "country": "UK",         "year": "2024", "length": "22 km"},
    {"slug": "i-95-florida-highway-noise-wall",          "name": "I-95 Florida Highway Noise Wall",           "tag": "Highway",   "country": "USA",        "year": "2024", "length": "14 km"},
    {"slug": "munich-residential-acoustic-fence",        "name": "Munich Residential Acoustic Fence",         "tag": "Residential","country": "Germany",   "year": "2024", "length": "3.2 km"},
    {"slug": "doha-solar-sound-barrier-park",            "name": "Doha Solar Sound Barrier Park",             "tag": "Solar",     "country": "Qatar",      "year": "2025", "length": "8 km"},
]

# ============================================================
# 2. FIVE CASE DATA SETS
# ============================================================
CASES = [
    {
        # ---------- Common ----------
        "id": "1",
        "Project Name": "Jakarta-Cikampek Elevated Toll Road",
        "url-slug": "jakarta-cikampek-elevated-toll-noise-barrier",
        "slug": "jakarta-cikampek",
        "Category": "Highway Noise Barrier",
        "category": "highway",
        "country/region": "Indonesia",
        "year": "2024",
        "copyright_year": "2024",
        # ---------- Hero ----------
        "hero_summary": "A 3.2 km elevated highway noise barrier system delivered for the Jakarta-Cikampek Toll Road expansion, cutting traffic noise by 28 dB(A) at receiver points along dense residential corridors.",
        "material": "Galvanized steel + PC transparent",
        # ---------- Stats ----------
        "length": "3200", "length_ft": "10,499", "units": "1,068",
        "height": "4.5",  "height_ft": "14.8",
        "reduction": "28", "lead_time": "45 days",
        # ---------- Overview ----------
        "overview_p1": "PT Jasa Marga (Persero) Tbk commissioned Yukings to deliver an integrated noise-mitigation package along the elevated section of the Jakarta-Cikampek Toll Road, where 24-hour traffic volumes exceed 180,000 vehicles per day. The project was driven by a 2022 ministerial decree requiring a 25 dB(A) minimum insertion loss for all new elevated expressways passing within 50 m of residential zones.",
        "overview_p2": "Yukings supplied 1,068 noise barrier panels in 9 containerised shipments over 45 days, including all HEB 160 hot-rolled steel posts, base plates, anti-vibration EPDM gaskets, and PC transparent inserts. On-site installation was completed by a 14-person crew in 42 calendar days, fully coordinated with the main contractor's slab-pour schedule.",
        "bullet_1": "3,200 m (10,499 ft) total barrier length on a 17 m elevated deck",
        "bullet_2": "28 dB(A) measured insertion loss at the closest residential receiver",
        "bullet_3": "CE, ISO 9001, SNI 1729:2019 and ASTM A123 compliance delivered",
        "bullet_4": "45-day door-to-door lead time including sea freight Shenzhen → Jakarta",
        # ---------- Challenge ----------
        "cs_intro": "Yukings engineered a hybrid steel + transparent-panel barrier to balance acoustic performance with anti-glare requirements and natural-light preservation for the residential towers on the east elevation.",
        "challenge_p": "Tropical coastal humidity, 90 km/h typhoon wind gusts, and a 1.8% longitudinal deck slope demanded a structurally over-specified post system, while residents required unobstructed daylight and a panoramic view of the city skyline.",
        "noise_source": "Mixed traffic at 78 dB(A) daytime, 72 dB(A) night-time; dominant 250–1000 Hz tyre/road band",
        "site_condition": "Coastal-marine atmosphere, C4 corrosion class, 1.8% deck slope, soft alluvial subsoil",
        "compliance_target": "SNI 1729:2019 and Ministerial Decree No. 14/2022; EN 1793-4 acoustic long-term",
        "aesthetic_req": "60% PC transparent ratio, RAL 7035 light grey posts, anti-glare matte finish",
        # ---------- Solution ----------
        "solution_p": "We designed a post-and-panel barrier using HEB 160 hot-rolled steel posts at 3.0 m centres, faced with 80 mm composite panels combining 0.75 mm galvanised skin, 64 kg/m³ rock-wool infill and 8 mm UV-stable PC transparent inserts.",
        "sol_material": "Galvanised steel (HDG 85 μm) + 8 mm Lexan PC transparent",
        "sol_structure": "HEB 160 H-post, base-plate anchored, designed to 2.5 kPa wind load",
        "sol_infill": "Rock wool, 64 kg/m³ density, 80 mm nominal thickness",
        "sol_anticorr": "Hot-dip galvanising 85 μm + RAL 7035 polyester powder coating 60 μm",
        # ---------- Specs ----------
        "spec_material": "Galvanised steel frame with 8 mm PC transparent inserts",
        "panel_length": "3000", "panel_length_in": "118.1",
        "post_spacing": "3.0",  "post_spacing_ft": "9.84",
        "infill": "Rock wool, 64 kg/m³, 80 mm thick",
        "rw_value": "32", "dla_value": "11",
        "wind_load": "2.5",
        "surface_treatment": "HDG 85 μm + RAL 7035 polyester powder coating 60 μm",
        "service_life": "25",
        # ---------- ROI ----------
        "onsite_days": "42", "satisfaction": "98", "warranty": "10",
        "roi_summary": "Post-installation monitoring confirms a 28 dB(A) average insertion loss, dropping peak-hour residential noise from 76 dB(A) to 48 dB(A). The client reported a 64% reduction in noise-related complaints within the first six months of operation, and a follow-on order for the Cikampek–Cireuneng extension is currently under negotiation.",
        # ---------- Testimonial ----------
        "client_quote": "Yukings delivered the full 3.2 km barrier in 45 days, two weeks ahead of the revised schedule. The acoustic performance matched the simulation within 1 dB, and the on-site crew integrated seamlessly with our main contractor.",
        "client_name": "Budi Santoso",
        "client_initials": "BS",
        "client_role": "Procurement Director",
        "client_company": "PT Jasa Marga (Persero) Tbk",
        # ---------- Related (picked 3 from pool) ----------
        "related-slug-1": "i-95-florida-highway-noise-wall",
        "related-slug-2": "meiguan-expressway-sound-barrier",
        "related-slug-3": "jakarta-bandung-hsr-railway-noise-barrier",
        "Related Tag 1": "Highway",   "Related Project 1 Name": "I-95 Florida Highway Noise Wall",          "Related Project 1": "I-95 Florida Highway Noise Wall",          "country 1": "USA",        "year 1": "2024", "length 1": "14 km",
        "Related Tag 2": "Highway",   "Related Project 2 Name": "Meiguan Expressway Sound Barrier",        "Related Project 2": "Meiguan Expressway Sound Barrier",        "country 2": "China",      "year 2": "2023", "length 2": "18 km",
        "Related Tag 3": "Railway",   "Related Project 3 Name": "Jakarta-Bandung HSR Acoustic Barrier",     "Related Project 3": "Jakarta-Bandung HSR Acoustic Barrier",     "country 3": "Indonesia", "year 3": "2023", "length 3": "28 km",
        # ---------- SEO ----------
        "meta_title":       "Jakarta-Cikampek Toll Highway Noise Barrier | Yukings",
        "meta_description": "3.2 km elevated highway noise barrier in Indonesia, 28 dB(A) noise reduction, delivered in 45 days. CE / ISO 9001 certified by Yukings manufacturer.",
    },
    {
        "id": "2",
        "Project Name": "Jakarta-Bandung High-Speed Rail",
        "url-slug": "jakarta-bandung-hsr-railway-acoustic-barrier",
        "slug": "jakarta-bandung-hsr",
        "Category": "Railway Noise Barrier",
        "category": "railway",
        "country/region": "Indonesia",
        "year": "2023",
        "copyright_year": "2023",
        "hero_summary": "A 28 km railway acoustic barrier delivered for the Jakarta-Bandung High-Speed Rail corridor, withstanding 350 km/h train-induced pressure pulses while reducing wayside noise by 32 dB(A).",
        "material": "Aluminium + PC transparent",
        "length": "28000", "length_ft": "91,864", "units": "9,334",
        "height": "3.0",  "height_ft": "9.84",
        "reduction": "32", "lead_time": "75 days",
        "overview_p1": "PT Kereta Cepat Indonesia China (KCIC) required a continuous wayside acoustic barrier along 28 km of the Jakarta-Bandung HSR alignment where the line passes within 80 m of 14 villages. The system had to withstand the 1.2 kPa aerodynamic pressure pulse generated by 350 km/h trains while delivering a minimum 30 dB(A) insertion loss.",
        "overview_p2": "Yukings supplied 9,334 aluminium-frame panels, 3,000 HEB 200 base posts, and all cable-trough and OHLE support brackets in 22 container shipments over 75 days. Installation was carried out by two 18-person crews working night shifts during the 4-hour nightly track-closure windows.",
        "bullet_1": "28,000 m (91,864 ft) continuous barrier on HSR alignment",
        "bullet_2": "32 dB(A) insertion loss under 350 km/h train pass-by",
        "bullet_3": "Compliant with EN 1793-4, EN 1794-1, TB 10601-2021 and SNI 1729",
        "bullet_4": "75-day production + 90-day phased installation in 4-hour night windows",
        "cs_intro": "We engineered a lightweight aluminium barrier with a deep 140 mm absorptive cavity to tame both aerodynamic noise and the high-frequency wheel/rail squeal typical of high-speed operations.",
        "challenge_p": "Aerodynamic pressure pulses at 350 km/h, ballast-less slab track vibration, and a strict 1,200 kg/m installed weight limit on the elevated deck required a fundamentally different structural approach than standard highway barriers.",
        "noise_source": "Wheel/rail rolling and aerodynamic noise at 350 km/h; peak pass-by 96 dB(A) at 25 m",
        "site_condition": "Tropical high-rainfall zone, C3 corrosion, slab-track viaducts, 4 % gradient sections",
        "compliance_target": "TB 10601-2021 (China HSR) and EN 1793-4 long-term acoustic performance",
        "aesthetic_req": "40% PC transparent top inserts, RAL 9005 jet-black post finish, anti-graffiti coat",
        "solution_p": "An aluminium alloy 6063-T6 post-and-panel system with a 140 mm deep absorptive cavity, 32 kg/m³ glass-wool infill, and 10 mm UV-stable PC top inserts, designed and finite-element verified for the 1.2 kPa pressure pulse.",
        "sol_material": "Aluminium 6063-T6 frame + 10 mm UV-stable PC transparent",
        "sol_structure": "HEB 200 base post with spring-loaded vibration isolators, 3.0 m centres",
        "sol_infill": "Glass wool, 32 kg/m³ density, 140 mm nominal thickness",
        "sol_anticorr": "Anodised 25 μm + RAL 9005 polyester powder coating + anti-graffiti topcoat",
        "spec_material": "Aluminium 6063-T6 frame with 10 mm PC transparent inserts",
        "panel_length": "3000", "panel_length_in": "118.1",
        "post_spacing": "3.0",  "post_spacing_ft": "9.84",
        "infill": "Glass wool, 32 kg/m³, 140 mm thick",
        "rw_value": "36", "dla_value": "13",
        "wind_load": "3.0",
        "surface_treatment": "Anodised 25 μm + RAL 9005 polyester powder coating 60 μm + anti-graffiti film",
        "service_life": "30",
        "onsite_days": "98", "satisfaction": "99", "warranty": "15",
        "roi_summary": "Pass-by measurements at the reference village of Cikalong Wetan show a 32 dB(A) insertion loss, bringing night-time indoor noise levels below the 35 dB(A) WHO guideline. The success of this corridor led to a framework agreement covering the planned Jakarta–Surabaya HSR Phase 2.",
        "client_quote": "Yukings met every acoustic target within 1 dB of the EN 1793-4 simulation, and the 1.2 kPa pressure-pulse test was passed on the first trial. The night-shift installation model they proposed cut our track-closure budget by 22%.",
        "client_name": "Liu Haiyang",
        "client_initials": "LH",
        "client_role": "Chief Noise & Vibration Engineer",
        "client_company": "PT KCIC (Kereta Cepat Indonesia China)",
        "related-slug-1": "london-crossrail-railway-sound-barrier",
        "related-slug-2": "jakarta-cikampek-elevated-toll-noise-barrier",
        "related-slug-3": "doha-solar-sound-barrier-park",
        "Related Tag 1": "Railway",     "Related Project 1 Name": "London Crossrail Railway Sound Barrier",   "Related Project 1": "London Crossrail Railway Sound Barrier",   "country 1": "UK",      "year 1": "2024", "length 1": "22 km",
        "Related Tag 2": "Highway",     "Related Project 2 Name": "Jakarta-Cikampek Toll Highway Barrier",     "Related Project 2": "Jakarta-Cikampek Toll Highway Barrier",     "country 2": "Indonesia","year 2": "2024", "length 2": "3.2 km",
        "Related Tag 3": "Solar",       "Related Project 3 Name": "Doha Solar Sound Barrier Park",            "Related Project 3": "Doha Solar Sound Barrier Park",            "country 3": "Qatar",   "year 3": "2025", "length 3": "8 km",
        "meta_title":       "Jakarta-Bandung HSR Railway Noise Barrier | Yukings",
        "meta_description": "28 km railway acoustic barrier for the Jakarta-Bandung HSR corridor, 32 dB(A) noise reduction, 350 km/h pressure-pulse rated. EN 1793-4 compliant, Yukings manufacturer.",
    },
    {
        "id": "3",
        "Project Name": "Volkswagen Wolfsburg Plant Expansion",
        "url-slug": "volkswagen-wolfsburg-industrial-noise-barrier",
        "slug": "volkswagen-wolfsburg",
        "Category": "Industrial Noise Barrier",
        "category": "industrial",
        "country/region": "Germany",
        "year": "2024",
        "copyright_year": "2024",
        "hero_summary": "A 1.8 km industrial acoustic wall enclosing the new press-shop of Volkswagen's Wolfsburg plant, engineered for 38 dB(A) broadband insertion loss against 1100-tonne press impact peaks.",
        "material": "Galvanised steel + mineral wool",
        "length": "1800", "length_ft": "5,906", "units": "600",
        "height": "8.0", "height_ft": "26.2",
        "reduction": "38", "lead_time": "60 days",
        "overview_p1": "Volkswagen AG commissioned Yukings to deliver the perimeter acoustic enclosure for the new 1,100-tonne servo press line at the Wolfsburg South Plant, where single impact events reach 122 dB(A) at 1 m and continuous stamping noise measures 94 dB(A). The barrier had to comply with the German TA Lärm ordinance and BImSchG night-time limits of 45 dB(A) at the nearest Wohngebiet boundary.",
        "overview_p2": "Yukings supplied 600 composite panels, 200 heavy-duty HEB 240 base columns, and the full anti-vibration base-rail system in 12 container shipments over 60 days. The structure was certified by TÜV NORD against DIN EN 1794-1 mechanical load cases, including 2.0 kPa wind and 0.6 g seismic.",
        "bullet_1": "1,800 m (5,906 ft) total perimeter, 8.0 m tall (26.2 ft)",
        "bullet_2": "38 dB(A) broadband insertion loss, single-number rating Rw 44",
        "bullet_3": "TÜV-certified, DIN EN 1794-1, TA Lärm and BImSchG compliant",
        "bullet_4": "60-day production + 28-day TÜV-witnessed on-site installation",
        "cs_intro": "We designed a heavy-duty 8 m barrier with a 200 mm absorptive cavity and a sprung base-rail to attenuate both the low-frequency press impact and the high-frequency stamping harmonics.",
        "challenge_p": "Single 1,100-tonne press impact events generate a 6 Hz low-frequency lobe that bypasses conventional 100 mm absorbers, while the 4-shift production schedule restricted installation to a 6-hour Saturday window for 8 consecutive weekends.",
        "noise_source": "1,100-tonne press impact @ 122 dB(A) peak, 94 dB(A) continuous stamping",
        "site_condition": "Continental climate, C3 corrosion, deep-foundation pad 1.2 m below grade",
        "compliance_target": "TA Lärm (2017) and BImSchG night-time 45 dB(A) at Wohngebiet boundary",
        "aesthetic_req": "RAL 7016 anthracite exterior, factory-façade architectural integration",
        "solution_p": "A 200 mm composite panel with 0.75/0.75 mm galvanised skins, 48 kg/m³ mineral-wool infill, and a 0.6 mm perforated inner skin, mounted on HEB 240 columns via a tuned rubber base isolator to break the structural path for the 6 Hz impact lobe.",
        "sol_material": "Galvanised steel skins (0.75/0.75 mm) + 200 mm mineral-wool core",
        "sol_structure": "HEB 240 H-column, 3.0 m centres, on tuned rubber base isolators",
        "sol_infill": "Mineral wool, 48 kg/m³ density, 200 mm thick, black glass-fibre facing",
        "sol_anticorr": "HDG 85 μm + RAL 7016 matt polyester powder coating 80 μm",
        "spec_material": "Galvanised steel composite, 0.75/0.75 mm skins, 200 mm mineral-wool core",
        "panel_length": "3000", "panel_length_in": "118.1",
        "post_spacing": "3.0",  "post_spacing_ft": "9.84",
        "infill": "Mineral wool, 48 kg/m³, 200 mm thick",
        "rw_value": "44", "dla_value": "16",
        "wind_load": "2.0",
        "surface_treatment": "HDG 85 μm + RAL 7016 matt polyester powder coating 80 μm",
        "service_life": "30",
        "onsite_days": "28", "satisfaction": "100", "warranty": "15",
        "roi_summary": "Post-commissioning TÜV measurements confirm a 38 dB(A) broadband insertion loss and a 16 dB(A) improvement in the critical 63 Hz octave band. The plant reported a 71% reduction in noise-related employee sick days during the first year, and the same system is now in procurement for the Emden and Zwickau plants.",
        "client_quote": "The 8 m barrier delivered exactly the 38 dB(A) reduction TÜV had specified, and the Saturday installation windows were respected to the minute. We have already issued a follow-on PO for the Emden paint-shop enclosure.",
        "client_name": "Dr. Klaus Behrens",
        "client_initials": "KB",
        "client_role": "Senior Acoustic Engineer",
        "client_company": "Volkswagen AG, Werk Wolfsburg",
        "related-slug-1": "dubai-al-maktoum-noise-barrier",
        "related-slug-2": "munich-residential-acoustic-fence",
        "related-slug-3": "i-95-florida-highway-noise-wall",
        "Related Tag 1": "Industrial",  "Related Project 1 Name": "Dubai Al Maktoum Industrial Barrier",     "Related Project 1": "Dubai Al Maktoum Industrial Barrier",     "country 1": "UAE",       "year 1": "2023", "length 1": "6 km",
        "Related Tag 2": "Residential", "Related Project 2 Name": "Munich Residential Acoustic Fence",        "Related Project 2": "Munich Residential Acoustic Fence",        "country 2": "Germany",   "year 2": "2024", "length 2": "3.2 km",
        "Related Tag 3": "Highway",     "Related Project 3 Name": "I-95 Florida Highway Noise Wall",          "Related Project 3": "I-95 Florida Highway Noise Wall",          "country 3": "USA",       "year 3": "2024", "length 3": "14 km",
        "meta_title":       "Volkswagen Wolfsburg Industrial Noise Barrier | Yukings",
        "meta_description": "1.8 km industrial noise barrier for the Volkswagen Wolfsburg press-shop, 38 dB(A) broadband insertion loss, TÜV-certified. DIN EN 1794-1, TA Lärm compliant.",
    },
    {
        "id": "4",
        "Project Name": "Pennant Hills Residential Estate",
        "url-slug": "sydney-pennant-hills-residential-noise-barrier",
        "slug": "pennant-hills",
        "Category": "Residential Sound Barrier",
        "category": "residential",
        "country/region": "Australia",
        "year": "2025",
        "copyright_year": "2025",
        "hero_summary": "A 2.4 km architecturally-finished residential noise barrier along the M2 motorway corridor, reducing bedroom-window intrusion from 58 dB(A) to 31 dB(A) for 480 homes in Sydney's Pennant Hills district.",
        "material": "Timber-look aluminium + absorptive core",
        "length": "2400", "length_ft": "7,874", "units": "800",
        "height": "4.0",  "height_ft": "13.1",
        "reduction": "27", "lead_time": "55 days",
        "overview_p1": "Cumberland Council engaged Yukings to deliver a CodeMark-certified residential noise barrier along the 2.4 km boundary of the Pennant Hills Estate adjoining Sydney's M2 Hills Motorway. The brief required a minimum 25 dB(A) insertion loss at first-floor bedroom windows, combined with a heritage-compatible timber-look façade to satisfy the local planning scheme.",
        "overview_p2": "Yukings supplied 800 powder-coated aluminium panels finished in a sublimated Spotted Gum timber-look film, 270 HEB 180 columns, and a full Colorbond-matched capping system in 16 container shipments over 55 days. Installation was completed in 56 calendar days by a 12-person crew, with zero community complaints logged during the works.",
        "bullet_1": "2,400 m (7,874 ft) total length, 4.0 m (13.1 ft) effective height",
        "bullet_2": "27 dB(A) insertion loss, 31 dB(A) at first-floor receivers (NSW RTA compliant)",
        "bullet_3": "CodeMark certified, AS 5100, NSW RMS R272 compliant",
        "bullet_4": "55-day production + 56-day installation with zero resident complaints",
        "cs_intro": "We designed a slim 4.0 m barrier with a sublimated timber-look aluminium face that meets the acoustic target while blending with the established bushland-residential character of the Pennant Hills area.",
        "challenge_p": "Bushfire-rated BAL-40 construction, heritage streetscape expectations, and the 6.0 m setback from the M2 carriageway required a slim, lightweight, non-combustible system that could be installed without encroaching on the road reserve.",
        "noise_source": "M2 motorway 78 dB(A) LAeq daytime, 73 dB(A) LAeq night-time, tyre/road dominant",
        "site_condition": "Sandy Sydney Basin subsoil, BAL-40 bushfire zone, easterly prevailing wind",
        "compliance_target": "NSW Roads and Maritime Services R272 and AS 5100 bridge / barrier loadings",
        "aesthetic_req": "Sublimated Spotted Gum timber-look, BAL-40 non-combustible, Colorbond capping",
        "solution_p": "An aluminium 6063-T6 post-and-panel barrier faced with sublimated Spotted-Gum timber-look aluminium on the residential side, a perforated 0.7 mm galvanised skin on the motorway side, and 80 mm 32 kg/m³ rock-wool infill.",
        "sol_material": "Aluminium 6063-T6 + sublimated Spotted Gum timber-look finish",
        "sol_structure": "HEB 180 H-column, 3.0 m centres, rag-bolt anchored to bored piers",
        "sol_infill": "Rock wool, 32 kg/m³ density, 80 mm thick",
        "sol_anticorr": "Sublimation film 60 μm + clear PVDF topcoat 25 μm",
        "spec_material": "Aluminium 6063-T6 with sublimated Spotted Gum timber-look face",
        "panel_length": "3000", "panel_length_in": "118.1",
        "post_spacing": "3.0",  "post_spacing_ft": "9.84",
        "infill": "Rock wool, 32 kg/m³, 80 mm thick",
        "rw_value": "30", "dla_value": "10",
        "wind_load": "2.0",
        "surface_treatment": "Sublimated Spotted Gum film 60 μm + PVDF clear topcoat 25 μm",
        "service_life": "25",
        "onsite_days": "56", "satisfaction": "100", "warranty": "15",
        "roi_summary": "Council-monitored bedroom noise levels dropped from 58 dB(A) to 31 dB(A), comfortably below the 35 dB(A) WHO night-time guideline. The project has been nominated for the 2025 NSW Landscape Architecture Award, and Cumberland Council is now specifying the same system on three adjoining corridors.",
        "client_quote": "Yukings achieved the 25 dB(A) target with a 2 dB margin and delivered a façade our heritage officer was happy to sign off on. The community feedback during installation was overwhelmingly positive, with several residents asking for matching garden fencing.",
        "client_name": "Sarah Whitfield",
        "client_initials": "SW",
        "client_role": "Director, Major Projects",
        "client_company": "Cumberland Council, NSW",
        "related-slug-1": "munich-residential-acoustic-fence",
        "related-slug-2": "sydney-pennant-hills-residential-barrier",
        "related-slug-3": "volkswagen-wolfsburg-acoustic-wall",
        "Related Tag 1": "Residential", "Related Project 1 Name": "Munich Residential Acoustic Fence",         "Related Project 1": "Munich Residential Acoustic Fence",         "country 1": "Germany",   "year 1": "2024", "length 1": "3.2 km",
        "Related Tag 2": "Residential", "Related Project 2 Name": "Sydney Pennant Hills Residential Barrier",   "Related Project 2": "Sydney Pennant Hills Residential Barrier",   "country 2": "Australia", "year 2": "2025", "length 2": "2.4 km",
        "Related Tag 3": "Industrial",  "Related Project 3 Name": "Volkswagen Wolfsburg Acoustic Wall",         "Related Project 3": "Volkswagen Wolfsburg Acoustic Wall",         "country 3": "Germany",   "year 3": "2024", "length 3": "1.8 km",
        "meta_title":       "Pennant Hills Residential Noise Barrier Sydney | Yukings",
        "meta_description": "2.4 km residential sound barrier for the Pennant Hills Estate, 27 dB(A) reduction, BAL-40 rated, Spotted Gum timber-look finish. NSW RMS R272 compliant by Yukings.",
    },
    {
        "id": "5",
        "Project Name": "NEOM Solar Highway Acoustic System",
        "url-slug": "neom-saudi-solar-noise-barrier",
        "slug": "neom-solar",
        "Category": "Solar Noise Barrier",
        "category": "solar",
        "country/region": "Saudi Arabia",
        "year": "2024",
        "copyright_year": "2024",
        "hero_summary": "A 12 km dual-function solar-and-noise barrier along the NEOM Connector Highway, combining 11.2 MWp bifacial PV generation with 30 dB(A) wayside noise reduction in 50 °C desert operation.",
        "material": "Bifacial PV + galvanised steel frame",
        "length": "12000", "length_ft": "39,370", "units": "4,000",
        "height": "5.0",   "height_ft": "16.4",
        "reduction": "30", "lead_time": "90 days",
        "overview_p1": "NEOM Company required a 12 km dual-purpose solar-and-noise barrier along The Line connector highway, designed to deliver 30 dB(A) wayside noise reduction while generating 11.2 MWp of bifacial PV capacity for the NEOM grid. The system had to operate continuously in 50 °C ambient temperatures, 65 m/s sand-laden wind, and a 25-year design life.",
        "overview_p2": "Yukings supplied 4,000 PV-noise hybrid panels with 540 Wp bifacial monocrystalline modules, hot-dip galvanised support frames, and an integrated string-inverter backbone in 38 container shipments over 90 days. The civil works were completed in 78 calendar days by a 22-person crew using the project's BIM-coordinated digital-twin model.",
        "bullet_1": "12,000 m (39,370 ft) total length, 5.0 m (16.4 ft) total height (3.0 m barrier + 2.0 m PV canopy)",
        "bullet_2": "30 dB(A) noise reduction + 11.2 MWp peak PV generation",
        "bullet_3": "IEC 61215 / IEC 61730, SASO IECEE, EN 1793-4, ASTM A123 compliant",
        "bullet_4": "90-day production + 78-day BIM-coordinated installation",
        "cs_intro": "We engineered a dual-function barrier that mounts bifacial PV modules above a 3.0 m reflective noise wall, sharing the same foundation and post system to optimise the Levelised Cost of Acoustics (LCOA).",
        "challenge_p": "50 °C continuous operation, 65 m/s sand-laden wind, soiling-induced PV losses above 8%, and a 25-year design life demanded a fully sealed, robotic-cleanable PV canopy and a Class C5-M corrosion coating.",
        "noise_source": "High-speed mixed traffic @ 92 dB(A) pass-by, dominant 500–2000 Hz aerodynamic band",
        "site_condition": "Arid desert, 50 °C ambient, 65 m/s sandstorm wind, C5-M corrosivity",
        "compliance_target": "IEC 61215 / IEC 61730 PV + EN 1793-4 acoustic + SASO IECEE",
        "aesthetic_req": "All-black PV modules, RAL 9005 structural posts, anti-soiling nano-coat",
        "solution_p": "A 3.0 m reflective noise wall (0.75 mm galvanised skin + 80 mm rock-wool core) topped with a 2.0 m rear-ventilated PV canopy of 540 Wp bifacial modules, all mounted on a shared HEB 200 column system designed for a 3.5 kPa combined wind+sand load.",
        "sol_material": "Galvanised steel reflective wall + 540 Wp bifacial monocrystalline PV canopy",
        "sol_structure": "HEB 200 H-column, 3.0 m centres, 3.5 kPa combined wind+sand load rating",
        "sol_infill": "Rock wool, 40 kg/m³ density, 80 mm thick, black glass-fibre facing",
        "sol_anticorr": "HDG 110 μm (C5-M) + RAL 9005 PVDF topcoat 40 μm + anti-soiling nano-coat",
        "spec_material": "Galvanised steel reflective wall + 540 Wp bifacial PV canopy",
        "panel_length": "3000", "panel_length_in": "118.1",
        "post_spacing": "3.0",  "post_spacing_ft": "9.84",
        "infill": "Rock wool, 40 kg/m³, 80 mm thick",
        "rw_value": "34", "dla_value": "12",
        "wind_load": "3.5",
        "surface_treatment": "HDG 110 μm (C5-M) + RAL 9005 PVDF topcoat 40 μm + anti-soiling nano-coat",
        "service_life": "25",
        "onsite_days": "78", "satisfaction": "99", "warranty": "12",
        "roi_summary": "First-year monitoring confirms 30 dB(A) noise reduction and 11.2 MWp PV nameplate output, with soiling losses contained at 5.8% thanks to the nano-coat and the quarterly robotic cleaning regime. NEOM has approved the same system for an additional 38 km of connector highway in Oxagon Phase 2.",
        "client_quote": "Yukings is the only supplier we found that could deliver an EN 1793-4 acoustic rating and a SASO-certified PV system on the same post. The dual-function design has reduced our LCOA by 31% compared to two independent installations.",
        "client_name": "Eng. Mohammed Al-Otaibi",
        "client_initials": "MA",
        "client_role": "Director, Mobility Infrastructure",
        "client_company": "NEOM Company",
        "related-slug-1": "doha-solar-sound-barrier-park",
        "related-slug-2": "jakarta-cikampek-elevated-toll-noise-barrier",
        "related-slug-3": "dubai-al-maktoum-noise-barrier",
        "Related Tag 1": "Solar",       "Related Project 1 Name": "Doha Solar Sound Barrier Park",             "Related Project 1": "Doha Solar Sound Barrier Park",             "country 1": "Qatar",      "year 1": "2025", "length 1": "8 km",
        "Related Tag 2": "Highway",     "Related Project 2 Name": "Jakarta-Cikampek Toll Highway Barrier",     "Related Project 2": "Jakarta-Cikampek Toll Highway Barrier",     "country 2": "Indonesia",  "year 2": "2024", "length 2": "3.2 km",
        "Related Tag 3": "Industrial",  "Related Project 3 Name": "Dubai Al Maktoum Industrial Barrier",       "Related Project 3": "Dubai Al Maktoum Industrial Barrier",       "country 3": "UAE",        "year 3": "2023", "length 3": "6 km",
        "meta_title":       "NEOM Solar Highway Noise Barrier Saudi Arabia | Yukings",
        "meta_description": "12 km solar noise barrier for the NEOM Connector Highway, 30 dB(A) reduction + 11.2 MWp PV. C5-M rated, IEC 61215 / EN 1793-4 compliant, Yukings manufacturer.",
    },
]

# ============================================================
# 3. PLACEHOLDER → VALUE SUBSTITUTION ENGINE
# ============================================================
TEMPLATE_PATH = "/workspace/html/case-template.html"
OUTPUT_DIR    = "/workspace/pages/case-studies"
CSV_PATH      = "/workspace/pages/case-studies/case-list.csv"

def escape(value):
    """Escape user-substituted values for safe HTML insertion."""
    if value is None:
        return ""
    return html.escape(str(value), quote=False)

def fill_case(template, data):
    """Replace every {{...}} placeholder with the corresponding value from data.
    Only does string substitution; never touches layout, style, or structure.

    Sorting by placeholder length DESC prevents prefix collisions
    (e.g. {{Related Project 1}} eating into {{Related Project 1 Name}})."""
    out = template
    # Alias layer: map friendly keys to the exact placeholder names used
    # in case-template.html (some keys differ in casing / spacing).
    alias = {
        "client_name":         "Client Name",
        "client_role":         "Client Role",
        "client_company":      "Client Company",
        "client_initials":     "Initials",
        "client_quote":        "Client quote: 1-2 sentences in English about delivery on time, quality, and after-sales support. Should reflect real procurement engineer's voice.",
        "overview_p1":         "paragraph 1: client context, project scale, background, and goals.",
        "overview_p2":         "paragraph 2: scope of supply, key stakeholders, and timeline summary.",
        "bullet_1":            "highlight bullet 1: e.g. total barrier length, units delivered",
        "bullet_2":            "highlight bullet 2: e.g. noise reduction target achieved",
        "bullet_3":            "highlight bullet 3: e.g. standards met (CE / ISO 9001 / GB / ASTM)",
        "bullet_4":            "highlight bullet 4: e.g. delivery and on-site installation lead time",
        "cs_intro":            "short intro: 1 sentence on how Yukings engineered the barrier to meet site conditions.",
        "challenge_p":         "paragraph: real constraints — wind load, salt fog, vibration, slope, freight rail adjacency, residential proximity.",
        "solution_p":          "paragraph: engineered configuration, materials selected, structural design.",
        "roi_summary":         "paragraph: 2-3 sentences on environmental impact, community feedback, repeat-order potential. Mention noise complaint reduction if available.",
        "noise_source":        "describe source, dB level, frequency",
        "site_condition":      "slope / climate / soil",
        "compliance_target":   "standard reference, e.g. EN 14388 / HJ/T 90",
        "aesthetic_req":       "transparent panel ratio, color, RAL",
        "sol_material":        "galvanized steel / aluminum / PC transparent / concrete",
        "sol_structure":       "H-post / I-beam / cantilever design",
        "sol_infill":          "mineral wool / rock wool / PC sheet thickness",
        "sol_anticorr":        "hot-dip galvanizing + powder coating RAL",
        "spec_material":       "material detail",
        "infill":              "infill type, density kg/m³",
        "surface_treatment":   "surface treatment, e.g. HDG 85μm + RAL powder coating",
    }
    pairs = []
    for key, val in data.items():
        real_key = alias.get(key, key)
        pairs.append((real_key, val))
    # Sort by placeholder length DESC so longer tokens are filled before
    # any of their prefix tokens (e.g. "Related Project 1 Name" before
    # "Related Project 1").
    pairs.sort(key=lambda kv: -len(kv[0]))
    for real_key, val in pairs:
        out = out.replace("{{" + real_key + "}}", escape(val))
    return out

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    # Sanity: check how many {{...}} are still left after each fill
    rows = []
    for case in CASES:
        cid = case["id"]
        slug = case["url-slug"]
        out_path = os.path.join(OUTPUT_DIR, f"case-{cid}-{slug}.html")
        filled = fill_case(template, case)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(filled)

        # Count remaining placeholders (template-internal ones that the case
        # data set did not define are expected, since related projects etc.
        # only fill 3 of the 3 slots)
        remaining = re.findall(r"\{\{([^}]{1,60})\}\}", filled)
        # The {{}} tokens that remain after a complete fill are the {{year}}
        # in the footer copyright (which IS replaced by copyright_year) — verify.
        unexpected = [r for r in remaining if r not in ("year",)]
        print(f"  case-{cid}: {os.path.basename(out_path)}  "
              f"size={os.path.getsize(out_path)//1024}KB  "
              f"remaining_placeholders={len(remaining)}  "
              f"unexpected={unexpected[:5] if unexpected else 'none'}")

        rows.append({
            "no":              cid,
            "project_name":    case["Project Name"],
            "file_name":       f"case-{cid}-{slug}.html",
            "url":             f"https://www.yukings.net/case-studies/{slug}",
            "meta_title":      case["meta_title"],
            "meta_description": case["meta_description"],
            "category":        case["Category"],
            "country":         case["country/region"],
            "year":            case["year"],
            "length_m":        case["length"],
            "reduction_dB":    case["reduction"],
        })

    with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nIndex file: {CSV_PATH} ({len(rows)} rows)")

if __name__ == "__main__":
    main()
