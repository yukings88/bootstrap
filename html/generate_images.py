#!/usr/bin/env python3
import os
import re
import time
import urllib.parse
import subprocess
import requests
from PIL import Image
from io import BytesIO

API_BASE = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMG_DIR = "/workspace/html/img"
HTML_DIR = "/workspace/html"

def get_missing_images():
    hero = set()
    hp = re.compile(r'rsb-hero[^}]*?background-image\s*:\s*url\([\'"]?(img/[^\'")]+)[\'"]?\)', re.DOTALL)
    for fn in os.listdir(HTML_DIR):
        if not fn.endswith('.html'):
            continue
        with open(os.path.join(HTML_DIR, fn)) as f:
            c = f.read()
        for m in hp.finditer(c):
            hero.add(os.path.basename(m.group(1)))
    
    missing = []
    for fn in os.listdir(HTML_DIR):
        if not fn.endswith('.html'):
            continue
        with open(os.path.join(HTML_DIR, fn)) as f:
            c = f.read()
        for m in re.finditer(r'img/([^"\'\s)]+)', c):
            p = m.group(1)
            if not p.endswith('.webp'):
                continue
            if p in ('yukings-factory.webp', 'yukings-logo.svg', 'yukings-logo.jpg'):
                continue
            fp = os.path.join(IMG_DIR, p)
            if not os.path.exists(fp) or os.path.getsize(fp) < 25000:
                mm = re.match(r'(.+)-([a-f0-9]{8})\.webp$', p)
                if mm and p not in [x[0] for x in missing]:
                    is_banner = p in hero
                    missing.append((p, mm.group(1), is_banner))
    return sorted(set(missing))

def make_prompt(name):
    """Convert kebab-case filename to a descriptive image prompt."""
    prompt_map = {
        'absorptive-highway-noise-barrier-polycarbonate-window': 'professional photograph of absorptive highway noise barrier with transparent polycarbonate window panels, modern road infrastructure, clear blue sky, engineering photography',
        'absorptive-noise-barrier-louvered-metal-panel': 'close-up detail of louvered metal absorptive noise barrier panel, perforated steel acoustic insulation, industrial product photography, clean white background',
        'aluminum-galvanized-steel-noise-barrier-comparison': 'comparison diagram showing aluminum vs galvanized steel noise barrier panels, side by side material samples, technical engineering illustration',
        'aluminum-lightweight-bridge-parapet-noise-barrier': 'lightweight aluminum noise barrier installed on bridge parapet, modern bridge infrastructure, elevated highway, blue sky, professional engineering photography',
        'aluminum-noise-barrier': 'aluminum noise barrier panel product, silver metallic finish, industrial manufacturing, factory showroom, professional product photography',
        'bifacial-solar-noise-barrier-installation-railway': 'bifacial solar photovoltaic noise barrier installation along railway track, construction workers installing panels, renewable energy infrastructure',
        'bridge-elevated-road-noise-barrier-viaduct-parapet': 'noise barrier on elevated road viaduct bridge parapet, modern concrete viaduct in urban setting, cityscape background, professional civil engineering photography',
        'bridge-noise-barrier': 'noise barrier panels installed on highway bridge, steel structure, modern infrastructure, professional construction photography',
        'bridge-parapet-reflective-noise-barrier': 'reflective noise barrier mounted on bridge parapet wall, rigid metal panels, concrete bridge edge, safety railing, engineering detail shot',
        'cantilever-cap-hybrid-noise-barrier-bridge': 'cantilever cap hybrid noise barrier on bridge, overhanging top section for acoustic diffraction, advanced engineering design, blue sky background',
        'clear-acrylic-sound-barrier-residential-street': 'clear transparent acrylic sound barrier wall along residential street, modern houses visible through panels, suburban neighborhood, clean modern design',
        'curved-cap-noise-wall-diffraction-engineering': 'curved top cap noise wall showing acoustic diffraction engineering principle, technical diagram overlay, sound wave visualization, civil engineering illustration',
        'en-1793-acoustic-performance-classification': 'EN 1793 standard acoustic performance classification chart for noise barriers, technical document, sound absorption testing data, engineering specification sheet',
        'en-1794-mechanical-performance-noise-barrier-impact-test': 'EN 1794 mechanical performance impact resistance testing on noise barrier panel, laboratory equipment, quality control testing, industrial certification',
        'en-1794-mechanical-performance-noise-barriers': 'EN 1794 mechanical performance standards for noise barriers, technical specification document, structural engineering requirements, European standard',
        'heavy-industrial-noise-barrier-factory-boundary-wall': 'heavy duty industrial noise barrier at factory boundary wall, large manufacturing plant perimeter, thick acoustic panels, industrial zone photography',
        'high-speed-rail-aero-acoustic-noise-barriers': 'aero-acoustic noise barriers designed for high speed rail, aerodynamic shape, streamlined top profile, bullet train passing by, advanced railway engineering',
        'high-speed-rail-noise-barrier-aero-acoustic-pulse-pressure': 'high speed rail noise barrier with aero-acoustic pulse pressure visualization, CFD simulation airflow diagram, technical engineering illustration',
        'high-speed-railway-hybrid-noise-barrier': 'hybrid noise barrier along high speed railway line, combination absorptive and reflective panels, train passing at speed, modern railway infrastructure',
        'high-speed-railway-noise-barrier-train-acoustic-wall': 'high speed railway acoustic noise barrier wall with bullet train passing, motion blur on train, concrete and steel panels, professional railway photography',
        'highway-expressway-noise-barrier-motorway-wall': 'noise barrier wall along busy highway expressway motorway, multiple lanes of traffic, green landscape, blue sky, modern road infrastructure',
        'highway-expressway-solar-pv-noise-barrier': 'solar PV photovoltaic noise barrier along highway expressway, blue solar panels integrated into noise wall, renewable energy and transportation',
        'highway-noise-barrier-project-urban-expressway': 'completed highway noise barrier project on urban expressway, city skyline in background, multi-lane road, successful infrastructure project photography',
        'highway-noise-control-expressway-ringroad': 'highway noise control measures on urban ring road expressway, circular road around city, traffic noise mitigation, aerial perspective view',
        'highway-rigid-reflective-noise-barrier': 'rigid reflective noise barrier panels along highway, solid non-porous metal sheets, concrete posts, standard motorway sound wall',
        'hot-dip-galvanized-noise-barrier-panel-factory': 'hot-dip galvanized noise barrier panels in factory setting, zinc coated steel, industrial manufacturing process, production line quality control',
        'how-to-choose-noise-barrier-panel-depth': 'guide illustration showing how to choose noise barrier panel depth comparison 80mm 100mm 120mm 140mm, technical decision diagram, acoustic performance chart',
        'hybrid-acoustic-barrier-cross-section-diagram-installation': 'cross-section technical diagram of hybrid acoustic barrier installation, layered construction showing absorptive and reflective materials, engineering blueprint style',
        'hybrid-noise-barrier': 'hybrid noise barrier product combining absorptive and reflective materials, dual-layer acoustic panel, professional industrial product photography',
        'hybrid-noise-barrier-dual-layer': 'dual-layer hybrid noise barrier construction detail, cross section showing inner absorption material and outer reflective shell, technical product photography',
        'hybrid-noise-barrier-dual-layer-railway-road': 'dual-layer hybrid noise barrier installed alongside both railway and road, combined transportation corridor, integrated infrastructure, professional engineering photo',
        'industrial-factory-noise-barrier-machinery-enclosure': 'industrial noise barrier as machinery enclosure inside factory, acoustic panels surrounding noisy equipment, worker safety, manufacturing plant interior',
        'industrial-noise-barrier': 'industrial noise barrier product, heavy duty acoustic panels for factories, dark gray metal finish, industrial warehouse setting',
        'industrial-noise-barrier-project-power-plant': 'industrial noise barrier project surrounding power plant facility, large energy infrastructure, cooling towers in background, perimeter acoustic wall',
        'industrial-plant-boundary-hybrid-noise-wall': 'hybrid noise wall at industrial plant boundary, factory perimeter fence, combination sound wall, industrial complex background',
        'industrial-plant-boundary-reflective-noise-wall': 'reflective noise wall at industrial plant boundary, solid concrete or metal panels, factory perimeter security wall, heavy industry',
        'industrial-plant-boundary-solar-acoustic-wall': 'solar acoustic wall at industrial plant boundary, PV panels integrated into noise barrier, renewable energy for factory, sustainable manufacturing',
        'industrial-plant-factory-noise-barrier-machinery-noise-control': 'factory noise barrier for machinery noise control, industrial equipment enclosures, worker hearing protection, manufacturing facility interior',
        'insertion-loss-sound-insulation-absorption-coefficients-noise-barriers': 'technical chart showing insertion loss, sound insulation and absorption coefficients for noise barriers, acoustic engineering graph, data visualization',
        'modern-industrial-noise-barrier-factory-site-aerial': 'aerial drone view of modern industrial noise barrier surrounding factory site, large manufacturing complex, bird eye perspective, industrial zone photography',
        'modern-reflective-noise-barrier-highway-rigid-panel': 'modern reflective noise barrier on highway with rigid smooth panels, clean contemporary design, gray metallic finish, motorway infrastructure',
        'new-energy-solar-noise-barrier-projects-pv': 'new energy solar noise barrier projects, large scale PV photovoltaic installation along transportation corridor, renewable energy infrastructure, bright sunny day',
        'noise-barrier-acoustic-principle-diagram-reflective-absorptive': 'acoustic principle diagram showing reflective vs absorptive noise barriers, sound wave propagation illustration, before and after comparison, educational infographic',
        'noise-barrier-applications-highway-railway-industrial-residential': 'collage showing noise barrier applications: highway, railway, industrial, residential, four quadrant layout, multiple use cases, comprehensive overview',
        'noise-barrier-blog-technical-articles-engineering-insight-lab': 'noise barrier blog and technical articles concept, engineering insight laboratory, desk with blueprints, laptop showing acoustic data, professional engineering workspace',
        'noise-barrier-faq-deep-dive': 'frequently asked questions about noise barriers concept, FAQ document with magnifying glass, deep dive technical analysis, information and support',
        'noise-barrier-industry-news-2': 'noise barrier industry news and updates concept, newspaper headlines, construction site background, latest developments in acoustic engineering',
        'noise-barrier-materials-steel-aluminum-acrylic-concrete': 'noise barrier material samples: steel, aluminum, acrylic, concrete arranged together, material comparison display, different textures and finishes',
        'noise-barrier-project-checklist': 'noise barrier project checklist document on clipboard, construction site background, planning and specification sheet, project management concept',
        'noise-barrier-technical-article-engineering-2': 'technical engineering article about noise barriers, open book with diagrams and calculations, engineering desk, professional technical publication',
        'noise-barrier-top-profiles-flat-curved-y-shaped': 'comparison of noise barrier top profiles: flat straight top, curved arc top, Y-shaped top, three designs side by side, acoustic diffraction shapes',
        'railway-metro-hybrid-noise-barrier': 'hybrid noise barrier along railway metro line, urban commuter train, city public transit infrastructure, combination acoustic panels',
        'railway-metro-solar-pv-noise-barrier': 'solar PV noise barrier along railway metro line, urban train passing, blue photovoltaic panels, public transit renewable energy integration',
        'railway-noise-barrier': 'railway noise barrier panels along train track, standard railroad sound wall, gravel ballast, steel rails, professional railway photography',
        'railway-noise-barrier-hybrid-slipstream-panel': 'hybrid noise barrier with special slipstream panels for railway, aerodynamic design to handle train wind pressure, high speed rail corridor',
        'railway-noise-barrier-project-high-speed-corridor': 'completed railway noise barrier project on high speed corridor, long straight wall stretching into distance, modern rail infrastructure, success project',
        'railway-noise-barriers-high-speed-rail': 'noise barriers along high speed rail line, dedicated HSR corridor, concrete and steel acoustic walls, electrified railway overhead lines',
        'railway-noise-reduction-high-speed-corridor': 'railway noise reduction solutions on high speed corridor, before and after concept, quieter communities near rail line, noise mitigation benefits',
        'railway-trackside-rigid-reflective-noise-barrier': 'rigid reflective noise barrier trackside at railway, solid panels close to tracks, ballast and rails visible, standard railroad sound wall',
        'reflective-noise-barrier': 'reflective noise barrier product, solid rigid panel that reflects sound waves, hard non-porous surface, concrete or dense metal, professional product shot',
        'reflective-sound-barrier-steel-panel-installation': 'reflective sound barrier steel panel installation on highway, construction workers mounting panels, active construction site, installation process',
        'residential-community-noise-protection-housing': 'residential community noise protection for housing estate, apartment buildings protected by noise wall, peaceful neighborhood, quality of life concept',
        'residential-noise-barriers-community-garden': 'residential noise barriers with community garden, green landscaping near homes, attractive sound wall design, flowers and plants, pleasant living environment',
        'residential-sensitive-highway-hybrid-noise-barrier': 'hybrid noise barrier protecting residential sensitive area near highway, houses close to motorway, specially designed acoustic protection, peaceful homes',
        'semi-enclosed-u-shape-noise-barrier-highway-railway': 'semi-enclosed U-shaped noise barrier covering highway or railway, tunnel-like partial cover structure, advanced noise protection for sensitive areas',
        'semi-enclosed-u-shape-noise-wall-cantilever-cover-plate-installation': 'semi-enclosed U-shaped noise wall with cantilever cover plate installation, construction workers installing top cover, complex engineering structure',
        'solar-noise-barrier-project-pv-highway': 'solar noise barrier PV project along highway, large scale installation of photovoltaic sound walls, blue panels along motorway, renewable energy generation',
        'solar-photovoltaic-noise-barrier-highway-pv-modules': 'solar photovoltaic noise barrier on highway, close-up of PV modules integrated into sound wall panels, blue solar cells, clean energy infrastructure',
        'solar-photovoltaic-noise-barrier-pv-modules': 'solar photovoltaic noise barrier PV modules product shot, bifacial solar panels designed for noise barrier integration, clean energy technology',
        'solar-pv-integrated-noise-barriers': 'solar PV integrated noise barrier system overview, complete solution combining sound insulation with clean energy generation, renewable transportation infrastructure',
        'urban-arterial-road-solar-noise-wall': 'solar noise wall along urban arterial road, city street with PV sound barrier, buildings in background, urban environment renewable energy',
        'yukings-noise-barrier-free-quotation-engineer': 'professional engineer offering free quotation for noise barrier project, friendly consultant at desk with blueprints, calculator and drawings, business meeting',
        'yukings-noise-barrier-terms-of-service-legal': 'terms of service legal document for noise barrier company, contract papers with scales of justice, legal agreement, professional business documentation',
        'yukings-privacy-policy-data-protection-gdpr': 'privacy policy and data protection GDPR compliance concept, document with lock icon, shield symbol, personal data security, legal compliance'
    }
    base_prompt = prompt_map.get(name, None)
    if base_prompt:
        return base_prompt + ", high quality, professional photography, 16:9 landscape, photorealistic, sharp focus"
    else:
        pretty_name = name.replace('-', ' ')
        return f"professional photograph of {pretty_name}, noise barrier acoustic infrastructure, high quality, photorealistic, sharp focus, 16:9 landscape"

def is_real_image(content):
    """Check if image content is a real generated image (not the default placeholder)."""
    try:
        img = Image.open(BytesIO(content))
        width, height = img.size
        if width == 1832 and height == 1832:
            return False
        if width >= 1300 and height >= 700:
            pixels = list(img.getdata())
            if len(pixels) > 1000:
                sample = pixels[:1000]
                from collections import Counter
                most_common = Counter(sample).most_common(1)[0][1]
                if most_common > 500:
                    return False
            return True
        return False
    except:
        return False

def process_image(content, is_banner):
    """Process downloaded image to correct dimensions and save as WebP."""
    img = Image.open(BytesIO(content))
    target_w = 1368
    target_h = 600 if is_banner else 768
    
    img = img.convert('RGB')
    orig_w, orig_h = img.size
    
    scale = max(target_w / orig_w, target_h / orig_h)
    new_w = int(orig_w * scale)
    new_h = int(orig_h * scale)
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    right = left + target_w
    bottom = top + target_h
    img = img.crop((left, top, right, bottom))
    
    return img

def generate_image(filename, prompt_name, is_banner, max_retries=15):
    """Generate a single image with retries."""
    output_path = os.path.join(IMG_DIR, filename)
    
    if os.path.exists(output_path) and os.path.getsize(output_path) > 30000:
        try:
            check_img = Image.open(output_path)
            w, h = check_img.size
            target_h = 600 if is_banner else 768
            if w == 1368 and h == target_h:
                print(f"  [SKIP] {filename} already exists with correct dimensions")
                return True
        except:
            pass
    
    prompt = make_prompt(prompt_name)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"{API_BASE}?prompt={encoded_prompt}&image_size=landscape_16_9"
    
    for attempt in range(max_retries):
        try:
            print(f"  Attempt {attempt+1}/{max_retries}...", end=" ", flush=True)
            
            session = requests.Session()
            response = session.get(url, allow_redirects=True, timeout=60)
            
            if response.status_code != 200:
                print(f"HTTP {response.status_code}, waiting...")
                time.sleep(15)
                continue
            
            content = response.content
            final_url = response.url
            
            if 'default.jpeg' in final_url or not is_real_image(content):
                print(f"placeholder/waiting, retry in 18s...")
                time.sleep(18)
                continue
            
            img = process_image(content, is_banner)
            img.save(output_path, 'WEBP', quality=88, method=6)
            
            file_size = os.path.getsize(output_path)
            if file_size > 30000:
                w, h = img.size
                print(f"SUCCESS! Saved ({w}x{h}, {file_size//1024}KB)")
                return True
            else:
                print(f"file too small ({file_size} bytes), retrying...")
                time.sleep(10)
                
        except Exception as e:
            print(f"error: {e}")
            time.sleep(15)
    
    print(f"FAILED after {max_retries} attempts")
    return False

def main():
    print("=" * 60)
    print("Noise Barrier Image Generator")
    print("=" * 60)
    
    os.makedirs(IMG_DIR, exist_ok=True)
    
    missing = get_missing_images()
    print(f"\nFound {len(missing)} images to generate\n")
    
    success = 0
    failed = []
    
    for i, (filename, prompt_name, is_banner) in enumerate(missing):
        print(f"[{i+1}/{len(missing)}] Generating: {filename} ({'BANNER' if is_banner else 'content'})")
        img_type = "BANNER" if is_banner else "content"
        
        result = generate_image(filename, prompt_name, is_banner)
        if result:
            success += 1
        else:
            failed.append(filename)
        
        if i < len(missing) - 1:
            wait_time = 8
            print(f"  Waiting {wait_time}s before next image...")
            time.sleep(wait_time)
        print()
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Successfully generated: {success}")
    print(f"Failed: {len(failed)}")
    if failed:
        print("Failed files:")
        for f in failed:
            print(f"  - {f}")
    
    webp_count = len([f for f in os.listdir(IMG_DIR) if f.endswith('.webp')])
    print(f"\nTotal webp files in img/: {webp_count}")

if __name__ == "__main__":
    main()
