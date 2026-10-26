"""Build index.html (repo root) and the inlined artifact from src/template.html.
Run from anywhere:  python3 src/build.py
"""
import re, base64, os, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root/'src'/'template.html').read_text()
assets = root/'assets'
imgs = sorted(set(re.findall(r'\{\{IMG:([^}]+)\}\}', tpl)))
missing = [i for i in imgs if not (assets/i).exists()]
assert not missing, f"missing assets: {missing}"
# deployable page at repo root (GitHub Pages serves from /)
dep = re.sub(r'\{\{IMG:([^}]+)\}\}', lambda m: 'assets/'+m.group(1), tpl)
i = dep.index('<nav class="nav"')
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        + dep[:i] + '</head>\n<body>\n' + dep[i:] + '\n</body>\n</html>\n')
(root/'index.html').write_text(html)
# single-file preview with images inlined (for claude.ai artifact republish); not committed
out = root/'src'/'dist'; out.mkdir(exist_ok=True)
art = re.sub(r'\{\{IMG:([^}]+)\}\}', lambda m: 'data:image/jpeg;base64,'+base64.b64encode((assets/m.group(1)).read_bytes()).decode(), tpl)
# fonts inlined too (the artifact host blocks relative/external assets), and relative preloads dropped
art = re.sub(r'url\("assets/fonts/([^"]+)"\)', lambda m: 'url("data:font/woff2;base64,'+base64.b64encode((assets/'fonts'/m.group(1)).read_bytes()).decode()+'")', art)
art = re.sub(r'<link rel="preload" href="assets/fonts/[^>]+>\n', '', art)
(out/'halapeno-artifact.html').write_text(art)
print('index.html', os.path.getsize(root/'index.html')//1024, 'KB |', len(imgs), 'images |', 'artifact', os.path.getsize(out/'halapeno-artifact.html')//1024, 'KB')
