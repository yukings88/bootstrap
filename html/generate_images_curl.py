#!/usr/bin/env python3
import os
import re
import time
import urllib.parse
import subprocess
import json
from PIL import Image
from io import BytesIO

API_BASE = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMG_DIR = "/workspace/html/img"
HTML_DIR = "/workspace/html"

BROWSER_HEADERS = [
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "-H", "Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Referer: https://trae-api-cn.mchost.guru/",
    "-H", "Sec-Ch-Ua: \"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "-H", "Sec-Ch-Ua-Mobile: ?0",
    "-H", "Sec-Ch-Ua-Platform: \"Windows\"",
    "-H", "Sec-Fetch-Dest: image",
    "-H", "Sec-Fetch-Mode: no-cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-L",
    "--max-time", "120"
]

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
        'yukings-privacy-policy-data-protection-gdpr': 'privacy policy and data protection GDPR compliance, document with lock icon, shield symbol, personal data security'
    }
    base_prompt = prompt_map.get(name, None)
    if base_prompt:
        return base_prompt + ", high quality, professional photography, 16:9 landscape, photorealistic, sharp focus, detailed"
    else:
        pretty_name = name.replace('-', ' ')
        return f"professional photograph of {pretty_name}, noise barrier acoustic infrastructure, high quality, photorealistic, 16:9 landscape"

def is_real_image(content):
    try:
        img = Image.open(BytesIO(content))
        width, height = img.size
        if width == 1832 and height == 1832:
            return False
        if width >= 1300 and height >= 700:
            img_small = img.resize((100, 100))
            pixels = list(img_small.getdata())
            from collections import Counter
            most_common = Counter(pixels).most_common(1)[0][1]
            if most_common > 5000:
                return False
            return True
        return False
    except:
        return False

def curl_download(url, output_path=None):
    cmd = ["curl", "-s", "-o", output_path if output_path else "-", "-w", "%{url_effective}\\n%{http_code}\\n%{size_download}"]
    cmd.extend(BROWSER_HEADERS)
    cmd.append(url)
    
    result = subprocess.run(cmd, capture_output=True, timeout=120)
    if result.returncode != 0:
        return None, None, None
    
    if output_path:
        output = result.stdout.decode('utf-8', errors='ignore').strip().split('\n')
        if len(output) >= 3:
            final_url = output[0]
            http_code = output[1]
            return final_url, http_code, None
        return None, None, None
    else:
        parts = result.stdout.decode('utf-8', errors='ignore').split('\n')
        if len(parts) >= 3:
            final_url = parts[-3]
            http_code = parts[-2]
            try:
                size_download = int(parts[-1])
            except:
                size_download = 0
            content_start = result.stdout.find(b'\xff\xd8')
            if content_start == -1:
                content_start = result.stdout.find(b'\x89PNG')
            if content_start == -1:
                content_start = result.stdout.find(b'RIFF')
            if content_start == -1:
                content_start = 0
            content = result.stdout[content_start:]
            return final_url, http_code, content
        return None, None, None

def process_image(content, is_banner, output_path):
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
    img = img.crop((left, top, left + target_w, top + target_h))
    
    img.save(output_path, 'WEBP', quality=88, method=6)
    return img

def generate_image(filename, prompt_name, is_banner, max_retries=20):
    output_path = os.path.join(IMG_DIR, filename)
    
    if os.path.exists(output_path) and os.path.getsize(output_path) > 30000:
        try:
            check_img = Image.open(output_path)
            w, h = check_img.size
            target_h = 600 if is_banner else 768
            if w == 1368 and h == target_h:
                print(f"  [SKIP] already exists")
                return True
        except:
            pass
    
    prompt = make_prompt(prompt_name)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"{API_BASE}?prompt={encoded_prompt}&image_size=landscape_16_9"
    
    for attempt in range(max_retries):
        try:
            print(f"  Attempt {attempt+1}/{max_retries}...", end=" ", flush=True)
            
            tmp_path = "/tmp/tra_img_download.tmp"
            final_url, http_code, _ = curl_download(url, tmp_path)
            
            if not http_code or http_code != "200":
                print(f"HTTP {http_code}, waiting 20s...")
                time.sleep(20)
                continue
            
            if not os.path.exists(tmp_path):
                print(f"no file, waiting...")
                time.sleep(15)
                continue
            
            with open(tmp_path, 'rb') as f:
                content = f.read()
            
            if 'default.jpeg' in (final_url or '') or not is_real_image(content):
                print(f"placeholder (url: {final_url[-50:] if final_url else 'none'}), waiting 20s...")
                time.sleep(20)
                continue
            
            img = process_image(content, is_banner, output_path)
            
            file_size = os.path.getsize(output_path)
            if file_size > 30000:
                w, h = img.size
                print(f"SUCCESS! {w}x{h}, {file_size//1024}KB")
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
                return True
            else:
                print(f"too small ({file_size}B), retry...")
                time.sleep(10)
                
        except Exception as e:
            print(f"error: {e}")
            import traceback
            traceback.print_exc()
            time.sleep(15)
    
    print(f"FAILED after {max_retries} attempts")
    return False

def main():
    print("=" * 60)
    print("Noise Barrier Image Generator (curl version)")
    print("=" * 60)
    
    os.makedirs(IMG_DIR, exist_ok=True)
    
    missing = get_missing_images()
    print(f"\nFound {len(missing)} images to generate\n")
    
    success = 0
    failed = []
    
    for i, (filename, prompt_name, is_banner) in enumerate(missing):
        print(f"[{i+1}/{len(missing)}] {filename} ({'BANNER' if is_banner else 'content'})")
        
        result = generate_image(filename, prompt_name, is_banner)
        if result:
            success += 1
        else:
            failed.append(filename)
        
        if i < len(missing) - 1:
            print(f"  Waiting 8s...")
            time.sleep(8)
        print()
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Success: {success}")
    print(f"Failed: {len(failed)}")
    if failed:
        for f in failed:
            print(f"  - {f}")
    
    webp_count = len([f for f in os.listdir(IMG_DIR) if f.endswith('.webp')])
    print(f"\nTotal webp files: {webp_count}")
    
    with open('/tmp/generation_results.json', 'w') as f:
        json.dump({'success': success, 'failed': failed, 'total_webp': webp_count}, f)

if __name__ == "__main__":
    main()
