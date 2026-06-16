#!/usr/bin/env python3
"""Yukings site generator - pages (part 4): blog, faqs, about, contact, get-quote, privacy, terms."""
import sys
sys.path.insert(0, "/workspace")
from _helpers import *

def page_blog():
    b=[]
    b.append(page_head(
        "Noise Barrier Blog | Yukings - Technical Articles, Industry News, FAQs",
        "Technical articles and industry news on noise barriers, sound walls, acoustic design, standards compliance, and noise barrier technology.",
        "blog.html"))
    b.append(breadcrumb([("Home","index.html"),("Blog",None)]))
    b.append(hero(
        "Ideas, engineering and industry __SPAN__ for noise barriers.",
        "insights",
        "Articles on noise barrier design, acoustic engineering, regulatory compliance, and case studies and best practices. Updated regularly with engineering notes from the Yukings R&D team.",
        "noise-barrier-blog-technical-articles-engineering-insight-lab",
        chips=["Technical Articles","Industry News","FAQs Deep Dive","Standards & Certifications","Global"],
        actions=[("primary","Get the Yukings Newsletter","get-quote.html"),("ghost","Ask an Engineer","contact.html")],
        stats=[("50+","articles published"),("12 yr","track record"),("18+","writing years")]))

    articles = [
        ("How to choose the right noise barrier panel depth","Technical Article \u00b7 8 min read","A practical guide to selecting the right panel depth for your noise barrier project, starting from source level, distance to receiver and required insertion loss using EN 1793.",
         "Read more","blog.html","how-to-choose-noise-barrier-panel-depth","TECHNICAL"),
        ("Understanding EN 1793-1 acoustic performance classification","Technical Article \u00b7 11 min read","Explaining EN 1793-1 single-number ratings for road traffic noise and how to read an acoustic report and use it to compare products.","Read more","blog.html","en-1793-acoustic-performance-classification","TECHNICAL"),
        ("Aero-acoustic pulse: high-speed rail barrier design","Technical Article \u00b7 14 min read","High-speed rail noise barriers must resist repeated aero-acoustic pulse. Here is how Yukings designs them.","Read more","blog.html","high-speed-rail-aero-acoustic-noise-barriers","TECHNICAL"),
        ("Solar PV-integrated noise barriers: commercial guide","Industry News \u00b7 9 min read","Noise barriers that also generate electricity. A commercial overview of solar-integrated acoustic barriers for highways.","Read more","blog.html","solar-pv-integrated-noise-barriers","NEWS"),
        ("Choosing between aluminum and galvanized steel noise barriers","Industry News \u00b7 7 min read","When to choose aluminum alloy noise barriers and when to specify galvanized steel for your project.","Read more","blog.html","aluminum-galvanized-steel-noise-barrier-comparison","NEWS"),
        ("EN 1794 mechanical performance and durability explained","Industry News \u00b7 10 min read","An engineer’s take on EN 1794-1 / -2 mechanical performance and durability testing of noise barriers.","Read more","blog.html","en-1794-mechanical-performance-noise-barriers","NEWS"),
        ("FAQ deep dive: insertion loss, sound insulation and absorption coefficients","FAQ \u00b7 6 min read","Deep-dive into DL (insertion loss) vs Rw (sound insulation) vs alpha-w (absorption coefficient).","Read more","blog.html","insertion-loss-sound-insulation-absorption-coefficients-noise-barriers","FAQ"),
        ("Noise barrier project checklist for bidding and construction","Technical Article \u00b7 12 min read","A practical project-level checklist for noise barrier projects, from specification through to commissioning.","Read more","blog.html","noise-barrier-project-checklist","TECHNICAL"),
        ("Global noise barrier market snapshot: EU, USA, Australia, Southeast Asia","Industry News \u00b7 8 min read","A snapshot of the noise barrier market across the EU, the US, Australia and Southeast Asia.","Read more","blog.html","global-noise-barrier-market-eu-usa-australia-southeast-asia","NEWS"),
    ]
    cards = "".join(card(*a) for a in articles)
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Latest Articles","Technical notes, industry news and FAQ deep dives")}
    <div class="rsb-grid rsb-grid--3" style="grid-template-columns:repeat(3,1fr)">
      {cards}
    </div>
  </div>
</section>""")

    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Three Editorial Streams","How we write for engineers, specifiers and procurement teams")}
    {split_block("noise-barrier-technical-article-engineering-2","Technical Articles","For the engineers and specifiers who want to dig into the technical details of noise barrier design, specification, standards and engineering.",["Deep dives into EN 1793 / 1794 / ASTM E90 / GB/T 34509 standards, case studies with real-world acoustic modelling, and comparison of material selection."],[("primary","Browse Technical Articles","blog.html"),("ghost-alt","Request a Technical Consultation","get-quote.html")])}
    {split_block("noise-barrier-industry-news-2","Industry News","For project owners, developers, contractors and procurement teams tracking the global noise barrier market.",["Coverage of noise barrier market trends, tendering practices, procurement models and regulatory updates across EU, US, Australia and emerging markets."],[("primary","Browse Industry News","blog.html"),("ghost-alt","Subscribe to Newsletter","get-quote.html")], reverse=True)}
    {split_block("noise-barrier-faq-deep-dive","FAQs Deep Dive","Dig into the questions we receive most often at Yukings, answered with engineering-level detail.",["Bigger answers on warranties, CE certification, EN 1793 single-number ratings, sample requests, and shipping lead times."],[("primary","Browse FAQs","faqs.html"),("ghost-alt","Submit Your Question","contact.html")])}
  </div>
</section>""")

    b.append(stat_section([
        ("50+","published articles"),
        ("12","years of editorial track record"),
        ("3","editorial streams"),
        ("4","engineering contributors"),
    ]))
    b.append(cta_section(
        "Subscribe to the Yukings engineering newsletter - and get our best content each quarter.",
        "Get a curated quarterly digest of noise barrier engineering articles, delivered to your inbox. No spam - just engineering, case studies and product updates from Yukings."))
    b.append(page_close())
    return "".join(b)

def page_faqs():
    b=[]
    b.append(page_head(
        "Noise Barrier FAQs | Yukings - Lead time, warranty, certification, samples, shipping, OEM",
        "Frequently asked questions about Yukings noise barriers - lead times, warranties, certifications, sample requests, OEM, shipping and installation.",
        "faqs.html"))
    b.append(breadcrumb([("Home","index.html"),("FAQs",None)]))
    b.append(hero(
        "Answers to the questions we hear __SPAN__.",
        "most often",
        "From lead times and warranty to OEM custom manufacturing, certifications and shipping lead times, samples and technical support. If you cannot find what you need here, our engineers are one click away.",
        "yukings-noise-barrier-faqs-helpdesk-support",
        chips=["Certifications","Warranty & Lifespan","Samples","OEM Manufacturing","Shipping and Installation","Shipping"],
        actions=[("primary","Submit a Question","contact.html"),("ghost","Request a Quote","get-quote.html")],
        stats=[("24h","response time"),("15 yr","warranty"),("42,000 m\u00b2","factory"),("60+","countries served")]))

    b.append(faq_section([
        ("Where is Yukings based, and where is your factory?",
         "Yukings is based in Shenzhen, Guangdong, China. Our primary manufacturing plant occupies over 42,000 m\u00b2 of purpose-built noise barrier production floor. We also maintain a secondary facility for specialized aluminum alloy panel fabrication and an in-house acoustic testing lab. Contact page includes full address details."),
        ("What is the typical lead time for Yukings noise barrier orders?",
         "Standard Yukings noise barrier panels (2,500 x 500 mm, 80-140 mm depths) ship within 20 working days from order confirmation. Custom-engineered panels, PV-integrated solar noise barriers and large-volume projects typically ship within 40 working days."),
        ("Do you offer custom / OEM noise barrier manufacturing?",
         "Yes. Yukings has manufactured noise barriers for 18+ years on an OEM/ODM basis. We support custom colors, custom panel depths, custom perforation patterns, custom heights, custom project-specific designs, project-specific drawings. Our team can review your drawings and deliver custom panels. Our team can review your project requirements and deliver a full design, we deliver a fully custom panel system, custom finishes, green-wall integrations, and full custom panel configurations and custom finishing."),
        ("Do you provide acoustic simulation, drawings and BIM?",
         "Yes. Our engineering team delivers acoustic simulation (CNOSSOS-EU / FHWA TNM 2.5), structural calculation, and AutoCAD 2D + Revit BIM drawings for every project at no extra cost when a formal PO is placed with Yukings. Full engineering deliverables are always included in our project price."),
        ("Can I request samples and test reports?",
         "Absolutely. Yukings ships noise barrier sample panels (typically 500 x 500 mm) together with CE / ISO test reports, acoustic insertion loss curves, and material certificates to any project engineer or buyer upon request."),
        ("What certifications do your noise barriers carry?",
         "Yukings noise barriers are produced in compliance with EN 1793-1/-2/-5 (acoustic performance), EN 1794-1/-2 (mechanical performance and durability), ASTM E90 and ASTM C423, plus the Chinese national noise barrier standard GB/T 34509. Our factory management system is ISO 9001 / 14001 / 45001 certified."),
        ("Do you export to Europe, USA, Australia, and Southeast Asia?",
         "Yes. Yukings ships noise barriers to more than 60+ countries across North America, Europe, Australia, Southeast Asia and the Middle East. We handle containerized FOB / CIF / DAP shipping and provide full shipping documents (packing list, commercial invoice, certificate of origin, test reports, CE declaration of conformity (DoC)."),
        ("What warranty does Yukings provide on its noise barrier products?",
         "All standard Yukings noise barrier panels carry a 15-year structural warranty against manufacturing defects under normal use, with a designed service life of 25 years. Acoustic performance is warranted to remain within +/- 2 dB of the published rating for the warranty period."),
        ("What are your payment terms?",
         "Our standard payment terms are 30% deposit on order confirmation, 60% prior to shipment, and 10% final against acceptance documents. Project-specific payment terms, including letter of credit, are available for major projects and are subject to credit review."),
        ("What is your minimum order quantity (MOQ)?",
         "For standard noise barrier panels our MOQ is one 40ft HC container (approximately 1,200 m2 of panel surface, subject to panel depth). Sample orders and custom-engineered projects are evaluated on a project-specific basis with no fixed MOQ."),
        ("Do you provide installation supervision and turnkey installation?",
         "Yes. Yukings provides turnkey installation crews and/or site supervision by certified Yukings engineers internationally, depending on project size, location, and complexity of the site-specific requirements. We also ship our clients, our site, on our own site, on our own terms and the Yukings provides turnkey installation crews, our installation site"),
        ("How are panels packaged and shipped?",
         "Panels are packed in corrugated cartons on heat-sealed plastic bags on wooden pallets or in specially designed steel stillages for heavy-duty items. H-beam posts are strapped and racked, wrapped and strapped with stretch wrap and clearly marked with part numbers, project codes and shipping marks, bar codes. Full shipping marks with part numbers. Full documents including part, container numbers project codes and barcodes are delivered with every shipment."),
    ], title="Frequently Asked Questions"))
    b.append(cta_section(
        "Still have a question? Contact the Yukings noise barrier helpdesk today.",
        "Our technical sales engineers answer every question within 24 hours. For project-specific questions, please include your project location, approximate barrier length and any relevant noise level data you may already have."))
    b.append(page_close())
    return "".join(b)

def page_about():
    b=[]
    b.append(page_head(
        "About Yukings | Noise Barrier Manufacturer Since 2006",
        "Yukings is a Shenzhen-based noise barrier manufacturer with 18+ years OEM/ODM experience, a 42,000 m² factory, exporting to 60+ countries. CE & ISO 9001 certified. Meet our team, tour our factory.",
        "about.html"))
    b.append(breadcrumb([("Home","index.html"),("About Us",None)]))
    b.append(hero(
        "A manufacturer of noise barriers since __SPAN__.",
        "engineers of acoustic barriers since 2006",
        "Shenzhen Yukings Industrial Co., Ltd. (Yukings) is a privately-owned, family-managed noise barrier manufacturer founded in 2006 in Shenzhen, China. We design, manufacture and deliver performance-rated noise barriers, sound walls and acoustic barriers for highway, railway, industrial, residential and solar infrastructure projects worldwide.",
        "yukings-noise-barrier-manufacturer-shenzhen-factory-aerial",
        chips=["ISO 9001 / 14001 / 45001","CE Certified","18+ Years Experience","42,000 m2 Factory"],
        actions=[("primary","Get the Company Brochure","get-quote.html"),("ghost","Visit Our Factory","contact.html")],
        stats=[("2006","founded"),("42,000 m2","factory floor"),("18+","years in business"),("60+","export countries")]))

    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Who We Are","A manufacturer of acoustic barriers with engineering at our core")}
    {split_block("yukings-noise-barrier-manufacturer-shenzhen-office-front","Company Profile",
                  "Yukings is a Shenzhen, China-based noise barrier manufacturer with a 42,000 m\u00b2 purpose-built factory, 18+ years of manufacturing history and a team of 120+ employees, of whom 40 are engineers.",
                  ["We supply noise barrier products and solutions to 60+ countries across North America, Europe, Australia, Southeast Asia and the Middle East. Yukings noise barriers are certified to EN 1793, EN 1794, ASTM E90, ASTM C423 and GB/T 34509.",
                   "Yukings is privately owned, privately managed, and debt-free. Our business has grown organically through investment in new panel tooling, extended R&D, and a strong export capability."],
                  ["Founded: 2006 in Shenzhen, Guangdong, China","Business: Privately-owned noise barrier manufacturer","Facility: 42,000 m2 purpose-built factory","Employees: 120+ employees, including 40+ engineers"],
                  [("primary","Download the Yukings company profile","get-quote.html"),("ghost-alt","Email our Managing Director","contact.html")])}
    {split_block("yukings-noise-barrier-factory-production-line","Our Factory","In-house roll-forming, CNC perforation, powder coating and acoustic testing under one roof.",
                  ["Yukings operates a 42,000 m2 purpose-built noise barrier factory in Shenzhen, Guangdong, China. The facility houses roll-forming lines, CNC punching and perforation lines, electrostatic powder coating, hot-dip galvanizing and an in-house acoustic laboratory.",
                   "The factory is managed under ISO 9001, ISO 14001 and ISO 45001 and has clean, controlled materials handling, rigorous inspection of raw-material inventory control, and a dedicated R&D team."],
                  ["42,000 m2 facility (452,084 sq. ft.)","ISO 9001 / 14001 / 45001 certified","In-house acoustic test lab","Roll-forming, CNC punching, laser cutting, powder coating lines"],
                  [("primary","Take a Virtual Tour","contact.html"),("ghost-alt","Download Factory Dossier","get-quote.html")], reverse=True)}
    {split_block("yukings-noise-barrier-rd-team-engineering","Our R&D and Engineering","A 40-person engineering team, backed by Harbin Institute of Technology (HIT) R&D partnership.",
                  ["Yukings has a 40-person in-house engineering team, plus a long-standing research collaboration with the Harbin Institute of Technology (HIT), one of China's top technical universities. We hold 109+ noise barrier related patents.",
                   "Our engineering scope covers acoustic simulation, structural calculation, CAD / BIM, factory process engineering, and project site engineering."],
                  ["40+ in-house engineers","109+ noise barrier related patents","HIT research collaboration","Acoustic simulation, structural calculation, CAD / BIM"],
                  [("primary","Talk to Engineering","contact.html"),("ghost-alt","Our Patents & Research","get-quote.html")])}
  </div>
</section>""")

    # Timeline
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Our Timeline","Two decades of engineering, manufacturing and exporting noise barriers")}
    <div class="rsb-timeline">
      <div class="rsb-timeline__item">
        <span class="rsb-timeline__year">2006</span>
        <h3 class="rsb-timeline__title">Yukings founded in Shenzhen, China</h3>
        <p class="rsb-timeline__text">Yukings was founded as a manufacturer of metal-louvered noise barriers for the Chinese highway market. First factory established in Bao'an District, Shenzhen.</p>
      </div>
      <div class="rsb-timeline__item">
        <span class="rsb-timeline__year">2010</span>
        <h3 class="rsb-timeline__title">First export shipment to Southeast Asia</h3>
        <p class="rsb-timeline__text">Yukings shipped its first export order of metal-louvered noise barriers for a highway project in Southeast Asia, establishing an export footprint outside mainland China.</p>
      </div>
      <div class="rsb-timeline__item">
        <span class="rsb-timeline__year">2014</span>
        <h3 class="rsb-timeline__title">Expanded factory to 42,000 m2</h3>
        <p class="rsb-timeline__text">Yukings moved into its current 42,000 m2 purpose-built noise barrier factory, adding roll-forming lines, CNC punching lines, in-house acoustic lab and powder coating facilities.</p>
      </div>
      <div class="rsb-timeline__item">
        <span class="rsb-timeline__year">2017</span>
        <h3 class="rsb-timeline__title">ISO 9001 / 14001 / 45001 certification</h3>
        <p class="rsb-timeline__text">Yukings achieved triple certification (ISO 9001 quality, ISO 14001 environment, ISO 45001 occupational health & safety) for its noise barrier manufacturing facility.</p>
      </div>
      <div class="rsb-timeline__item">
        <span class="rsb-timeline__year">2020</span>
        <h3 class="rsb-timeline__title">Solar PV noise barrier product line</h3>
        <p class="rsb-timeline__text">Yukings launched a solar PV-integrated noise barrier product line combining EN 1793 tested acoustic absorbers with monocrystalline bifacial PV modules.</p>
      </div>
      <div class="rsb-timeline__item">
        <span class="rsb-timeline__year">2023</span>
        <h3 class="rsb-timeline__title">60+ export countries and 109 patents</h3>
        <p class="rsb-timeline__text">Yukings noise barriers are now exported to 60+ countries worldwide, with 109+ noise barrier related patents and an engineering team of 40+ engineers.</p>
      </div>
    </div>
  </div>
</section>""")

    # Certifications
    b.append(cert_block([
        ("ISO\n9001","ISO 9001:2015 Quality Management","Yukings quality management system certified to ISO 9001:2015 covering design, manufacture and installation of noise barriers."),
        ("ISO\n14001","ISO 14001:2015 Environmental Management","Environmental management system for Yukings manufacturing and installation operations, certified ISO 14001:2015."),
        ("ISO\n45001","ISO 45001:2018 Occupational Health & Safety","Occupational health and safety management system certified ISO 45001:2018 for Yukings noise barrier operations."),
        ("CE","CE Marking per EN 1793 / EN 1794","CE marking with full Technical Construction File (TCF) for Yukings noise barrier products, covering EN 1793, EN 1794, EN 1991, EN 1993, EN 1998."),
        ("ASTM\nE90","ASTM E90 / ASTM C423","ASTM E90 laboratory measurement of airborne sound insulation and ASTM C423 noise absorption coefficient testing."),
        ("GB/T\n34509","GB/T 34509 Chinese National Standard","Yukings noise barrier products meet the Chinese national standard GB/T 34509 for highway noise barrier requirements."),
        ("EN\n1793","EN 1793 Acoustic Performance","EN 1793-1 / 1793-2 / 1793-5 acoustic performance for road traffic noise reducing devices."),
        ("EN\n1794","EN 1794 Mechanical Performance","EN 1794-1 / 1794-2 mechanical performance and durability of road traffic noise reducing devices."),
    ]))

    # Team
    team = [
        ("Our Managing Director / Founder","Managing Director \u00b7 Founder","Founder and Managing Director of Yukings since 2006. Mechanical engineer, M.Eng., with 20+ years of noise barrier design and project management experience.","Contact Managing Director","contact.html","yukings-noise-barrier-managing-director-portrait","MD"),
        ("Technical Director","Engineering Director \u00b7 PhD, Acoustics","PhD in acoustics with 18+ years of noise barrier engineering, acoustic modelling and research, including publications in international journals.","Contact Technical Director","contact.html","yukings-noise-barrier-technical-director-portrait","TECH"),
        ("Head of Export Sales","Export Sales Director \u00b7 MBA","Export sales director responsible for international sales, quotations, OEM partnerships and client relationship management.","Contact Sales","contact.html","yukings-noise-barrier-export-sales-director","SALES"),
    ]
    team_html = "".join(card(*t) for t in team)
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Meet the Team","The people behind Yukings noise barriers")}
    <div class="rsb-grid rsb-grid--3" style="grid-template-columns:repeat(3,1fr)">
      {team_html}
    </div>
  </div>
</section>""")

    b.append(stat_section([
        ("2006","founded"),("42,000 m2","factory floor"),("109+","patents"),("60+","export countries"),
    ]))
    b.append(cta_section(
        "Want to know more about Yukings? Get in touch with our team.",
        "Yukings welcomes factory visits from potential customers, distributors and partners. Contact us to schedule a factory visit, download our company dossier or request a formal quotation."))
    b.append(page_close())
    return "".join(b)

def page_contact():
    b=[]
    b.append(page_head(
        "Contact Yukings | Get a Noise Barrier Quote in 24 Hours",
        "Contact Shenzhen Yukings Industrial Co., Ltd. for noise barrier quotations, engineering consultations or technical support. Email, phone and WhatsApp details on this page.",
        "contact.html"))
    b.append(breadcrumb([("Home","index.html"),("Contact Us",None)]))
    b.append(hero(
        "Let's __SPAN__ about your noise barrier project.",
        "talk",
        "Tell us about your noise barrier project - project scope, project location, target insertion loss or required barrier length. Our technical sales engineers respond to every email within 24 hours.",
        "yukings-noise-barrier-contact-office",
        chips=["24-hour response","English & Chinese","Tel, WhatsApp, WeChat","Shenzhen factory visit by appointment"],
        actions=[("primary","Email Our Team","contact.html"),("ghost","Call +86-755-86366707","contact.html")],
        stats=[("24 hours","response time"),("Mon-Sat","08:30-18:30 CST"),("Shenzhen","Guangdong, China"),("WeChat/WhatsApp","international")]))

    # Contact info grid
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("Get in Touch","Multiple ways to reach the Yukings team")}
    <div class="rsb-grid rsb-grid--4" style="grid-template-columns:repeat(2,1fr)">
      <div class="rsb-feature">
        <h3 style="font-size:18px;margin-bottom:10px">Head Office & Factory</h3>
        <p style="font-size:14px">Room 1405, Building B2, Yunzhi Tech Park, Guangming District, Shenzhen, Guangdong, China 518106</p>
      </div>
      <div class="rsb-feature">
        <h3 style="font-size:18px;margin-bottom:10px">Telephone</h3>
        <p style="font-size:14px">+86 755 86366707 (Shenzhen head office, 08:30-18:30 Monday to Saturday, Beijing Time)</p>
      </div>
      <div class="rsb-feature">
        <h3 style="font-size:18px;margin-bottom:10px">Email</h3>
        <p style="font-size:14px">weilai04525@163.com (general inquiries, quotation requests, technical support)</p>
      </div>
      <div class="rsb-feature">
        <h3 style="font-size:18px;margin-bottom:10px">Sales & Engineering WhatsApp / WeChat</h3>
        <p style="font-size:14px">Miss Tang (International Sales Manager): +86 17727812004 (WhatsApp / WeChat). Mr. Yu (Technical & Solution Engineer): +86 13828819804 (WhatsApp / WeChat).</p>
      </div>
    </div>
  </div>
</section>""")

    # Contact form
    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Send Us a Message","Submit a project enquiry and get a response within 24 hours")}
    <div class="rsb-form">
      <div class="rsb-form__grid" style="display:grid;grid-template-columns:1fr 1fr;gap:18px">
        <div class="rsb-form__field">
          <label>Your Name *</label>
          <input type="text" placeholder="John Doe">
        </div>
        <div class="rsb-form__field">
          <label>Company Name</label>
          <input type="text" placeholder="Your company">
        </div>
        <div class="rsb-form__field">
          <label>Country</label>
          <input type="text" placeholder="Your country">
        </div>
        <div class="rsb-form__field">
          <label>Email *</label>
          <input type="email" placeholder="john@example.com">
        </div>
        <div class="rsb-form__field">
          <label>WhatsApp / Phone</label>
          <input type="text" placeholder="+1 555 0100">
        </div>
        <div class="rsb-form__field">
          <label>Project Category</label>
          <select><option>Highway Noise Barrier</option><option>Railway Noise Barrier</option><option>Industrial Noise Barrier</option><option>Residential Noise Barrier</option><option>Solar PV Noise Barrier</option><option>Other / Not Sure</option></select>
        </div>
        <div class="rsb-form__field" style="grid-column:1/-1">
          <label>Project Description / Noise Reduction Requirement</label>
          <textarea rows="5" placeholder="Project description and noise reduction requirement"></textarea>
        </div>
        <div class="rsb-form__field" style="grid-column:1/-1">
          <label>Attachment (drawings, specification, project scope)</label>
          <input type="file">
        </div>
      </div>
      <a href="mailto:weilai04525@163.com" class="rsb-btn rsb-btn--primary rsb-btn--lg rsb-form__submit" style="display:block;margin-top:20px;width:100%;text-align:center">Send Enquiry</a>
    </div>
  </div>
</section>""")

    b.append(cta_section(
        "Prefer a direct line? Contact Miss Tang or Mr. Yu on WhatsApp today.",
        "Miss Tang (International Sales Manager): WhatsApp / WeChat: +86 17727812004. Mr. Yu (Technical and Solution Engineer): WhatsApp / WeChat: +86 13828819804."))
    b.append(page_close())
    return "".join(b)

def page_getquote():
    b=[]
    b.append(page_head(
        "Get a Noise Barrier Quote | Yukings - Free Project Evaluation in 24 Hours",
        "Get a free noise barrier quotation and project evaluation in 24 hours from Yukings. Free engineering feasibility, CAD drawings and acoustic simulation with your formal quote.",
        "get-quote.html"))
    b.append(breadcrumb([("Home","index.html"),("Get Quote",None)]))
    b.append(hero(
        "Get a free, no-obligation noise barrier project __SPAN__ in 24 hours.",
        "quotation & technical evaluation",
        "Send us your project details - we respond within 24 hours with a noise barrier quotation, technical specification overview and, where relevant, a preliminary acoustic simulation.",
        "yukings-noise-barrier-free-quotation-engineer",
        chips=["Free quotation","Engineering support","24-hour response","Sample panels on request","OEM & custom sizes available"],
        actions=[("primary","Email Yukings Sales","contact.html"),("ghost","WhatsApp Miss Tang","contact.html")],
        stats=[("24 hours","response time"),("48 hours","for detailed proposals"),("20 working days","standard lead time"),("40 days","custom-engineered")]))
    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    {section_head("How to get a quote","A simple four-step process")}
    <div class="rsb-grid rsb-grid--4" style="grid-template-columns:repeat(4,1fr)">
      <div class="rsb-feature"><i class="rsb-feature__icon" style="width:48px;height:48px;background:linear-gradient(135deg,rgba(228,102,42,.12),rgba(228,102,42,.04));color:var(--orange);display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;margin-bottom:16px;font-style:normal;border:1px solid rgba(228,102,42,.25);border-radius:50%;transition:all .35s ease">01</i><h3 style="font-size:18px;margin-bottom:10px">Step 1 - Send us your project brief</h3><p style="font-size:14px;color:#4a5568;line-height:1.65">Send us your project details: barrier type, approximate length, location and noise reduction requirements.</p></div>
      <div class="rsb-feature"><i class="rsb-feature__icon" style="width:48px;height:48px;background:linear-gradient(135deg,rgba(228,102,42,.12),rgba(228,102,42,.04));color:var(--orange);display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;margin-bottom:16px;font-style:normal;border:1px solid rgba(228,102,42,.25);border-radius:50%;transition:all .35s ease">02</i><h3 style="font-size:18px;margin-bottom:10px">Step 2 - We engineer a solution</h3><p style="font-size:14px;color:#4a5568;line-height:1.65">Our engineers will respond within 24 hours with a noise barrier proposal and technical overview.</p></div>
      <div class="rsb-feature"><i class="rsb-feature__icon" style="width:48px;height:48px;background:linear-gradient(135deg,rgba(228,102,42,.12),rgba(228,102,42,.04));color:var(--orange);display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;margin-bottom:16px;font-style:normal;border:1px solid rgba(228,102,42,.25);border-radius:50%;transition:all .35s ease">03</i><h3 style="font-size:18px;margin-bottom:10px">Step 3 - Send samples on request</h3><p style="font-size:14px;color:#4a5568;line-height:1.65">On request we send 500 x 500 mm sample panels together with CE / ISO test reports.</p></div>
      <div class="rsb-feature"><i class="rsb-feature__icon" style="width:48px;height:48px;background:linear-gradient(135deg,rgba(228,102,42,.12),rgba(228,102,42,.04));color:var(--orange);display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;margin-bottom:16px;font-style:normal;border:1px solid rgba(228,102,42,.25);border-radius:50%;transition:all .35s ease">04</i><h3 style="font-size:18px;margin-bottom:10px">Step 4 - Formal PO &amp; delivery</h3><p style="font-size:14px;color:#4a5568;line-height:1.65">Your purchase order is confirmed, production is released and delivery is booked.</p></div>
    </div>
  </div>
</section>""")

    # Request form
    b.append(f"""<section class="rsb-section rsb-section--gray">
  <div class="rsb-container">
    {section_head("Request a quotation","Free, no-obligation noise barrier quotation")}
    <div class="rsb-form">
      <div class="rsb-form__grid" style="display:grid;grid-template-columns:1fr 1fr;gap:18px">
        <div class="rsb-form__field"><label>Your Name *</label><input type="text" placeholder="Your name"></div>
        <div class="rsb-form__field"><label>Company Name</label><input type="text" placeholder="Your company"></div>
        <div class="rsb-form__field"><label>Country</label><input type="text" placeholder="Your country"></div>
        <div class="rsb-form__field"><label>Email *</label><input type="email" placeholder="you@example.com"></div>
        <div class="rsb-form__field"><label>WhatsApp / Phone</label><input type="text" placeholder="+1 555 0100"></div>
        <div class="rsb-form__field"><label>Project Category</label><select><option>Highway Noise Barrier</option><option>Railway Noise Barrier</option><option>Industrial Noise Barrier</option><option>Residential Noise Barrier</option><option>Solar PV Noise Barrier</option><option>Other / Not Sure</option></select></div>
        <div class="rsb-form__field" style="grid-column:1/-1"><label>Project Description / Noise Reduction Requirement</label><textarea rows="5" placeholder="Project description, project size, noise reduction requirement, etc."></textarea></div>
        <div class="rsb-form__field" style="grid-column:1/-1"><label>Attachments (drawings, specifications, scope documents)</label><input type="file"></div>
      </div>
      <a href="mailto:weilai04525@163.com" class="rsb-btn rsb-btn--primary rsb-btn--lg rsb-form__submit" style="display:block;margin-top:20px;width:100%;text-align:center">Request Quotation</a>
    </div>
  </div>
</section>""")

    b.append(stat_section([
        ("20 working days","standard product"),("40 working days","custom-engineered"),("24 hours","our response time"),("15 years","structural warranty"),
    ]))
    b.append(cta_section(
        "Want a fast-track quotation? WhatsApp Miss Tang right now.",
        "Miss Tang (International Sales Manager): WhatsApp / WeChat: +86 17727812004. Mr. Yu (Technical & Solution Engineer): WhatsApp / WeChat: +86 13828819804."))
    b.append(page_close())
    return "".join(b)

def page_privacy():
    b=[]
    b.append(page_head(
        "Privacy Policy | Yukings Noise Barrier Manufacturer",
        "Yukings privacy policy: how we handle personal information, cookies and data in compliance with GDPR and international privacy standards.",
        "privacy-policy.html"))
    b.append(breadcrumb([("Home","index.html"),("Privacy Policy",None)]))
    b.append(hero(
        "Your privacy matters to __SPAN__.",
        "Yukings",
        "This privacy policy explains how Shenzhen Yukings Industrial Co., Ltd. (Yukings) collects, uses and protects any information that you provide us when you use this website or contact Yukings.",
        "yukings-privacy-policy-data-protection-gdpr",
        chips=["GDPR-aligned","ISO 27001 practices","data subject rights","no third-party sharing"],
        actions=[("primary","Contact Our DPO","contact.html")],
        stats=[("May 2025","last updated"),("Shenzhen, CN","data location")]))

    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    <div class="rsb-legal" style="max-width:900px;margin:0 auto">
      <h2>Introduction</h2>
      <p>This privacy policy sets out how Yukings uses and protects any information that you give Yukings when you use this website. Yukings is committed to ensuring that your privacy is protected. Should we ask you to provide certain information by which you can be identified when using this website, you can be assured that such information will only be used in accordance with this privacy statement.</p>
      <p>Yukings may change this policy from time to time by updating this page. You should check this page from time to time to ensure that you are happy with any changes. This policy is effective from May 2025.</p>
      <h3>What we collect</h3>
      <p>We may collect the following information: your name and job title; contact information including email address and phone number; demographic information such as postcode, preferences and interests; other information relevant to customer surveys, project quotations and / or offers.</p>
      <h3>What we do with the information we gather</h3>
      <p>We require this information to understand your needs and provide you with a better service, and in particular for the following reasons: internal record keeping; we may use the information to improve our products and services; we may periodically send promotional emails about new products, special offers or other information which we think you may find interesting using the email address which you have provided; from time to time, we may also use your information to contact you for market research purposes. We may contact you by email, phone, fax or mail. We may use the information to customise the website according to your interests.</p>
      <h3>Security</h3>
      <p>We are committed to ensuring that your information is secure. In order to prevent unauthorised access or disclosure we have put in place suitable physical, electronic and managerial procedures to safeguard and secure the information we collect online.</p>
      <h3>How we use cookies</h3>
      <p>A cookie is a small file which asks permission to be placed on your computer’s hard drive. Once you agree, the file is added and the cookie helps analyse web traffic or lets you know when you visit a particular site. Cookies allow web applications to respond to you as an individual. The web application can tailor its operations to your needs, likes and dislikes by gathering and remembering information about your preferences.</p>
      <p>We use traffic log cookies to identify which pages are being used. This helps us analyse data about web page traffic and improve our website in order to tailor it to customer needs. We only use this information for statistical analysis purposes and then the data is removed from the system.</p>
      <p>Overall, cookies help us provide you with a better website, by enabling us to monitor which pages you find useful and which you do not. A cookie in no way gives us access to your computer or any information about you, other than the data you choose to share with us. You can choose to accept or decline cookies. Most web browsers automatically accept cookies, but you can usually modify your browser setting to decline cookies if you prefer. This may prevent you from taking full advantage of the website.</p>
      <h3>Controlling your personal information</h3>
      <p>You may choose to restrict the collection or use of your personal information in the following ways: whenever you are asked to fill in a form on the website, look for the box that you can click to indicate that you do not want the information to be used by anybody for direct marketing purposes; if you have previously agreed to us using your personal information for direct marketing purposes, you may change your mind at any time by writing to or emailing us at weilai04525@163.com. We will not sell, distribute or lease your personal information to third parties unless we have your permission or are required by law to do so. We may use your personal information to send you promotional information about third parties which we think you may find interesting if you tell us that you wish this to happen. You may request details of personal information which we hold about you under the Data Protection Act 1998. A small fee will be payable. If you would like a copy of the information held on you please write to Room 1405, Building B2, Yunzhi Tech Park, Guangming District, Shenzhen, Guangdong, China. If you believe that any information we are holding on you is incorrect or incomplete, please write to or email us as soon as possible at the above address. We will promptly correct any information found to be incorrect.</p>
      <h3>Your rights under the GDPR</h3>
      <p>In addition to the rights set out above, you have the right to ask us not to process your personal data for marketing purposes. We will usually inform you (before collecting your data) if we intend to use your data for such purposes or if we intend to disclose your information to any third party for such purposes. You can exercise the right at any time by contacting us at weilai04525@163.com.</p>
      <h3>Contacting us</h3>
      <p>If you have any questions about this Privacy Policy, please contact us at: Shenzhen Yukings Industrial Co., Ltd., Room 1405, Building B2, Yunzhi Tech Park, Guangming District, Shenzhen, Guangdong, China, email weilai04525@163.com, telephone +86-755-86366707.</p>
    </div>
  </div>
</section>""")
    b.append(cta_section(
        "Have a privacy-related question? Contact our Data Protection Officer today.",
        "Our Data Protection Officer is available by email at weilai04525@163.com with response within 24 hours."))
    b.append(page_close())
    return "".join(b)

def page_terms():
    b=[]
    b.append(page_head(
        "Terms of Service | Yukings Noise Barrier Manufacturer",
        "Yukings terms of service: use of website, intellectual property, quotations, ordering, delivery, warranty, limitation of liability and dispute resolution.",
        "terms-of-service.html"))
    b.append(breadcrumb([("Home","index.html"),("Terms of Service",None)]))
    b.append(hero(
        "Yukings noise barrier __SPAN__.",
        "website & service terms",
        "The terms and conditions governing the use of this website, noise barrier product quotations, orders and services offered by Shenzhen Yukings Industrial Co., Ltd. (Yukings).",
        "yukings-noise-barrier-terms-of-service-legal",
        chips=["English law","Shenzhen arbitration","ISO 9001 quality","CE certified products"],
        actions=[("primary","Contact Our Sales","contact.html"),("ghost","Download Terms PDF","get-quote.html")]))

    b.append(f"""<section class="rsb-section">
  <div class="rsb-container">
    <div class="rsb-legal" style="max-width:900px;margin:0 auto">
      <h2>Introduction</h2>
      <p>Welcome to the Yukings website and services website and services website. If you continue to browse and use this website and service you are agreeing to comply with and be bound by the following terms and conditions of use, which together with our privacy policy govern Yukings relationship with you in relation to this website.</p>
      <p>The term 'Yukings' or 'us' or 'we' refers to the owner of the website whose registered office is Room 1405, Building B2, Yunzhi Tech Park, Guangming District, Shenzhen, Guangdong, China. The term 'you' refers to the user or viewer of our website.</p>
      <h3>The use of this website is subject to the following terms of use</h3>
      <p>The content of the pages of this website is for your general information and use only. It is subject to change without notice. Neither we nor any third parties provide any warranty or guarantee as to the accuracy, timeliness, performance, completeness or suitability of the information and materials found or offered on this website for any particular purpose. You acknowledge that such information and materials may contain inaccuracies or errors and we expressly exclude liability for any such inaccuracies or errors to the fullest extent permitted by law.</p>
      <p>Your use of any information or materials on this website is entirely at your own risk, for which we shall not be liable. It shall be your own responsibility to ensure that any products, services or information available through this website meet your specific requirements.</p>
      <h3>Intellectual property</h3>
      <p>This website contains material which is owned by or licensed to us. This material includes, but is not limited to, the design, layout, look, appearance and graphics. Reproduction is prohibited other than in accordance with the copyright notice, which forms part of these terms and conditions. All trademarks reproduced in this website which are not the property of, or licensed to, the operator are acknowledged on the website.</p>
      <h3>Quotations and orders</h3>
      <p>All noise barrier quotations provided by Yukings are valid for 30 days from date of issue unless otherwise stated in writing. Orders are subject to our standard terms and conditions of sale, including 30% deposit on order and 60% prior to shipment and 10% final against acceptance documents. Lead times are as stated in the relevant quotation or, where not specified, standard lead time is 20 working days for standard panels and 40 working days for custom-engineered panels.</p>
      <h3>Warranty</h3>
      <p>Yukings warrants its noise barrier products against manufacturing defects in materials and workmanship for a period of 15 years from date of shipment, provided that the products have been installed in accordance with Yukings installation and maintenance instructions, installed by a properly qualified installer, and subject to normal service conditions. Acoustic performance remains within +/- 2 dB of the published rating for the warranty period.</p>
      <h3>Limitation of liability</h3>
      <p>Yukings total liability for any claim (whether in contract, tort or otherwise) arising out of or in connection with the supply of goods or services under a quotation or order is limited to the price paid by the customer for the goods or services giving rise to the claim. Yukings shall not be liable for any indirect or consequential loss including without limitation loss of profit, revenue, business, opportunity, goodwill or reputation, loss of data or information, or any other commercial or economic loss of any kind.</p>
      <h3>Governing law and dispute resolution</h3>
      <p>Any dispute arising out of or in connection with a contract, quotation or this website shall be governed by and construed in accordance with the laws of the People's Republic of China. Any dispute, controversy or claim arising out of or relating to this contract, or the breach, termination or invalidity thereof, shall be settled by arbitration in accordance with the Arbitration Rules of the Shenzhen Court of International Arbitration (SCIA). The arbitration shall be conducted in the English language. The place of arbitration shall be Shenzhen, Guangdong, China.</p>
      <h3>Contacting Yukings</h3>
      <p>If you have any questions about these Terms, please contact us at: Shenzhen Yukings Industrial Co., Ltd., Room 1405, Building B2, Yunzhi Tech Park, Guangming District, Shenzhen, Guangdong, China; email weilai04525@163.com; telephone +86-755-86366707.</p>
    </div>
  </div>
</section>""")
    b.append(cta_section(
        "Have a legal or commercial question? Contact Yukings today.",
        "For legal or commercial questions or contract-related questions please contact our business team at weilai04525@163.com or by telephone at +86-755-86366707."))
    b.append(page_close())
    return "".join(b)

write_page("blog.html", page_blog())
write_page("faqs.html", page_faqs())
write_page("about.html", page_about())
write_page("contact.html", page_contact())
write_page("get-quote.html", page_getquote())
write_page("privacy-policy.html", page_privacy())
write_page("terms-of-service.html", page_terms())
print("pages part 4 (blog, faqs, about, contact, get-quote, privacy, terms) done.")
