import os
import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()

def ocr_pdf(pdf_path, max_pages=15):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
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

# OCR 2025
p2025 = ocr_pdf('题库/2025真题和答案.pdf', 12)
with open('ocr_2025.txt', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(p2025))
print("2025 done.")

# OCR 2021
p2021_ans = ocr_pdf('题库/2021广东工业大学837参考答案.pdf', 10)
with open('ocr_2021_ans_full.txt', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(p2021_ans))
print("2021 done.")

# OCR 2024 809
p2024_809 = ocr_pdf('题库/2024广东工业大学809真题及解析.pdf', 8)
with open('ocr_2024_809.txt', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(p2024_809))
print("2024 809 done.")
