#!/usr/bin/env python3
"""Batch update noise barrier classification pages."""
import shutil
import re

HTML_DIR = "/workspace/html"

# ============================================================
# 1. Update flat-top-noise-barriers.html
# ============================================================
def update_flat_top():
    path = f"{HTML_DIR}/flat-top-noise-barriers.html"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # Title / description / keywords
    c = c.replace(
        "<title>Flat / Straight Top Noise Barriers | Yukings</title>",
        "<title>Flat Panel Noise Barriers | Yukings</title>",
    )
    c = c.replace(
        '<meta name="description" content="Flat and straight top noise barriers — classic standard-profile modular panels for cost-effective highway and railway noise control. Request a free quote.">',
        '<meta name="description" content="Flat panel noise barriers — classic straight-profile modular panels for cost-effective highway, railway and urban noise control. CE / ISO certified. Request a free quote.">',
    )
    c = c.replace(
        '<meta name="keywords" content="flat top noise barrier, straight top sound barrier, flat profile acoustic barrier, standard top noise wall, flat-top noise barrier manufacturer, Yukings flat top noise barriers">',
        '<meta name="keywords" content="flat panel noise barrier, straight profile sound barrier, flat-form acoustic barrier, standard noise wall, Yukings flat panel noise barrier manufacturer">',
    )
    # og:title / twitter:title
    c = c.replace(
        '<meta property="og:title" content="Flat / Straight Top Noise Barriers">',
        '<meta property="og:title" content="Flat Panel Noise Barriers">',
    )
    c = c.replace(
        '<meta name="twitter:title" content="Flat / Straight Top Noise Barriers">',
        '<meta name="twitter:title" content="Flat Panel Noise Barriers">',
    )
    # og:description / twitter:description
    c = c.replace(
        '<meta property="og:description" content="Flat and straight top noise barriers — classic standard-profile modular panels for cost-effective highway and railway noise control. Request a free quote.">',
        '<meta property="og:description" content="Flat panel noise barriers — classic straight-profile modular panels for cost-effective highway, railway and urban noise control. CE / ISO certified. Request a free quote.">',
    )
    c = c.replace(
        '<meta name="twitter:description" content="Flat and straight top noise barriers — classic standard-profile modular panels for cost-effective highway and railway noise control. Request a free quote.">',
        '<meta name="twitter:description" content="Flat panel noise barriers — classic straight-profile modular panels for cost-effective highway, railway and urban noise control. CE / ISO certified. Request a free quote.">',
    )

    # Product JSON-LD
    c = c.replace(
        '"name":"Flat / Straight Top Noise Barriers"',
        '"name":"Flat Panel / Straight Panel Noise Barriers"',
    )
    c = c.replace(
        '"description":"Classic flat and straight top noise barriers with standard modular panel construction. Cost-effective solution for highway and railway projects where diffraction-over-top attenuation is acceptable."',
        '"description":"Flat / straight panel form noise barriers with standard modular panel construction. The classic straight-profile noise wall for cost-effective highway, railway and urban noise control projects."',
    )
    c = c.replace('"sku":"YK-FLAT-TOP"', '"sku":"YK-FLAT-PANEL"')
    c = c.replace('"productID":"YK-FLAT-TOP"', '"productID":"YK-FLAT-PANEL"')
    c = c.replace(
        '"material":"Galvanized steel absorptive or reflective panels, standard H-beam posts"',
        '"material":"DX51D+Z galvanized steel perforated absorptive panels, EN AW-5754 aluminum, standard H-beam posts, optional polycarbonate transparent windows"',
    )
    c = c.replace('"priceRange":"$25-$72"', '"priceRange":"$28-$78"')

    # BreadcrumbList position 3
    c = c.replace(
        '{"@type":"ListItem","position":3,"name":"Flat Top Noise Barriers","item":"https://www.yukings.net/flat-top-noise-barriers.html"}',
        '{"@type":"ListItem","position":3,"name":"Flat Panel Noise Barriers","item":"https://www.yukings.net/flat-top-noise-barriers.html"}',
    )

    # Breadcrumb HTML
    c = c.replace(
        '<span class="rsb-breadcrumb__current">Flat Top Noise Barriers</span>',
        '<span class="rsb-breadcrumb__current">Flat Panel Noise Barriers</span>',
    )

    # Hero h1
    c = c.replace(
        '<h1 id="hero-title">Flat &amp; straight top noise barriers — classic standard-profile modular noise wall with straightforward panel installation for cost-effective <span>highway &amp; railway</span> noise control.</h1>',
        '<h1 id="hero-title">Flat panel (straight-profile) noise barriers — classic standard modular noise wall for cost-effective <span>highway, railway &amp; urban</span> noise control.</h1>',
    )

    # Hero lede
    c = c.replace(
        '<p class="lede">Yukings flat-top noise barriers are the classic straight-profile noise wall with standard modular panel construction. The flat top profile is simple to manufacture, easy to install and maintain, and delivers reliable attenuation for most highway, railway and industrial noise control applications. Straight-top barriers are the default choice for cost-effective, high-volume noise wall installation.</p>',
        '<p class="lede">Yukings flat panel noise barriers are the classic straight-profile noise wall with standard modular panel construction. The flat-form panel profile is simple to manufacture, easy to install and maintain, and delivers reliable attenuation for highway, railway and urban noise control applications. Straight-profile barriers are the default choice for cost-effective, high-volume noise wall installation.</p>',
    )

    # Hero chips
    c = c.replace(
        '<span class="rsb-hero__chip">Classic Straight Profile</span><span class="rsb-hero__chip">Standard Modular Panels</span><span class="rsb-hero__chip">Cost-Effective High-Volume</span><span class="rsb-hero__chip">Easy Installation &amp; Maintenance</span><span class="rsb-hero__chip">Universal Application</span>',
        '<span class="rsb-hero__chip">Classic Straight Profile</span><span class="rsb-hero__chip">Standard Modular Panels</span><span class="rsb-hero__chip">Cost-Effective</span><span class="rsb-hero__chip">Easy Installation &amp; Maintenance</span><span class="rsb-hero__chip">Universal Application</span>',
    )

    # Product overview headings
    c = c.replace(
        '<span class="rsb-eyebrow">Product Overview</span>\n      <h2>Flat Top Noise Barriers — Standard Profile</h2>',
        '<span class="rsb-eyebrow">Product Overview</span>\n      <h2>Flat Panel / Straight Profile Noise Barriers</h2>',
    )
    c = c.replace(
        '<p>The flat-top or straight-top profile is the most widely used noise wall geometry, combining proven modular panel construction with simple top-of-wall installation. It is the default specification for highway, railway and industrial projects where cost-effectiveness, speed of installation and long-term reliability are the primary criteria.</p>',
        '<p>The flat / straight panel form is the most widely used noise wall geometry, combining proven modular panel construction with simple installation. It is the default specification for highway, railway and urban projects where cost-effectiveness, speed of installation and long-term reliability are the primary criteria.</p>',
    )

    # Split section
    c = c.replace(
        '<span class="rsb-split__eyebrow">What is it</span>\n        <h2>Classic straight-top noise wall for straightforward, reliable attenuation.</h2>',
        '<span class="rsb-split__eyebrow">What is it</span>\n        <h2>Classic straight-profile noise wall for straightforward, reliable attenuation.</h2>',
    )
    c = c.replace(
        '<p>Yukings flat-top noise barriers feature a clean, straight-profile top edge with standard modular panels stacked between hot-dip galvanized steel H-posts. The flat-top design minimizes tooling complexity, reduces per-meter manufacturing cost, and simplifies on-site panel handling and installation compared to shaped-top alternatives.</p>',
        '<p>Yukings flat panel noise barriers feature a clean, straight-profile form with standard modular panels stacked between hot-dip galvanized steel H-posts. The flat-form panel design minimizes tooling complexity, reduces per-meter manufacturing cost, and simplifies on-site panel handling and installation compared to shaped-top alternatives.</p>',
    )

    # Spec table heading + "Top Profile" row
    c = c.replace(
        '<h3>Flat Top Noise Barriers — Product Specification</h3><p>Classic straight-top profile with standard modular panel construction.</p>',
        '<h3>Flat Panel Noise Barriers — Product Specification</h3><p>Classic straight-profile form with standard modular panel construction.</p>',
    )
    c = c.replace(
        '<tr><td>Top Profile</td><td>flat / straight top edge</td></tr>',
        '<tr><td>Form / Shape</td><td>flat panel / straight profile</td></tr>',
    )
    c = c.replace(
        '<h2>Flat Top Noise Barriers — Full Specification</h2>',
        '<h2>Flat Panel Noise Barriers — Full Specification</h2>',
    )
    c = c.replace(
        '<p>Detailed engineering specification for Yukings flat-top noise barriers. All parameters align with EN 1793 / EN 1794 / EN 1991-1-4 testing and design standards.</p>',
        '<p>Detailed engineering specification for Yukings flat panel noise barriers. All parameters align with EN 1793 / EN 1794 / EN 1991-1-4 testing and design standards.</p>',
    )

    # Features section
    c = c.replace(
        '<h2>What makes our Flat Top Noise Barriers different</h2>',
        '<h2>What makes our Flat Panel Noise Barriers different</h2>',
    )
    c = c.replace(
        '<p>Straightforward manufacturing, standard component dimensions and full project traceability make Yukings flat-top noise barriers a reliable, cost-effective solution for any noise wall project.</p>',
        '<p>Straightforward manufacturing, standard component dimensions and full project traceability make Yukings flat panel noise barriers a reliable, cost-effective solution for any noise wall project.</p>',
    )
    c = c.replace('<h3>Standard Modular Panel</h3>', '<h3>Standard Modular Flat Panel</h3>')
    c = c.replace(
        '<h3>Straight-Top Profile</h3><p>Flat top-edge geometry is the reference specification for highways and railways worldwide; simple to fabricate and install.</p>',
        '<h3>Straight-Profile Form</h3><p>Flat panel form is the reference specification for highways and railways worldwide; simple to fabricate and install.</p>',
    )
    c = c.replace('<h3>22-38 dB Insertion Loss</h3>', '<h3>22-38 dB Insertion Loss</h3>')

    # Related products section heading + intro
    c = c.replace(
        '<h2>Other noise barrier profiles and solutions</h2>',
        '<h2>Other noise barrier forms and solutions</h2>',
    )
    c = c.replace(
        '<p>Compare flat-top barriers with Yukings curved-top and angled folded-top profiles, or explore our dedicated application-specific noise wall product lines.</p>',
        '<p>Compare flat panel barriers with Yukings curved-top and angled folded-top forms, or explore our semi-enclosed, fully-enclosed and application-specific noise wall product lines.</p>',
    )

    # FAQ section
    c = c.replace(
        '<h2>Flat Top Noise Barriers — FAQs</h2>',
        '<h2>Flat Panel Noise Barriers — FAQs</h2>',
    )
    c = c.replace(
        '<p>Commonly asked technical, commercial and logistics questions about Yukings flat-top noise barriers.</p>',
        '<p>Commonly asked technical, commercial and logistics questions about Yukings flat panel noise barriers.</p>',
    )

    # CTA heading
    c = c.replace(
        '<h2>Need a Flat / Straight Top Noise Barriers quotation for your project? Contact Yukings today.</h2>',
        '<h2>Need a Flat Panel Noise Barriers quotation for your project? Contact Yukings today.</h2>',
    )
    c = c.replace(
        '<p>Our flat-top noise barrier specialists will respond to your project inquiry within 24 hours, including technical guidance, panel dimension recommendations and project pricing where applicable.</p>',
        '<p>Our flat panel noise barrier specialists will respond to your project inquiry within 24 hours, including technical guidance, panel dimension recommendations and project pricing where applicable.</p>',
    )

    # Form
    c = c.replace(
        '<h2>Tell us about your flat-top noise barrier project</h2>',
        '<h2>Tell us about your flat panel noise barrier project</h2>',
    )
    c = c.replace(
        '<h3>Project Quote Request — Flat Top Noise Barriers</h3>',
        '<h3>Project Quote Request — Flat Panel Noise Barriers</h3>',
    )
    c = c.replace(
        '<p>Share your project parameters and a Yukings engineer will prepare a tailored proposal, including panel dimensions, H-post spacing, barrier height and estimated attenuation performance.</p>',
        '<p>Share your project parameters and a Yukings engineer will prepare a tailored proposal, including panel dimensions, H-post spacing, barrier height and estimated attenuation performance.</p>',
    )

    # isRelatedTo - add semi and fully enclosed
    c = c.replace(
        '"isRelatedTo":[{"@type":"Product","name":"Galvanized Steel Noise Barriers","url":"https://www.yukings.net/galvanized-steel-noise-barriers.html"},{"@type":"Product","name":"All Noise Barrier Products","url":"https://www.yukings.net/products.html"}]',
        '"isRelatedTo":[{"@type":"Product","name":"Galvanized Steel Noise Barriers","url":"https://www.yukings.net/galvanized-steel-noise-barriers.html"},{"@type":"Product","name":"Curved / Arched Top Noise Barriers","url":"https://www.yukings.net/curved-top-noise-barriers.html"},{"@type":"Product","name":"Angled / Folded L-Cap Top Noise Barriers","url":"https://www.yukings.net/angled-folded-top-noise-barriers.html"},{"@type":"Product","name":"Semi-Enclosed / U-Shaped Noise Barriers","url":"https://www.yukings.net/semi-enclosed-noise-barriers.html"},{"@type":"Product","name":"Fully-Enclosed / Acoustic Tunnel Noise Barriers","url":"https://www.yukings.net/fully-enclosed-noise-barriers.html"},{"@type":"Product","name":"All Noise Barrier Products","url":"https://www.yukings.net/products.html"}]',
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated flat-top-noise-barriers.html")


# ============================================================
# 2. Update curved-top-noise-barriers.html
# ============================================================
def update_curved_top():
    path = f"{HTML_DIR}/curved-top-noise-barriers.html"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # Title
    c = c.replace(
        "<title>Curved / Arc Top Noise Barriers | Yukings</title>",
        "<title>Curved / Arched Top Noise Barriers | Yukings</title>",
    )
    # description
    c = c.replace(
        '<meta name="description" content="Curved and arc-top noise barriers with engineered curved-cap profile delivering 3-8 dB additional diffraction attenuation over flat-top walls. CE certified. Request a free quote.">',
        '<meta name="description" content="Curved and arched top noise barriers with engineered arc profile delivering 3-8 dB additional diffraction attenuation over flat-top walls. CE / ISO certified. Request a free quote.">',
    )
    # keywords
    c = c.replace(
        '<meta name="keywords" content="curved top noise barrier, arc cap sound barrier, curved-top acoustic barrier, curved cap noise wall, Yukings curved top noise barrier manufacturer">',
        '<meta name="keywords" content="curved top noise barrier, arched profile sound barrier, curved cap acoustic barrier, radius top noise wall, Yukings curved top noise barrier manufacturer">',
    )
    # og:title / twitter:title
    c = c.replace(
        '<meta property="og:title" content="Curved / Arc Top Noise Barriers">',
        '<meta property="og:title" content="Curved / Arched Top Noise Barriers">',
    )
    c = c.replace(
        '<meta name="twitter:title" content="Curved / Arc Top Noise Barriers">',
        '<meta name="twitter:title" content="Curved / Arched Top Noise Barriers">',
    )
    # og:description / twitter:description
    c = c.replace(
        '<meta property="og:description" content="Curved and arc-top noise barriers with engineered curved-cap profile delivering 3-8 dB additional diffraction attenuation over flat-top walls. CE certified. Request a free quote.">',
        '<meta property="og:description" content="Curved and arched top noise barriers with engineered arc profile delivering 3-8 dB additional diffraction attenuation over flat-top walls. CE / ISO certified. Request a free quote.">',
    )
    c = c.replace(
        '<meta name="twitter:description" content="Curved and arc-top noise barriers with engineered curved-cap profile delivering 3-8 dB additional diffraction attenuation over flat-top walls. CE certified. Request a free quote.">',
        '<meta name="twitter:description" content="Curved and arched top noise barriers with engineered arc profile delivering 3-8 dB additional diffraction attenuation over flat-top walls. CE / ISO certified. Request a free quote.">',
    )

    # Product JSON-LD
    c = c.replace(
        '"name":"Curved / Arc Top Noise Barriers"',
        '"name":"Curved / Arched Top Noise Barriers"',
    )
    c = c.replace(
        '"description":"Curved-cap (arc-top) noise barriers featuring an engineered curved top profile that redirects diffracted sound waves over the barrier top, providing 3-8 dB additional attenuation compared to an equivalent-height flat-top barrier."',
        '"description":"Curved and arched top noise barriers featuring an engineered arc cap profile that redirects diffracted sound waves, adding 3-8 dB of additional attenuation compared to equivalent flat-top barriers."',
    )
    c = c.replace('"sku":"YK-CURVED-ARC"', '"sku":"YK-CURVED-TOP"')
    c = c.replace('"productID":"YK-CURVED-ARC"', '"productID":"YK-CURVED-TOP"')
    c = c.replace(
        '"material":"Galvanized steel perforated absorptive panels with factory-formed curved cap, standard H-beam posts"',
        '"material":"DX51D+Z galvanized steel perforated absorptive panels with factory-formed arched cap, standard H-beam posts"',
    )

    # BreadcrumbList
    c = c.replace(
        '{"@type":"ListItem","position":3,"name":"Curved Top Noise Barriers","item":"https://www.yukings.net/curved-top-noise-barriers.html"}',
        '{"@type":"ListItem","position":3,"name":"Curved / Arched Top Noise Barriers","item":"https://www.yukings.net/curved-top-noise-barriers.html"}',
    )
    # Breadcrumb HTML
    c = c.replace(
        '<span class="rsb-breadcrumb__current">Curved Top Noise Barriers</span>',
        '<span class="rsb-breadcrumb__current">Curved / Arched Top Noise Barriers</span>',
    )

    # Hero h1
    c = c.replace(
        '<h1 id="hero-title">Curved &amp; arc-top noise barriers — engineered curved-cap profile that diffracts sound waves over the barrier top for <span>3-8 dB additional</span> attenuation compared to flat-top walls.</h1>',
        '<h1 id="hero-title">Curved / arched top noise barriers — engineered arc-profile cap that diffracts sound waves over the barrier top for <span>3-8 dB additional</span> attenuation.</h1>',
    )

    # Hero lede
    c = c.replace(
        '<p class="lede">Yukings curved-top (arc-top) noise barriers feature an engineered curved-cap profile that redirects diffracted sound waves over the top of the barrier. Independent testing confirms +3 to +8 dB additional insertion loss compared to equivalent-height flat-top noise walls, making the curved-top profile ideal for high-speed rail corridors, urban expressway corridors and sensitive receiver zones.</p>',
        '<p class="lede">Yukings curved / arched top noise barriers feature an engineered arc cap profile that redirects diffracted sound waves over the top of the barrier. Independent testing confirms +3 to +8 dB additional insertion loss compared to equivalent-height flat-top noise walls, making the arched-top form ideal for high-speed rail corridors, urban expressways and sensitive receiver zones.</p>',
    )

    # Hero chips
    c = c.replace(
        '<span class="rsb-hero__chip">Curved-Cap Profile</span><span class="rsb-hero__chip">+3-8 dB Extra Attenuation</span><span class="rsb-hero__chip">Aerodynamic Shape</span><span class="rsb-hero__chip">HSR Slipstream Friendly</span><span class="rsb-hero__chip">Visually Softer Profile</span>',
        '<span class="rsb-hero__chip">Arc-Profile Cap</span><span class="rsb-hero__chip">+3-8 dB Extra Attenuation</span><span class="rsb-hero__chip">Aerodynamic Shape</span><span class="rsb-hero__chip">HSR Slipstream Friendly</span><span class="rsb-hero__chip">Visually Softer Profile</span>',
    )

    # Product overview headings
    c = c.replace(
        '<h2>Curved / Arc Top Noise Barriers — Enhanced Diffraction Attenuation</h2>',
        '<h2>Curved / Arched Top Noise Barriers — Enhanced Diffraction Attenuation</h2>',
    )
    c = c.replace(
        '<p>The curved-cap (arc-top) profile is a performance-enhanced noise wall geometry that replaces the standard straight top edge with a factory-formed curved cap. This shaped-top profile redirects diffracted sound waves over the top of the barrier, delivering measurably higher insertion loss than an equivalent-height flat-top wall.</p>',
        '<p>The arched-cap (arc-top) profile is a performance-enhanced noise wall geometry that replaces the standard straight top edge with a factory-formed arched cap. This shaped-top form redirects diffracted sound waves over the top of the barrier, delivering measurably higher insertion loss than an equivalent-height flat panel wall.</p>',
    )

    # Split section
    c = c.replace(
        '<h2>Engineered curved-cap profile for enhanced diffraction attenuation.</h2>',
        '<h2>Engineered arched-cap profile for enhanced diffraction attenuation.</h2>',
    )
    c = c.replace(
        '<p>Yukings curved-top noise barriers feature a factory-formed galvanized steel curved cap integrated with standard modular absorptive panels. The curved-cap geometry is engineered to redirect sound waves diffracting over the barrier top, providing +3 to +8 dB of additional insertion loss without increasing barrier height. The curved-cap profile is also aerodynamically shaped, making it well-suited for high-speed rail applications where slipstream pressure and fatigue loads are a concern.</p>',
        '<p>Yukings curved-top noise barriers feature a factory-formed galvanized steel arched cap integrated with standard modular absorptive panels. The arched-cap geometry is engineered to redirect sound waves diffracting over the barrier top, providing +3 to +8 dB of additional insertion loss without increasing barrier height. The arched-cap profile is also aerodynamically shaped, making it well-suited for high-speed rail applications where slipstream pressure and fatigue loads are a concern.</p>',
    )

    # Spec table
    c = c.replace(
        '<h2>Curved / Arc Top Noise Barriers — Full Specification</h2>',
        '<h2>Curved / Arched Top Noise Barriers — Full Specification</h2>',
    )
    c = c.replace(
        '<h3>Curved / Arc Top Noise Barriers — Product Specification</h3><p>Engineered curved-cap profile with standard modular panel construction and factory-formed arched top cap.</p>',
        '<h3>Curved / Arched Top Noise Barriers — Product Specification</h3><p>Engineered arc-cap profile with standard modular panel construction and factory-formed arched top cap.</p>',
    )
    c = c.replace(
        '<tr><td>Top Profile</td><td>curved / arc cap (factory formed)</td></tr>',
        '<tr><td>Form / Shape</td><td>curved / arched cap top</td></tr>',
    )

    # Features section
    c = c.replace(
        '<h2>What makes our Curved / Arc Top Noise Barriers different</h2>',
        '<h2>What makes our Curved / Arched Top Noise Barriers different</h2>',
    )
    c = c.replace(
        '<p>The curved-cap profile delivers real, measurable performance gains over flat-top barriers without adding height — tested and documented with EN 1793 insertion loss data for every Yukings curved-top noise barrier project.</p>',
        '<p>The arched-cap profile delivers real, measurable performance gains over flat panel barriers without adding height — tested and documented with EN 1793 insertion loss data for every Yukings curved-top noise barrier project.</p>',
    )
    c = c.replace('<h3>Curved-Cap Profile</h3>', '<h3>Arched-Cap Profile</h3>')

    # Related products intro
    c = c.replace(
        '<p>Compare curved-top barriers with Yukings flat-top and angled folded-top profiles, or explore our dedicated application-specific noise wall product lines.</p>',
        '<p>Compare curved-top barriers with Yukings flat panel and angled folded-top forms, or explore our semi-enclosed, fully-enclosed and application-specific noise wall product lines.</p>',
    )

    # FAQ
    c = c.replace(
        '<h2>Curved / Arc Top Noise Barriers — FAQs</h2>',
        '<h2>Curved / Arched Top Noise Barriers — FAQs</h2>',
    )

    # CTA heading
    c = c.replace(
        '<h2>Need a Curved / Arc Top Noise Barriers quotation for your project? Contact Yukings today.</h2>',
        '<h2>Need a Curved / Arched Top Noise Barriers quotation for your project? Contact Yukings today.</h2>',
    )
    c = c.replace(
        '<p>Our curved-top noise barrier specialists will respond to your project inquiry within 24 hours, including technical guidance, arched-cap dimension recommendations and project pricing where applicable.</p>',
        '<p>Our curved-top noise barrier specialists will respond to your project inquiry within 24 hours, including technical guidance, arched-cap dimension recommendations and project pricing where applicable.</p>',
    )

    # Form
    c = c.replace(
        '<h2>Tell us about your curved-top noise barrier project</h2>',
        '<h2>Tell us about your curved / arched top noise barrier project</h2>',
    )
    c = c.replace(
        '<h3>Project Quote Request — Curved / Arc Top Noise Barriers</h3>',
        '<h3>Project Quote Request — Curved / Arched Top Noise Barriers</h3>',
    )

    # isRelatedTo - add semi and fully enclosed
    c = c.replace(
        '"isRelatedTo":[{"@type":"Product","name":"Galvanized Steel Noise Barriers","url":"https://www.yukings.net/galvanized-steel-noise-barriers.html"},{"@type":"Product","name":"All Noise Barrier Products","url":"https://www.yukings.net/products.html"}]',
        '"isRelatedTo":[{"@type":"Product","name":"Galvanized Steel Noise Barriers","url":"https://www.yukings.net/galvanized-steel-noise-barriers.html"},{"@type":"Product","name":"Flat Panel / Straight Panel Noise Barriers","url":"https://www.yukings.net/flat-top-noise-barriers.html"},{"@type":"Product","name":"Angled / Folded L-Cap Top Noise Barriers","url":"https://www.yukings.net/angled-folded-top-noise-barriers.html"},{"@type":"Product","name":"Semi-Enclosed / U-Shaped Noise Barriers","url":"https://www.yukings.net/semi-enclosed-noise-barriers.html"},{"@type":"Product","name":"Fully-Enclosed / Acoustic Tunnel Noise Barriers","url":"https://www.yukings.net/fully-enclosed-noise-barriers.html"},{"@type":"Product","name":"All Noise Barrier Products","url":"https://www.yukings.net/products.html"}]',
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated curved-top-noise-barriers.html")


# ============================================================
# 3. Update angled-folded-top-noise-barriers.html
# ============================================================
def update_angled_top():
    path = f"{HTML_DIR}/angled-folded-top-noise-barriers.html"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # Title
    c = c.replace(
        "<title>Angled / Folded-Top Noise Barriers | Yukings</title>",
        "<title>Angled / Folded Top Noise Barriers | Yukings</title>",
    )
    # description
    c = c.replace(
        '<meta name="description" content="Angled and L-shaped folded cantilever cap top noise barriers creating an extended acoustic shadow zone behind the barrier. Highest effective dB per meter height. CE certified. Request a free quote.">',
        '<meta name="description" content="Angled and L-shaped folded cantilever cap top noise barriers creating an extended acoustic shadow zone behind the barrier. Highest effective dB per meter height. Request a free quote.">',
    )
    # keywords
    c = c.replace(
        '<meta name="keywords" content="angled top noise barrier, folded cap sound barrier, L-cantilever top acoustic barrier, horizontal overhang noise wall, Yukings angled folded-top noise barrier manufacturer">',
        '<meta name="keywords" content="angled top noise barrier, L-shaped cantilever cap sound barrier, folded top acoustic barrier, horizontal overhang noise wall, Yukings angled folded top noise barrier">',
    )
    # og:title / twitter:title
    c = c.replace(
        '<meta property="og:title" content="Angled / Folded-Top Noise Barriers">',
        '<meta property="og:title" content="Angled / Folded Top Noise Barriers">',
    )
    c = c.replace(
        '<meta name="twitter:title" content="Angled / Folded-Top Noise Barriers">',
        '<meta name="twitter:title" content="Angled / Folded Top Noise Barriers">',
    )
    # og:description / twitter:description
    c = c.replace(
        '<meta property="og:description" content="Angled and L-shaped folded cantilever cap top noise barriers creating an extended acoustic shadow zone behind the barrier. Highest effective dB per meter height. CE certified. Request a free quote.">',
        '<meta property="og:description" content="Angled and L-shaped folded cantilever cap top noise barriers creating an extended acoustic shadow zone behind the barrier. Highest effective dB per meter height. Request a free quote.">',
    )
    c = c.replace(
        '<meta name="twitter:description" content="Angled and L-shaped folded cantilever cap top noise barriers creating an extended acoustic shadow zone behind the barrier. Highest effective dB per meter height. CE certified. Request a free quote.">',
        '<meta name="twitter:description" content="Angled and L-shaped folded cantilever cap top noise barriers creating an extended acoustic shadow zone behind the barrier. Highest effective dB per meter height. Request a free quote.">',
    )

    # Product JSON-LD
    c = c.replace(
        '"name":"Angled / Folded-Top Noise Barriers"',
        '"name":"Angled / Folded L-Cap Top Noise Barriers"',
    )
    c = c.replace(
        '"description":"Angled, folded and L-shaped cantilever cap top noise barriers creating an extended acoustic shadow zone behind the barrier for maximum effective insertion loss per meter of barrier height."',
        '"description":"Angled, folded and L-shaped cantilever cap top noise barriers creating an extended acoustic shadow zone behind the barrier for maximum effective insertion loss per meter of barrier height."',
    )
    c = c.replace('"sku":"YK-ANGLED-TOP"', '"sku":"YK-ANGLED-TOP"')

    # BreadcrumbList
    c = c.replace(
        '{"@type":"ListItem","position":3,"name":"Angled Top Noise Barriers","item":"https://www.yukings.net/angled-folded-top-noise-barriers.html"}',
        '{"@type":"ListItem","position":3,"name":"Angled / Folded Top Noise Barriers","item":"https://www.yukings.net/angled-folded-top-noise-barriers.html"}',
    )
    # Breadcrumb HTML
    c = c.replace(
        '<span class="rsb-breadcrumb__current">Angled Top Noise Barriers</span>',
        '<span class="rsb-breadcrumb__current">Angled / Folded Top Noise Barriers</span>',
    )

    # Hero h1
    c = c.replace(
        '<h1 id="hero-title">Angled &amp; folded-top noise barriers — L-shaped cantilever cap that creates an extended <span>acoustic shadow zone</span> behind the barrier for maximum dB-per-meter-height performance.</h1>',
        '<h1 id="hero-title">Angled, folded &amp; L-shaped cantilever cap top noise barriers creating an extended <span>acoustic shadow zone</span> behind the barrier for maximum effective insertion loss.</h1>',
    )

    # Hero lede
    c = c.replace(
        '<p class="lede">Yukings angled (folded-top / L-shaped cantilever cap) noise barriers feature a horizontal overhang cap element that extends the acoustic shadow zone behind the barrier. Independent testing confirms highest effective insertion loss per meter of barrier height compared to flat-top and curved-top alternatives, making angled-top barriers the preferred geometry for high-speed rail corridors, urban expressway noise control and sensitive receiver zones.</p>',
        '<p class="lede">Yukings angled, folded and L-shaped cantilever cap top noise barriers feature a horizontal overhang cap element that extends the acoustic shadow zone behind the barrier. Independent testing confirms highest effective insertion loss per meter of barrier height compared to flat panel and curved-top alternatives, making angled-top forms the preferred geometry for high-speed rail corridors, urban expressway noise control and sensitive receiver zones.</p>',
    )

    # Hero chips
    c = c.replace(
        '<span class="rsb-hero__chip">L-Cap Cantilever Profile</span><span class="rsb-hero__chip">Extended Acoustic Shadow Zone</span><span class="rsb-hero__chip">Highest dB Per Meter Height</span><span class="rsb-hero__chip">HSR Noise Effective</span><span class="rsb-hero__chip">Residential Friendly</span>',
        '<span class="rsb-hero__chip">L-Cap Cantilever Profile</span><span class="rsb-hero__chip">Extended Acoustic Shadow Zone</span><span class="rsb-hero__chip">Highest dB per Meter Height</span><span class="rsb-hero__chip">HSR Noise Effective</span><span class="rsb-hero__chip">Residential-Friendly</span>',
    )

    # Product overview
    c = c.replace(
        '<h2>Angled / Folded-Top Noise Barriers — Extended Acoustic Shadow</h2>',
        '<h2>Angled / Folded Top Noise Barriers — Extended Acoustic Shadow</h2>',
    )
    c = c.replace(
        '<p>The angled (folded-top / L-shaped cantilever cap) profile is the highest-performing roadside barrier geometry for effective insertion loss per meter of barrier height. The horizontal overhang cap element creates an extended acoustic shadow zone behind the barrier by reducing the angle of sound wave diffraction over the top edge.</p>',
        '<p>The angled (folded / L-shaped cantilever cap) form is the highest-performing roadside barrier geometry for effective insertion loss per meter of barrier height. The horizontal overhang cap element creates an extended acoustic shadow zone behind the barrier by reducing the angle of sound wave diffraction over the top edge.</p>',
    )

    # Split section
    c = c.replace(
        '<h2>Folded-top L-shaped cantilever cap for maximum effective attenuation per meter of height.</h2>',
        '<h2>Folded L-shaped cantilever cap for maximum effective attenuation per meter of height.</h2>',
    )

    # Spec table
    c = c.replace(
        '<h2>Angled / Folded-Top Noise Barriers — Full Specification</h2>',
        '<h2>Angled / Folded Top Noise Barriers — Full Specification</h2>',
    )
    c = c.replace(
        '<h3>Angled / Folded-Top Noise Barriers — Product Specification</h3><p>L-shaped cantilever cap profile with standard modular panel construction and factory-formed horizontal overhang cap.</p>',
        '<h3>Angled / Folded Top Noise Barriers — Product Specification</h3><p>L-shaped cantilever cap form with standard modular panel construction and factory-formed horizontal overhang cap.</p>',
    )
    c = c.replace(
        '<tr><td>Top Profile</td><td>angled / folded L-shaped cantilever cap</td></tr>',
        '<tr><td>Form / Shape</td><td>angled / folded L-shaped cantilever cap top</td></tr>',
    )

    # Features section
    c = c.replace(
        '<h2>What makes our Angled / Folded-Top Noise Barriers different</h2>',
        '<h2>What makes our Angled / Folded Top Noise Barriers different</h2>',
    )

    # Related products intro
    c = c.replace(
        '<p>Compare angled-top barriers with Yukings flat-top and curved-cap profiles, or explore our dedicated application-specific noise wall product lines.</p>',
        '<p>Compare angled-top barriers with Yukings flat panel and curved-top forms, or explore our semi-enclosed, fully-enclosed and application-specific noise wall product lines.</p>',
    )

    # FAQ
    c = c.replace(
        '<h2>Angled / Folded-Top Noise Barriers — FAQs</h2>',
        '<h2>Angled / Folded Top Noise Barriers — FAQs</h2>',
    )

    # CTA heading
    c = c.replace(
        '<h2>Need an Angled / Folded-Top Noise Barriers quotation for your project? Contact Yukings today.</h2>',
        '<h2>Need an Angled / Folded Top Noise Barriers quotation for your project? Contact Yukings today.</h2>',
    )
    c = c.replace(
        '<p>Our angled-top noise barrier specialists will respond to your project inquiry within 24 hours, including technical guidance, L-cap dimension recommendations and project pricing where applicable.</p>',
        '<p>Our angled-top noise barrier specialists will respond to your project inquiry within 24 hours, including technical guidance, L-cap dimension recommendations and project pricing where applicable.</p>',
    )

    # Form
    c = c.replace(
        '<h2>Tell us about your angled-top noise barrier project</h2>',
        '<h2>Tell us about your angled / folded top noise barrier project</h2>',
    )
    c = c.replace(
        '<h3>Project Quote Request — Angled / Folded-Top Noise Barriers</h3>',
        '<h3>Project Quote Request — Angled / Folded Top Noise Barriers</h3>',
    )

    # isRelatedTo - add semi and fully enclosed
    c = c.replace(
        '"isRelatedTo":[{"@type":"Product","name":"Galvanized Steel Noise Barriers","url":"https://www.yukings.net/galvanized-steel-noise-barriers.html"},{"@type":"Product","name":"All Noise Barrier Products","url":"https://www.yukings.net/products.html"}]',
        '"isRelatedTo":[{"@type":"Product","name":"Galvanized Steel Noise Barriers","url":"https://www.yukings.net/galvanized-steel-noise-barriers.html"},{"@type":"Product","name":"Flat Panel / Straight Panel Noise Barriers","url":"https://www.yukings.net/flat-top-noise-barriers.html"},{"@type":"Product","name":"Curved / Arched Top Noise Barriers","url":"https://www.yukings.net/curved-top-noise-barriers.html"},{"@type":"Product","name":"Semi-Enclosed / U-Shaped Noise Barriers","url":"https://www.yukings.net/semi-enclosed-noise-barriers.html"},{"@type":"Product","name":"Fully-Enclosed / Acoustic Tunnel Noise Barriers","url":"https://www.yukings.net/fully-enclosed-noise-barriers.html"},{"@type":"Product","name":"All Noise Barrier Products","url":"https://www.yukings.net/products.html"}]',
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated angled-folded-top-noise-barriers.html")


if __name__ == "__main__":
    update_flat_top()
    update_curved_top()
    update_angled_top()
