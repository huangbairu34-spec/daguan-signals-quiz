import os
import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()

def ocr_pdf(pdf_path, max_pages=15):
    if not os.path.exists(pdf_path):
        return []
    doc = pymupdf.open(pdf_path)
    pages = []
    for i in range(min(max_pages, len(doc))):
        pix = doc[i].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes('png'))
        text = '\n'.join([l[1] for l in res]) if res else ''
        pages.append(text)
    return pages

# OCR 2023 exam and answer
print("Processing 2023...")
exam_2023 = ocr_pdf('题库/2023年广工837真题.pdf', 5)
ans_2023 = ocr_pdf('题库/2023广东工业大学837真题及解析.pdf', 10)
open('ocr_2023_all.txt', 'w', encoding='utf-8').write("=== EXAM 2023 ===\n" + '\n--- PAGE ---\n'.join(exam_2023) + "\n\n=== ANS 2023 ===\n" + '\n--- PAGE ---\n'.join(ans_2023))

# OCR 2022 exam and answer
print("Processing 2022...")
exam_2022 = ocr_pdf('题库/2022年广工837真题.pdf', 5)
ans_2022 = ocr_pdf('题库/2022广东工业大学837真题和参考答案.pdf', 10)
open('ocr_2022_all.txt', 'w', encoding='utf-8').write("=== EXAM 2022 ===\n" + '\n--- PAGE ---\n'.join(exam_2022) + "\n\n=== ANS 2022 ===\n" + '\n--- PAGE ---\n'.join(ans_2022))

print("OCR complete for 2023 and 2022.")
