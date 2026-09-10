"""Cheap deterministic checks for all static pages; no browser or external network."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1] / 'dist'
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.path=path; self.ids=[]; self.refs=[]; self.h1=0
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if tag=='h1': self.h1+=1
        if 'id' in d: self.ids.append(d['id'])
        if tag=='img': assert d.get('alt'), f'Missing alt: {self.path}'
        for k in ('src','href'):
            if d.get(k): self.refs.append(d[k])

pages={p.resolve():Page(p) for p in root.rglob('*.html')}
for path,page in pages.items():
    assert page.h1==1, f'H1 count: {path}'
    assert len(page.ids)==len(set(page.ids)), f'Duplicate IDs: {path}'
    for ref in page.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc: continue
        target=(root/unquote(u.path).lstrip('/') if u.path.startswith('/') else path.parent/unquote(u.path)).resolve() if u.path else path
        if target.is_dir(): target=target/'index.html'
        assert target.exists(), f'Broken file: {path}: {ref}'
        if u.fragment and target in pages: assert unquote(u.fragment) in pages[target].ids, f'Broken anchor: {path}: {ref}'
    if 'atuacao' in path.parts:
        assert all(x in page.ids for x in ['problem','action','situation','result','execution','sources-title'])
print(f'OK: {len(pages)} pages; local routes, assets, anchors, headings and evidence fields.')
