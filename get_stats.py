import os
import pymupdf
import json

folder = '题库'
files = sorted(os.listdir(folder))
info = []
for f in files:
    if not f.endswith('.pdf'): continue
    path = os.path.join(folder, f)
    doc = pymupdf.open(path)
    sz = os.path.getsize(path)
    info.append({
        'file': f,
        'pages': len(doc),
        'size_kb': round(sz / 1024, 1)
    })

with open('file_stats.json', 'w', encoding='utf-8') as out:
    json.dump(info, out, ensure_ascii=False, indent=2)

print("Saved file_stats.json")
