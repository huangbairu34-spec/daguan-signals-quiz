import os
import pymupdf

folder = '题库'
target_file = os.path.join(folder, '2021年广工837真题.pdf')
doc = pymupdf.open(target_file)
print("Page count:", len(doc))
for i, page in enumerate(doc):
    imgs = page.get_images()
    print(f"Page {i}: {len(imgs)} images, text len: {len(page.get_text())}")
