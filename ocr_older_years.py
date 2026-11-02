import os
import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()

def ocr_pdf(pdf_path, max_pages=10):
    if not os.path.exists(pdf_path):
        return []
    doc = pymupdf.open(pdf_path)
    pages = []
    num_to_read = min(max_pages, len(doc))
    print(f"OCRing {pdf_path} ({num_to_read} pages)...")
    for i in range(num_to_read):
        pix = doc[i].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes('png'))
        text = '\n'.join([l[1] for l in res]) if res else ''
        pages.append(f"--- Page {i+1} ---\n" + text)
    doc.close()
    return pages

# OCR 2018, 2019, 2020
p2018 = ocr_pdf('题库/2018广东工业大学837参考答案.pdf', 6)
open('ocr_2018.txt', 'w', encoding='utf-8').write('\n\n'.join(p2018))

p2019 = ocr_pdf('题库/2019广东工业大学837答案.pdf', 6)
open('ocr_2019.txt', 'w', encoding='utf-8').write('\n\n'.join(p2019))

p2020 = ocr_pdf('题库/2020广东工业大学837参考答案.pdf', 5)
open('ocr_2020.txt', 'w', encoding='utf-8').write('\n\n'.join(p2020))

print("2018, 2019, 2020 OCR complete.")
