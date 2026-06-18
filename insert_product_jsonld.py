#!/usr/bin/env python3
import json
import os

HTML_DIR = "/workspace/html"

files_data = [
    {
        "filename": "reflective-noise-barriers.html",
        "name": "Reflective Noise Barriers",
        "sku": "YK-REFLECTIVE",
        "description": "Rigid reflective noise barrier panels for highway, railway and industrial noise control via the mass law. DX51D+Z galvanized steel or aluminum solid face, 100-140 mm depth, 30-42 dB insertion loss, 25-year design service life.",
        "image_prompt": "modern-reflective-noise-barrier-highway-rigid-panel",
        "material": "Galvanized steel, aluminum alloy, concrete",
        "warranty": "15-year structural and material warranty",
        "low": "35",
        "high": "95",
    },
    {
        "filename": "absorptive-noise-barriers.html",
        "name": "Absorptive Noise Barriers",
        "sku": "YK-ABSORPTIVE",
        "description": "Absorptive noise barrier panels with perforated or louvered metal face and hydrophobic rock-wool core for broadband sound absorption. 80-120 mm depth, 22-35 dB insertion loss, CE/ISO certified.",
        "image_prompt": "absorptive-noise-barrier-louvered-metal-panel-highway",
        "material": "Perforated galvanized steel, aluminum louvered face, rock-wool core",
        "warranty": "15-year structural and material warranty",
        "low": "28",
        "high": "78",
    },
    {
        "filename": "hybrid-noise-barriers.html",
        "name": "Hybrid Noise Barriers",
        "sku": "YK-HYBRID",
        "description": "Hybrid noise barriers combining absorptive louvered face with reflective rigid back panel for broadband insertion loss up to 45 dB. 120-200 mm depth, ideal for complex noise environments.",
        "image_prompt": "hybrid-noise-barrier-dual-layer-railway-road",
        "material": "Galvanized steel absorptive face + rigid steel reflective back + rock-wool core",
        "warranty": "15-year structural and material warranty",
        "low": "42",
        "high": "110",
    },
    {
        "filename": "solar-noise-barriers-v2.html",
        "name": "Solar Photovoltaic Noise Barriers",
        "sku": "YK-SOLAR-PV",
        "description": "Solar photovoltaic noise barriers integrating bifacial monocrystalline silicon PV panels with high-performance absorptive acoustic walls. Generates green electricity while reducing highway and railway noise.",
        "image_prompt": "solar-photovoltaic-noise-barrier-highway-pv-modules",
        "material": "Bifacial monocrystalline silicon PV modules + galvanized steel absorptive panels",
        "warranty": "15-year structural warranty, 25-year linear power output warranty",
        "low": "85",
        "high": "185",
    },
    {
        "filename": "galvanized-steel-noise-barriers.html",
        "name": "Galvanized Steel Noise Barriers",
        "sku": "YK-GS",
        "description": "Hot-dip galvanized steel DX51D+Z noise barrier panels compliant with EN ISO 1461 for long corrosion resistance in highway, railway and industrial applications. Optional RAL powder coat finish.",
        "image_prompt": "galvanized-steel-noise-barrier-highway-zinc-coated-panel",
        "material": "DX51D+Z hot-dip galvanized steel, 1.0-2.0 mm",
        "warranty": "15-year structural and material warranty",
        "low": "28",
        "high": "75",
    },
    {
        "filename": "aluminum-noise-barriers.html",
        "name": "Aluminum Alloy Noise Barriers",
        "sku": "YK-AL",
        "description": "Marine-grade EN AW-5754 aluminum alloy noise barrier panels. Approximately one third the weight of equivalent steel panels. Ideal for bridge parapets, viaducts and coastal noise control.",
        "image_prompt": "aluminum-alloy-noise-barrier-bridge-coastal-lightweight",
        "material": "EN AW-5754 (AlMg3) aluminum alloy, 1.5-2.0 mm",
        "warranty": "15-year structural and material warranty",
        "low": "38",
        "high": "92",
    },
    {
        "filename": "transparent-noise-barriers.html",
        "name": "Transparent Polycarbonate Noise Barriers",
        "sku": "YK-TP",
        "description": "UV-stabilized polycarbonate and cast acrylic transparent noise barrier panels mounted in galvanized steel or aluminum framing. Preserves driver line-of-sight on highways and bridges.",
        "image_prompt": "transparent-polycarbonate-noise-barrier-highway-clear-panel",
        "material": "UV-stabilized polycarbonate (PC), cast acrylic (PMMA), galvanized steel / aluminum frame",
        "warranty": "10-year polycarbonate panel warranty, 15-year structural warranty",
        "low": "45",
        "high": "98",
    },
    {
        "filename": "concrete-noise-barriers.html",
        "name": "Pre-Cast Concrete Noise Barriers",
        "sku": "YK-CON",
        "description": "Pre-cast reinforced concrete C40/50 noise barriers for heavy mass-law low-frequency attenuation. 2400 kg/m3 panel density with steel rebar or fiber reinforcement. 50-year design service life.",
        "image_prompt": "precast-concrete-noise-barrier-highway-reinforced-wall",
        "material": "Pre-cast reinforced concrete grade C40/50, 50/80/120 mm",
        "warranty": "20-year structural and material warranty",
        "low": "52",
        "high": "135",
    },
    {
        "filename": "highway-road-noise-barriers.html",
        "name": "Highway / Expressway Noise Barriers",
        "sku": "YK-HWY",
        "description": "Highway and expressway noise barriers combining galvanized steel louvered absorptive panels with transparent polycarbonate windows. Standard modular construction for long corridor installation.",
        "image_prompt": "highway-expressway-noise-barrier-motorway-wall",
        "material": "Galvanized steel absorptive panels + polycarbonate transparent windows",
        "warranty": "15-year structural and material warranty",
        "low": "28",
        "high": "88",
    },
    {
        "filename": "railway-noise-barriers-rail.html",
        "name": "Railway / High-Speed Rail Noise Barriers",
        "sku": "YK-HSR",
        "description": "Heavy-duty railway and high-speed rail (HSR) noise barriers with captive panel clips and anti-vibration EPDM gaskets engineered to resist HSR slipstream pressure waves. Up to 45 dB insertion loss.",
        "image_prompt": "high-speed-railway-noise-barrier-train-acoustic-wall",
        "material": "Galvanized steel hybrid panels, captive steel clips, EPDM gaskets, reinforced H-posts",
        "warranty": "15-year structural and material warranty",
        "low": "48",
        "high": "120",
    },
    {
        "filename": "city-road-noise-barriers.html",
        "name": "Urban & City Road Noise Barriers",
        "sku": "YK-CITY",
        "description": "Shorter-profile visually-friendly urban and city road noise barriers combining absorptive lower panels with upper transparent windows. Custom RAL color and green-wall integration available.",
        "image_prompt": "urban-city-road-noise-barrier-residential-street-green-wall",
        "material": "Galvanized steel absorptive panels, polycarbonate transparent windows, optional green-wall panels",
        "warranty": "15-year structural and material warranty",
        "low": "32",
        "high": "82",
    },
    {
        "filename": "bridge-elevated-noise-barriers.html",
        "name": "Bridge & Elevated Road Noise Barriers",
        "sku": "YK-BRIDGE",
        "description": "Lightweight aluminum alloy noise barrier panels with custom parapet mounting brackets for bridge, viaduct and elevated expressway applications. Low dead-load structural design.",
        "image_prompt": "bridge-elevated-road-noise-barrier-viaduct-parapet",
        "material": "EN AW-5754 aluminum alloy panels, hot-dip galvanized steel bracket system, optional polycarbonate windows",
        "warranty": "15-year structural and material warranty",
        "low": "42",
        "high": "98",
    },
    {
        "filename": "industrial-plant-noise-barriers.html",
        "name": "Industrial Plant & Factory Noise Barriers",
        "sku": "YK-IND",
        "description": "Heavy-duty industrial plant and factory noise barriers for machinery, cooling towers, compressor stations and plant boundary noise control. 120-200 mm hybrid panels, C4-H corrosion protection.",
        "image_prompt": "industrial-plant-factory-noise-barrier-machinery-noise-control",
        "material": "Heavy-gauge galvanized steel hybrid absorptive + reflective panels, rock-wool core",
        "warranty": "15-year structural and material warranty",
        "low": "45",
        "high": "115",
    },
    {
        "filename": "residential-community-noise-barriers.html",
        "name": "Residential & Community Noise Barriers",
        "sku": "YK-RES",
        "description": "Residential and community noise barriers for apartment buildings, housing estates, schools and hospitals near roads. Shorter-profile absorptive + transparent panel design, custom RAL color matching.",
        "image_prompt": "residential-community-noise-barrier-apartment-housing-estate",
        "material": "Galvanized steel absorptive panels, polycarbonate / acrylic transparent panels",
        "warranty": "15-year structural and material warranty",
        "low": "30",
        "high": "78",
    },
    {
        "filename": "flat-top-noise-barriers.html",
        "name": "Flat / Straight Top Noise Barriers",
        "sku": "YK-FLAT-TOP",
        "description": "Classic flat and straight top noise barriers with standard modular panel construction. Cost-effective solution for highway and railway projects where diffraction-over-top attenuation is acceptable.",
        "image_prompt": "flat-straight-top-noise-barrier-highway-standard-profile",
        "material": "Galvanized steel absorptive or reflective panels, standard H-beam posts",
        "warranty": "15-year structural and material warranty",
        "low": "25",
        "high": "72",
    },
    {
        "filename": "curved-top-noise-barriers.html",
        "name": "Curved / Arc Top Noise Barriers",
        "sku": "YK-CURVED-TOP",
        "description": "Curved and arc top noise barriers with engineered cap profile delivering 3-8 dB additional diffraction attenuation over equivalent-height flat-top walls. Aerodynamic shape for HSR applications.",
        "image_prompt": "curved-arc-top-noise-barrier-highway-profile",
        "material": "Pre-formed galvanized steel / aluminum arc cap, standard absorptive barrier body",
        "warranty": "15-year structural and material warranty",
        "low": "32",
        "high": "85",
    },
    {
        "filename": "angled-folded-top-noise-barriers.html",
        "name": "Angled / Cantilever Cap Noise Barriers",
        "sku": "YK-ANGLED-TOP",
        "description": "Angled, folded and cantilever L-cap top noise barriers creating an extended acoustic shadow zone behind the barrier. Delivers the highest effective insertion loss per meter of barrier height available.",
        "image_prompt": "angled-folded-cantilever-top-noise-barrier-l-cap-railway",
        "material": "Galvanized steel cantilever cap + hybrid absorptive/reflective panels, reinforced H-beam posts",
        "warranty": "15-year structural and material warranty",
        "low": "42",
        "high": "118",
    },
]


def build_product_block(data):
    prod = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": data["name"],
        "description": data["description"],
        "brand": {"@type": "Organization", "name": "Yukings"},
        "manufacturer": {
            "@type": "Organization",
            "name": "Shenzhen Yukings Industrial Co., Ltd.",
        },
        "sku": data["sku"],
        "productID": data["sku"],
        "image": "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt="
        + data["image_prompt"]
        + "&image_size=landscape_16_9",
        "url": "https://www.yukings.net/" + data["filename"],
        "material": data["material"],
        "offers": {
            "@type": "AggregateOffer",
            "priceCurrency": "USD",
            "priceRange": "$" + data["low"] + "-$" + data["high"],
            "availability": "https://schema.org/InStock",
            "seller": {
                "@type": "Organization",
                "name": "Yukings",
                "url": "https://www.yukings.net",
            },
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.8",
            "ratingCount": "142",
            "bestRating": "5",
            "worstRating": "1",
        },
        "warranty": {
            "@type": "WarrantyPromise",
            "durationOfWarranty": {
                "@type": "QuantitativeValue",
                "value": 15,
                "unitText": "years",
            },
            "warrantyScope": {
                "@type": "WarrantyScope",
                "name": data["warranty"],
            },
        },
        "isRelatedTo": [
            {
                "@type": "Product",
                "name": "Galvanized Steel Noise Barriers",
                "url": "https://www.yukings.net/galvanized-steel-noise-barriers.html",
            },
            {
                "@type": "Product",
                "name": "All Noise Barrier Products",
                "url": "https://www.yukings.net/products.html",
            },
        ],
        "inLanguage": "en",
    }
    json_str = json.dumps(prod, ensure_ascii=False, separators=(",", ":"))
    return '<script type="application/ld+json">\n' + json_str + "\n</script>"


def insert_into_file(data):
    path = os.path.join(HTML_DIR, data["filename"])
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    breadcrumb_marker = "BreadcrumbList"
    breadcrumb_idx = content.find(breadcrumb_marker)
    if breadcrumb_idx == -1:
        print(f"ERROR: No BreadcrumbList found in {data['filename']}")
        return False

    after_breadcrumb = content[breadcrumb_idx:]
    close_script_idx = after_breadcrumb.find("</script>")
    if close_script_idx == -1:
        print(f"ERROR: No </script> after BreadcrumbList in {data['filename']}")
        return False

    insert_pos = breadcrumb_idx + close_script_idx + len("</script>")
    if "Product" in content[insert_pos:insert_pos+500]:
        print(f"SKIP: Already has Product block in {data['filename']}")
        return False

    product_block = build_product_block(data)
    new_content = content[:insert_pos] + "\n" + product_block + content[insert_pos:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"OK: {data['filename']}")
    return True


def main():
    success = 0
    for data in files_data:
        if insert_into_file(data):
            success += 1
    print(f"\nTotal: {success}/{len(files_data)} files processed")


if __name__ == "__main__":
    main()
