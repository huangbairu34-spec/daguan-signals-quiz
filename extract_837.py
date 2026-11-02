import pymupdf

doc = pymupdf.open('题库/837上岸经典必刷题(含答案).pdf')
print("Total pages:", len(doc))
full_text = ""
for i, page in enumerate(doc):
    t = page.get_text()
    full_text += f"\n=== PAGE {i+1} ===\n" + t

with open('837_classic_full_text.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print("Saved 837_classic_full_text.txt, length:", len(full_text))
print("First 1500 chars:\n", full_text[:1500])
