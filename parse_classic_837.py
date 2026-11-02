import pymupdf
import re
import json

doc = pymupdf.open('题库/837上岸经典必刷题(含答案).pdf')
print("Total pages:", len(doc))

pages_text = []
for i in range(len(doc)):
    t = doc[i].get_text("blocks")
    block_texts = [b[4].strip() for b in t if b[4].strip()]
    pages_text.append({"page": i+1, "blocks": block_texts})

with open('classic_837_blocks.json', 'w', encoding='utf-8') as f:
    json.dump(pages_text[:10], f, ensure_ascii=False, indent=2)

print("Saved classic_837_blocks.json preview")
