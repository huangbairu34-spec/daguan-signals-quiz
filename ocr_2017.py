import os
import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open('题库/2017广东工业大学837参考答案.pdf')
pages = []
for i in range(len(doc)):
    pix = doc[i].get_pixmap(dpi=150)
    res, _ = ocr(pix.tobytes('png'))
    pages.append('\n'.join([l[1] for l in res]) if res else '')
open('ocr_2017.txt', 'w', encoding='utf-8').write('\n--- PAGE ---\n'.join(pages))
print("2017 OCR done.")
