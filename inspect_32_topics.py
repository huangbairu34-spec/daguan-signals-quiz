import pymupdf

doc = pymupdf.open('题库/25版绝杀32专题.pdf')
print("Pages:", len(doc))
toc = doc.get_toc()
print("TOC entries:", len(toc))
for item in toc[:40]:
    print(item)
if not toc:
    print("No native TOC, extracting text of first 6 pages...")
    for i in range(min(6, len(doc))):
        print(f"--- Page {i+1} ---")
        print(doc[i].get_text()[:400])
