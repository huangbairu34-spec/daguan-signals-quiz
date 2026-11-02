import os
import json
import fitz # PyMuPDF

pdf_dir = "题库"
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
print(f"Total PDFs found: {len(pdf_files)}")

results = []
for f in sorted(pdf_files):
    path = os.path.join(pdf_dir, f)
    try:
        doc = fitz.open(path)
        pages = len(doc)
        total_text = ""
        for i in range(min(5, pages)):
            total_text += doc[i].get_text()
        results.append({
            "name": f,
            "pages": pages,
            "has_native_text": len(total_text.strip()) > 50,
            "preview": total_text[:200].replace('\n', ' ')
        })
        doc.close()
    except Exception as e:
        results.append({"name": f, "error": str(e)})

with open("pdf_scan_overview.json", "w", encoding="utf-8") as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print("Overview written to pdf_scan_overview.json")
