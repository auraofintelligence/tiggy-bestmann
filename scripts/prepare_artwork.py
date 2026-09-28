"""Copy selected generated originals into web assets without changing the originals."""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import json

ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'artwork-manifest.json').read_text(encoding='utf-8'))
review=ROOT.parent/'outputs'/'tiggy-bestmann-review'
review.mkdir(parents=True,exist_ok=True)
sheet=Image.new('RGB',(1200,6*425),'#fffbed')
draw=ImageDraw.Draw(sheet)
for i,row in enumerate(rows):
    im=Image.open(row['path']).convert('RGB')
    if row['name']=='favicon':
        im.save(ROOT/'assets'/'brand-icon.webp',quality=92,method=6)
        im.resize((180,180),Image.Resampling.LANCZOS).save(ROOT/'assets'/'icon-180.png')
        im.save(ROOT/'assets'/'favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])
    else:
        im.save(ROOT/'assets'/(row['name']+'.webp'),quality=87,method=6)
    thumb=ImageOps.contain(im,(580,385))
    x=(i%2)*600+10;y=(i//2)*425
    sheet.paste(thumb,(x,y));draw.text((x,y+392),row['name'],fill='#16221e')
sheet.save(review/'artwork-contact-sheet.jpg',quality=90)
print(f'Prepared {len(rows)-1} original heroes and the new favicon.')
