import os
import pymupdf

pdf_dir = "题库"
files = [
    "001 【刷题本】郑君里课后刷题本(全).pdf",
    "001 【刷题本】奥本海姆课后刷题本（全）.pdf",
    "奥本海姆课后题详细解答(含第八章).pdf"
]

for fname in files:
    path = os.path.join(pdf_dir, fname)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    doc = pymupdf.open(path)
    pages = len(doc)
    toc = doc.get_toc()
    print(f"\n==========================================")
    print(f"File: {fname}")
    print(f"Pages: {pages}")
    print(f"TOC entries: {len(toc)}")
    if toc:
        for item in toc[:25]:
            print("  ", item)
    
    # Check text in first 5 pages
    has_text = False
    samples = []
    for i in range(min(5, pages)):
        t = doc[i].get_text()
        if len(t.strip()) > 30:
            has_text = True
            samples.append(f"Page {i+1}: {t[:150].replace(chr(10), ' ')}")
    print(f"Has native text: {has_text}")
    for s in samples[:3]:
        print("  ", s)
    doc.close()
