import pymupdf

doc = pymupdf.open("题库/奥本海姆课后题详细解答(含第八章).pdf")
for p in range(2, 10):
    print(f"=== Page {p+1} ===")
    txt = doc[p].get_text()
    for l in txt.splitlines()[:25]:
        print("  ", l)
