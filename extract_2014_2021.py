import os
import pymupdf

pdf_dir = "题库"
target = None
for f in os.listdir(pdf_dir):
    if "2014-2021" in f:
        target = os.path.join(pdf_dir, f)
        break

print("Found target:", target)
if target:
    doc = pymupdf.open(target)
    out_text = []
    for page_idx, page in enumerate(doc):
        text = page.get_text()
        out_text.append(f"--- PAGE {page_idx + 1} ---\n{text}")
    doc.close()
    
    with open("text_2014_2021.txt", "w", encoding="utf-8") as out:
        out.write("\n".join(out_text))
    print(f"Extracted {len(out_text)} pages, saved to text_2014_2021.txt")
