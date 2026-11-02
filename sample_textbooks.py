import os
import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()

def sample_ocr(pdf_name, pages_to_ocr):
    path = os.path.join("题库", pdf_name)
    doc = pymupdf.open(path)
    print(f"\nSampling {pdf_name} (total {len(doc)} pages)...")
    results = []
    for p in pages_to_ocr:
        if p < len(doc):
            pix = doc[p].get_pixmap(dpi=150)
            res, _ = ocr(pix.tobytes('png'))
            txt = '\n'.join([l[1] for l in res]) if res else ''
            results.append(f"--- Page {p+1} ---\n{txt}")
    doc.close()
    return '\n\n'.join(results)

# Sample 郑君里
txt_zjl = sample_ocr("001 【刷题本】郑君里课后刷题本(全).pdf", [0, 1, 2, 3, 4, 10, 20])
with open("sample_zhengjunli.txt", "w", encoding="utf-8") as f:
    f.write(txt_zjl)

# Sample 奥本海姆
txt_obh = sample_ocr("001 【刷题本】奥本海姆课后刷题本（全）.pdf", [0, 1, 2, 3, 4, 10, 20])
with open("sample_oppenheim.txt", "w", encoding="utf-8") as f:
    f.write(txt_obh)

print("Finished sampling!")
