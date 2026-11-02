import os
import fitz # PyMuPDF
import json

folder = '题库'
results = []
for f in sorted(os.listdir(folder)):
    if not f.endswith('.pdf'): continue
    path = os.path.join(folder, f)
    try:
        doc = fitz.open(path)
        total_len = 0
        samples = []
        for i in range(min(5, len(doc))):
            t = doc[i].get_text()
            total_len += len(t)
            if t.strip():
                samples.append(t.strip()[:100])
        results.append({
            'file': f,
            'pages': len(doc),
            'text_len_5_pages': total_len,
            'has_text': total_len > 50,
            'sample': ' | '.join(samples)[:200]
        })
    except Exception as e:
        results.append({'file': f, 'error': str(e)})

with open('pymupdf_results.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print('Analyzed', len(results), 'files.')
