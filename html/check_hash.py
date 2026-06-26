import re, os, hashlib
from urllib.parse import urlencode

trae_api_base = 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image'

unknown = [
    'noise-barrier-acoustic-principle-diagram-reflective-absorptive-500d466b.webp',
    'noise-barrier-applications-highway-railway-industrial-residential-d001df4a.webp',
    'noise-barrier-materials-steel-aluminum-acrylic-concrete-1f8b7e6e.webp',
    'noise-barrier-top-profiles-flat-curved-y-shaped-b63c815d.webp',
    'semi-enclosed-u-shape-noise-barrier-highway-railway-06ed9585.webp',
    'semi-enclosed-u-shape-noise-wall-cantilever-cover-plate-installation-358fec1e.webp',
]

for fname in unknown:
    m = re.match(r'(.+)-([a-f0-9]{8})\.webp$', fname)
    if not m:
        print(f"Cannot parse: {fname}")
        continue
    prompt = m.group(1)
    expected = m.group(2)
    
    print(f"\nFile: {fname}")
    print(f"  prompt: {prompt}")
    print(f"  expected hash: {expected}")
    
    for size in ['landscape_16_9', 'landscape_4_3', 'portrait_16_9', 'portrait_4_3', 'square_hd', 'square']:
        test_url = trae_api_base + '?' + urlencode({'prompt': prompt, 'image_size': size})
        h = hashlib.md5(test_url.encode()).hexdigest()[:8]
        match = "✅ MATCH!" if h == expected else ""
        print(f"    {size:20s} -> hash={h} {match}")
