import pymupdf
from rapidocr_onnxruntime import RapidOCR
import json

ocr = RapidOCR()

def extract_ocr_samples(pdf_path, pages_to_ocr):
    doc = pymupdf.open(pdf_path)
    res = {}
    for p in pages_to_ocr:
        if p < len(doc):
            pix = doc[p].get_pixmap(dpi=150)
            lines, _ = ocr(pix.tobytes('png'))
            txt = '\n'.join([l[1] for l in lines]) if lines else ''
            res[f"page_{p+1}"] = txt
    return res

# Sample 2014-2021 837
print("OCR 2014-2021 sample...")
s_2014 = extract_ocr_samples('题库/2014-2021广工837真题，14-16答案.pdf', [2, 3, 5, 6, 10, 15, 20])
with open('sample_2014_2021.json', 'w', encoding='utf-8') as f:
    json.dump(s_2014, f, ensure_ascii=False, indent=2)

print("OCR complete.")
