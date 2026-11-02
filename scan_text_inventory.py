import os
import pymupdf
import json

folder = '题库'
inventory = []
for f in sorted(os.listdir(folder)):
    if not f.endswith('.pdf'): continue
    path = os.path.join(folder, f)
    try:
        doc = pymupdf.open(path)
        total_text_len = 0
        all_text = []
        for i, page in enumerate(doc):
            t = page.get_text()
            total_text_len += len(t)
            if t.strip():
                all_text.append(f"--- PAGE {i+1} ---\n" + t.strip())
        
        inventory.append({
            'file': f,
            'pages': len(doc),
            'total_text_len': total_text_len,
            'is_scanned': total_text_len < 100,
            'text_preview': '\n'.join(all_text)[:1000] if all_text else ''
        })
    except Exception as e:
        inventory.append({'file': f, 'error': str(e)})

with open('pdf_text_inventory.json', 'w', encoding='utf-8') as out:
    json.dump(inventory, out, ensure_ascii=False, indent=2)

print('Done.')
