import json

data = json.load(open('pymupdf_results.json', encoding='utf-8'))
for item in data:
    fn = item['file']
    pg = item['pages']
    has_text = item['has_text']
    tl = item['text_len_5_pages']
    sp = item.get('sample', '')[:60].replace('\n', ' ')
    print(f"{'TEXT' if has_text else 'SCAN':<4} | p:{pg:<3} | {tl:<5} | {fn:<40} | {sp}")
