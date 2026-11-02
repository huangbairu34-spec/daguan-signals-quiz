import json

data = json.load(open('pdf_summary.json', encoding='utf-8'))
for item in data:
    fn = item['filename']
    pg = item.get('pages', 0)
    sp = item.get('sample', '').replace('\n', ' ')[:70]
    has_text = len(sp.strip()) > 0
    print(f"{fn:<45} | pages: {pg:<3} | text: {'YES' if has_text else 'EMPTY/SCAN'}")
