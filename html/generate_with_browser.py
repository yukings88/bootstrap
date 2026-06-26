#!/usr/bin/env python3
import os
import re
import time
import urllib.parse
import subprocess
import json
import sys
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
    
    all_webps = set()
    for fn in os.listdir(HTML_DIR):
        if not fn.endswith('.html'):
            continue
        with open(os.path.join(HTML_DIR, fn)) as f:
            c = f.read()
        for m in re.finditer(r'img/([^"\'\s)]+)', c):
            p = m.group(1)
            if p.endswith('.webp') and p not in ('yukings-factory.webp',):
                all_webps.add(p)
    
    missing = []
    for p in sorted(all_webps):
        fp = os.path.join(IMG_DIR, p)
        is_banner = p in hero
        target_h = 600 if is_banner else 768
        
        if not os.path.exists(fp):
            mm = re.match(r'(.+)-([a-f0-9]{8})\.webp$', p)
            if mm:
                missing.append((p, mm.group(1), is_banner, target_h))
        else:
            try:
                img = Image.open(fp)
                w, h = img.size
                if w != 1368 or h != target_h or os.path.getsize(fp) < 30000:
                    mm = re.match(r'(.+)-([a-f0-9]{8})\.webp$', p)
                    if mm:
                        missing.append((p, mm.group(1), is_banner, target_h))
            except:
                mm = re.match(r'(.+)-([a-f0-9]{8})\.webp$', p)
                if mm:
                    missing.append((p, mm.group(1), is_banner, target_h))
    
    return missing

def make_prompt(name):
    prompt_map = {
        'absorptive-highway-noise-barrier-polycarbonate-window': 'professional photograph of absorptive highway noise barrier with transparent polycarbonate window panels, modern road infrastructure, clear blue sky, engineering photography',
        'absorptive-noise-barrier-louvered-metal-panel': 'close-up detail of louvered metal absorptive noise barrier panel, perforated steel acoustic insulation, industrial product photography',
        'aluminum-galvanized-steel-noise-barrier-comparison': 'comparison showing aluminum vs galvanized steel noise barrier panels, side by side material samples, technical engineering',
        'aluminum-lightweight-bridge-parapet-noise-barrier': 'lightweight aluminum noise barrier installed on bridge parapet, modern bridge infrastructure, elevated highway, blue sky',
        'aluminum-noise-barrier': 'aluminum noise barrier panel product, silver metallic finish, industrial manufacturing, professional product photography',
        'bifacial-solar-noise-barrier-installation-railway': 'bifacial solar photovoltaic noise barrier installation along railway track, construction workers installing panels, renewable energy',
        'bridge-elevated-road-noise-barrier-viaduct-parapet': 'noise barrier on elevated road viaduct bridge parapet, modern concrete viaduct in urban setting, cityscape background',
        'bridge-noise-barrier': 'noise barrier panels installed on highway bridge, steel structure, modern infrastructure, construction photography',
        'bridge-parapet-reflective-noise-barrier': 'reflective noise barrier mounted on bridge parapet wall, rigid metal panels, concrete bridge edge, engineering detail',
        'cantilever-cap-hybrid-noise-barrier-bridge': 'cantilever cap hybrid noise barrier on bridge, overhanging top section for acoustic diffraction, advanced engineering',
        'clear-acrylic-sound-barrier-residential-street': 'clear transparent acrylic sound barrier wall along residential street, modern houses visible through panels, suburban neighborhood',
        'curved-cap-noise-wall-diffraction-engineering': 'curved top cap noise wall showing acoustic diffraction engineering, sound wave visualization, civil engineering illustration',
        'en-1793-acoustic-performance-classification': 'EN 1793 standard acoustic performance classification chart for noise barriers, technical document, sound absorption testing data',
        'en-1794-mechanical-performance-noise-barrier-impact-test': 'EN 1794 mechanical performance impact resistance testing on noise barrier panel, laboratory equipment, quality control',
        'en-1794-mechanical-performance-noise-barriers': 'EN 1794 mechanical performance standards for noise barriers, technical specification, structural engineering requirements',
        'heavy-industrial-noise-barrier-factory-boundary-wall': 'heavy duty industrial noise barrier at factory boundary wall, large manufacturing plant perimeter, thick acoustic panels',
        'high-speed-rail-aero-acoustic-noise-barriers': 'aero-acoustic noise barriers for high speed rail, aerodynamic shape, streamlined top profile, bullet train passing by',
        'high-speed-rail-noise-barrier-aero-acoustic-pulse-pressure': 'high speed rail noise barrier with aero-acoustic pulse pressure visualization, airflow diagram, technical illustration',
        'high-speed-railway-hybrid-noise-barrier': 'hybrid noise barrier along high speed railway line, absorptive and reflective panels, train passing at speed',
        'high-speed-railway-noise-barrier-train-acoustic-wall': 'high speed railway acoustic noise barrier wall with bullet train passing, motion blur, concrete and steel panels',
        'highway-expressway-noise-barrier-motorway-wall': 'noise barrier wall along busy highway expressway motorway, multiple lanes traffic, green landscape, blue sky',
        'highway-expressway-solar-pv-noise-barrier': 'solar PV photovoltaic noise barrier along highway expressway, blue solar panels integrated into noise wall',
        'highway-noise-barrier-project-urban-expressway': 'completed highway noise barrier project on urban expressway, city skyline in background, multi-lane road',
        'highway-noise-control-expressway-ringroad': 'highway noise control on urban ring road expressway, circular road around city, traffic noise mitigation, aerial view',
        'highway-rigid-reflective-noise-barrier': 'rigid reflective noise barrier panels along highway, solid non-porous metal sheets, concrete posts, motorway sound wall',
        'hot-dip-galvanized-noise-barrier-panel-factory': 'hot-dip galvanized noise barrier panels in factory, zinc coated steel, industrial manufacturing, production line',
        'how-to-choose-noise-barrier-panel-depth': 'guide showing how to choose noise barrier panel depth comparison 80mm 100mm 120mm 140mm, technical diagram',
        'hybrid-acoustic-barrier-cross-section-diagram-installation': 'cross-section technical diagram of hybrid acoustic barrier installation, layered construction, engineering blueprint',
        'hybrid-noise-barrier': 'hybrid noise barrier product combining absorptive and reflective materials, dual-layer acoustic panel',
        'hybrid-noise-barrier-dual-layer': 'dual-layer hybrid noise barrier construction detail, cross section showing inner absorption and outer reflective shell',
        'hybrid-noise-barrier-dual-layer-railway-road': 'dual-layer hybrid noise barrier alongside railway and road, combined transportation corridor, integrated infrastructure',
        'industrial-factory-noise-barrier-machinery-enclosure': 'industrial noise barrier as machinery enclosure inside factory, acoustic panels surrounding noisy equipment',
        'industrial-noise-barrier': 'industrial noise barrier product, heavy duty acoustic panels for factories, dark gray metal finish',
        'industrial-noise-barrier-project-power-plant': 'industrial noise barrier project surrounding power plant, large energy infrastructure, cooling towers, perimeter acoustic wall',
        'industrial-plant-boundary-hybrid-noise-wall': 'hybrid noise wall at industrial plant boundary, factory perimeter fence, combination sound wall',
        'industrial-plant-boundary-reflective-noise-wall': 'reflective noise wall at industrial plant boundary, solid panels, factory perimeter security wall, heavy industry',
        'industrial-plant-boundary-solar-acoustic-wall': 'solar acoustic wall at industrial plant boundary, PV panels integrated into noise barrier, renewable energy for factory',
        'industrial-plant-factory-noise-barrier-machinery-noise-control': 'factory noise barrier for machinery noise control, industrial equipment enclosures, worker safety, manufacturing',
        'insertion-loss-sound-insulation-absorption-coefficients-noise-barriers': 'technical chart showing insertion loss, sound insulation and absorption coefficients for noise barriers, acoustic graph',
        'modern-industrial-noise-barrier-factory-site-aerial': 'aerial drone view of modern industrial noise barrier surrounding factory site, large manufacturing complex, bird eye view',
        'modern-reflective-noise-barrier-highway-rigid-panel': 'modern reflective noise barrier on highway with rigid smooth panels, clean contemporary design, gray metallic finish',
        'new-energy-solar-noise-barrier-projects-pv': 'new energy solar noise barrier projects, large scale PV photovoltaic installation, renewable energy infrastructure',
        'noise-barrier-acoustic-principle-diagram-reflective-absorptive': 'acoustic principle diagram showing reflective vs absorptive noise barriers, sound wave propagation, educational infographic',
        'noise-barrier-applications-highway-railway-industrial-residential': 'noise barrier applications: highway, railway, industrial, residential, multiple use cases overview',
        'noise-barrier-blog-technical-articles-engineering-insight-lab': 'noise barrier blog technical articles, engineering insight lab, desk with blueprints, laptop showing acoustic data',
        'noise-barrier-faq-deep-dive': 'frequently asked questions about noise barriers, FAQ document with magnifying glass, deep dive technical analysis',
        'noise-barrier-industry-news-2': 'noise barrier industry news, newspaper headlines, construction site background, acoustic engineering developments',
        'noise-barrier-materials-steel-aluminum-acrylic-concrete': 'noise barrier material samples: steel, aluminum, acrylic, concrete arranged together, material comparison display',
        'noise-barrier-project-checklist': 'noise barrier project checklist document on clipboard, construction site background, planning specification sheet',
        'noise-barrier-technical-article-engineering-2': 'technical engineering article about noise barriers, open book with diagrams, engineering desk, professional publication',
        'noise-barrier-top-profiles-flat-curved-y-shaped': 'comparison of noise barrier top profiles: flat straight, curved arc, Y-shaped, three designs side by side',
        'railway-metro-hybrid-noise-barrier': 'hybrid noise barrier along railway metro line, urban commuter train, city public transit infrastructure',
        'railway-metro-solar-pv-noise-barrier': 'solar PV noise barrier along railway metro line, urban train passing, blue photovoltaic panels',
        'railway-noise-barrier': 'railway noise barrier panels along train track, railroad sound wall, gravel ballast, steel rails',
        'railway-noise-barrier-hybrid-slipstream-panel': 'hybrid noise barrier with slipstream panels for railway, aerodynamic design for train wind pressure, high speed rail',
        'railway-noise-barrier-project-high-speed-corridor': 'completed railway noise barrier project on high speed corridor, long wall stretching into distance, modern rail infrastructure',
        'railway-noise-barriers-high-speed-rail': 'noise barriers along high speed rail line, dedicated HSR corridor, concrete and steel acoustic walls',
        'railway-noise-reduction-high-speed-corridor': 'railway noise reduction on high speed corridor, quieter communities near rail line, noise mitigation benefits',
        'railway-trackside-rigid-reflective-noise-barrier': 'rigid reflective noise barrier trackside at railway, solid panels close to tracks, ballast and rails visible',
        'reflective-noise-barrier': 'reflective noise barrier product, solid rigid panel that reflects sound, hard non-porous surface, professional product shot',
        'reflective-sound-barrier-steel-panel-installation': 'reflective sound barrier steel panel installation on highway, construction workers mounting panels, active construction site',
        'residential-community-noise-protection-housing': 'residential community noise protection for housing estate, apartment buildings protected by noise wall, peaceful neighborhood',
        'residential-noise-barriers-community-garden': 'residential noise barriers with community garden, green landscaping near homes, attractive sound wall with flowers plants',
        'residential-sensitive-highway-hybrid-noise-barrier': 'hybrid noise barrier protecting residential area near highway, houses close to motorway, acoustic protection, peaceful homes',
        'semi-enclosed-u-shape-noise-barrier-highway-railway': 'semi-enclosed U-shaped noise barrier covering highway or railway, tunnel-like partial cover structure, advanced noise protection',
        'semi-enclosed-u-shape-noise-wall-cantilever-cover-plate-installation': 'semi-enclosed U-shaped noise wall with cantilever cover plate installation, workers installing top cover, complex engineering',
        'solar-noise-barrier-project-pv-highway': 'solar noise barrier PV project along highway, large scale photovoltaic sound walls, blue panels along motorway',
        'solar-photovoltaic-noise-barrier-highway-pv-modules': 'solar photovoltaic noise barrier on highway, close-up of PV modules integrated into sound wall panels, blue solar cells',
        'solar-photovoltaic-noise-barrier-pv-modules': 'solar photovoltaic noise barrier PV modules, bifacial solar panels designed for noise barrier integration',
        'solar-pv-integrated-noise-barriers': 'solar PV integrated noise barrier system, complete solution combining sound insulation with clean energy generation',
        'urban-arterial-road-solar-noise-wall': 'solar noise wall along urban arterial road, city street with PV sound barrier, buildings in background',
        'yukings-noise-barrier-free-quotation-engineer': 'professional engineer offering free quotation for noise barrier project, friendly consultant at desk with blueprints, business meeting',
        'yukings-noise-barrier-terms-of-service-legal': 'terms of service legal document for noise barrier company, contract papers, legal agreement, professional documentation',
        'yukings-privacy-policy-data-protection-gdpr': 'privacy policy and data protection GDPR compliance, document with lock icon, shield symbol, personal data security',
        'residential-community-noise-barrier-apartment-housing-estate': 'residential community noise barrier protecting apartment housing estate, multi-story buildings, acoustic wall, peaceful living',
        'residential-noise-reduction-projects-community': 'residential noise reduction projects in community, before and after comparison, quieter neighborhood, quality of life',
        'rusted-old-noise-barrier-failed-corrosion-urban-highway': 'rusted old noise barrier showing failed corrosion protection on urban highway, weathered panels, maintenance issue',
        'solar-energy-noise-barrier-pv-infrastructure': 'solar energy noise barrier PV infrastructure, large scale photovoltaic installation, clean energy and transportation'
    }
    base_prompt = prompt_map.get(name, None)
    if base_prompt:
        return base_prompt + ", high quality, professional photography, 16:9 landscape, photorealistic, sharp focus, detailed, cinematic lighting"
    else:
        pretty_name = name.replace('-', ' ')
        return f"professional photograph of {pretty_name}, noise barrier acoustic infrastructure, high quality, photorealistic, 16:9 landscape"

def run_ab(cmd_list, timeout=120):
    try:
        result = subprocess.run(cmd_list, capture_output=True, text=True, timeout=timeout)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "", "timeout", -1

def wait(ms):
    time.sleep(ms / 1000.0)

def generate_one_image(filename, prompt_name, is_banner, target_h, max_retries=25):
    output_path = os.path.join(IMG_DIR, filename)
    prompt = make_prompt(prompt_name)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"{API_BASE}?prompt={encoded_prompt}&image_size=landscape_16_9"
    
    for attempt in range(max_retries):
        print(f"    Attempt {attempt+1}/{max_retries}...", end=" ", flush=True)
        
        out, err, rc = run_ab(["agent-browser", "open", url], timeout=90)
        if rc != 0:
            print(f"open error (rc={rc}), wait 10s...")
            wait(10000)
            continue
        
        wait(6000)
        
        title_out, err, rc = run_ab(["agent-browser", "get", "title"], timeout=15)
        url_out, err2, rc2 = run_ab(["agent-browser", "get", "url"], timeout=15)
        
        print(f"Title: {title_out[:60]}")
        
        if "default.jpeg" in title_out or "1832" in title_out:
            wait_sec = 18 + min(attempt, 10)
            print(f"      Placeholder detected, waiting {wait_sec}s before retry...")
            wait(wait_sec * 1000)
            continue
        
        if "1368" in title_out or (url_out and "default.jpeg" not in url_out and "lf-cdn" in url_out):
            print(f"      Got real image URL, downloading...")
            cdn_url = url_out.strip()
            
            tmp_path = f"/tmp/gen_{filename}"
            curl_cmd = ["curl", "-s", "-L", "-o", tmp_path,
                       "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                       "--max-time", "60", cdn_url]
            run_ab(curl_cmd, timeout=70)
            
            if not os.path.exists(tmp_path):
                print(f"      Download failed, retry...")
                wait(10000)
                continue
            
            try:
                with open(tmp_path, 'rb') as f:
                    content = f.read()
                
                img = Image.open(BytesIO(content))
                orig_w, orig_h = img.size
                print(f"      Downloaded: {orig_w}x{orig_h}, {len(content)//1024}KB")
                
                if orig_w < 1000 or orig_h < 500:
                    print(f"      Too small, retry...")
                    wait(10000)
                    continue
                
                img = img.convert('RGB')
                target_w = 1368
                scale = max(target_w / orig_w, target_h / orig_h)
                new_w = int(orig_w * scale)
                new_h = int(orig_h * scale)
                img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                
                left = (new_w - target_w) // 2
                top = (new_h - target_h) // 2
                img = img.crop((left, top, left + target_w, top + target_h))
                
                img.save(output_path, 'WEBP', quality=88, method=6)
                
                file_size = os.path.getsize(output_path)
                if file_size > 30000:
                    w, h = img.size
                    print(f"      SAVED: {w}x{h}, {file_size//1024}KB")
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)
                    return True
                else:
                    print(f"      Output file too small ({file_size}B), retry...")
                    wait(10000)
            except Exception as e:
                print(f"      Processing error: {e}")
                wait(10000)
        else:
            print(f"      Unexpected state, waiting 15s...")
            wait(15000)
    
    print(f"    FAILED after {max_retries} attempts")
    return False

def main():
    print("=" * 60)
    print("Image Generator (agent-browser)")
    print("=" * 60)
    
    os.makedirs(IMG_DIR, exist_ok=True)
    
    run_ab(["agent-browser", "close", "--all"], timeout=10)
    wait(2000)
    run_ab(["agent-browser", "set", "viewport", "1920", "1080"], timeout=10)
    
    missing = get_missing_images()
    print(f"\nFound {len(missing)} images to process\n")
    
    success = 0
    failed = []
    
    for i, (filename, prompt_name, is_banner, target_h) in enumerate(missing):
        img_type = "BANNER" if is_banner else "content"
        print(f"[{i+1}/{len(missing)}] {filename} ({img_type}, target: 1368x{target_h})")
        
        result = generate_one_image(filename, prompt_name, is_banner, target_h)
        if result:
            success += 1
        else:
            failed.append(filename)
        
        with open('/tmp/gen_progress.json', 'w') as f:
            json.dump({'done': i+1, 'success': success, 'failed': failed}, f)
        
        if i < len(missing) - 1:
            print(f"    Pausing 8s before next...")
            wait(8000)
        print()
    
    run_ab(["agent-browser", "close"], timeout=10)
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Successfully processed: {success}")
    print(f"Failed: {len(failed)}")
    if failed:
        print("Failed files:")
        for f in failed:
            print(f"  - {f}")
    
    webp_count = len([f for f in os.listdir(IMG_DIR) if f.endswith('.webp')])
    print(f"\nTotal webp files in img/: {webp_count}")

if __name__ == "__main__":
    main()
