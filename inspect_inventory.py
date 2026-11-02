import json

with open('pdf_text_inventory.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, item in enumerate(data):
    print(f"[{i:02d}] pages={item['pages']:<3} len={item['total_text_len']:<6} {item['file']}")
