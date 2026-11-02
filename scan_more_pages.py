import os
import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()

def scan_pages(pdf_name, page_range):
    path = os.path.join("题库", pdf_name)
    doc = pymupdf.open(path)
    res_list = []
    for p in page_range:
        pix = doc[p].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes('png'))
        txt = '\n'.join([l[1] for l in res]) if res else ''
        res_list.append(f"=== Page {p+1} ===\n{txt}")
    doc.close()
    return '\n\n'.join(res_list)

# 郑君里 pages 4 to 8
zjl_txt = scan_pages("001 【刷题本】郑君里课后刷题本(全).pdf", range(3, 8))
with open("zjl_p4_8.txt", "w", encoding="utf-8") as f:
    f.write(zjl_txt)

# 奥本海姆 pages 4 to 8
obh_txt = scan_pages("001 【刷题本】奥本海姆课后刷题本（全）.pdf", range(3, 8))
with open("obh_p4_8.txt", "w", encoding="utf-8") as f:
    f.write(obh_txt)

print("Scan p4-8 done!")
