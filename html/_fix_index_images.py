
import urllib.request, hashlib, os, re

urls = [
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=noise-barrier-acoustic-principle-diagram-reflective-absorptive&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=noise-barrier-materials-steel-aluminum-acrylic-concrete&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=noise-barrier-applications-highway-railway-industrial-residential&image_size=landscape_16_9',
    'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=noise-barrier-top-profiles-flat-curved-y-shaped&image_size=landscape_16_9',
]

out_dir = '/workspace/html/img'
os.makedirs(out_dir, exist_ok=True)

replacements = {}
for url in urls:
    m = re.search(r'\?prompt=([^&]+)&', url)
    prompt = urllib.parse.unquote(m.group(1)) if m else 'image'
    safe = re.sub(r'[^a-z0-9-]+', '-', prompt.lower()).strip('-')[:60]
    hash_suffix = hashlib.md5(url.encode()).hexdigest()[:5]
    fname = 'nb-' + safe + '-' + hash_suffix + '.webp'
    fpath = os.path.join(out_dir, fname)
    if not os.path.exists(fpath):
        try:
            req = urllib.request.urlopen(url, timeout=60)
            data = req.read()
            headers = dict(req.headers)
            with open(fpath, 'wb') as f:
                f.write(data)
            with open(fpath + '.headers.txt', 'w') as f:
                for k, v in headers.items():
                    f.write(k + ': ' + v + '\n')
            ct = headers.get('Content-Type', '?')
            print('Downloaded: ' + fname + ' (' + str(len(data)) + ' bytes, ' + ct + ')')
        except Exception as e:
            print('FAILED: ' + url + ': ' + str(e))
    else:
        print('Exists: ' + fname)
    replacements[url] = 'img/' + fname

index_path = '/workspace/html/index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()
for url, v in replacements.items():
    orig_url = url.replace('/text_to_image?', '/text-to-image?')
    content = content.replace(orig_url, v)
    content = content.replace(url, v)
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('\nDone replacements in index.html')
