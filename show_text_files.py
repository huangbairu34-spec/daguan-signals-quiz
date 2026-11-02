import json

data = json.load(open('pdf_text_inventory.json', encoding='utf-8'))
for item in data:
    fn = item['file']
    pg = item['pages']
    tl = item['total_text_len']
    sc = item['is_scanned']
    if not sc:
        print(f"HAS TEXT: {fn} | pages: {pg} | text_chars: {tl}")
