import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
doc = pymupdf.open('题库/25版绝杀32专题.pdf')
pages = []
for i in range(min(4, len(doc))):
    pix = doc[i].get_pixmap(dpi=150)
    res, _ = ocr(pix.tobytes('png'))
    pages.append('\n'.join([l[1] for l in res]) if res else '')
open('ocr_32_p1_4.txt', 'w', encoding='utf-8').write('\n--- PAGE ---\n'.join(pages))
print("32 topics OCR p1-4 done.")
