"""Check page routes, navigation, image descriptions and artwork uniqueness."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from hashlib import sha256

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=set();self.links=[];self.assets=[];self.images=[];self.h1=0;self.prev=[];self.next=[];self.top=0;self.current=0;self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='a':
            href=a.get('href','');self.links.append(href)
            if a.get('rel')=='prev':self.prev.append(href)
            if a.get('rel')=='next':self.next.append(href)
            self.top+=a.get('aria-label')=='Back to top'
            self.current+=a.get('aria-current')=='page'
        if tag in ['img','script','link']:
            src=a.get('src',a.get('href',''))
            if src:self.assets.append(src)
        if tag=='img':
            assert a.get('alt'),'Missing image description'
            self.images.append(a['src'])

pages={p.name:Page(p.read_text(encoding='utf-8')) for p in ROOT.glob('*.html')}
assert len(pages)==10,f'Expected ten pages, got {len(pages)}'
hashes={}
for name,p in pages.items():
    assert (p.h1,len(p.prev),len(p.next),p.top,p.current)==(1,1,1,1,1),f'Heading/navigation issue: {name}'
    assert {'top','main','chapter-menu'} <= p.ids,f'Missing structure: {name}'
    assert len(p.images)==1,f'Expected one unique full-width hero: {name}'
    for href in p.links+p.assets:
        u=urlsplit(href)
        if u.scheme or u.netloc:continue
        target=unquote(u.path) or name
        assert (ROOT/target).is_file(),f'{name}: missing {target}'
        if u.fragment and target in pages:assert u.fragment in pages[target].ids,f'{name}: missing anchor {href}'
    for src in p.images:
        digest=sha256((ROOT/src).read_bytes()).hexdigest()
        assert digest not in hashes,f'{name}: artwork reused from {hashes.get(digest)}'
        hashes[digest]=name
    assert pages[p.next[0]].prev==[name],f'Next/previous mismatch: {name}'

visited=[];current='index.html'
while current not in visited:visited.append(current);current=pages[current].next[0]
assert current=='index.html' and len(visited)==10,'Chapter route does not cover the site'
sire=ROOT.parent/'australiansire'
if sire.is_dir():
    for file in (sire/'assets').glob('*.webp'):
        assert sha256(file.read_bytes()).hexdigest() not in hashes,f'Sire artwork reused: {file.name}'
print('PASS: ten pages; ten unique heroes; no Sire artwork reused; all local links, assets, anchors and chapter controls valid.')
