import pymupdf

doc = pymupdf.open("题库/奥本海姆课后题详细解答(含第八章).pdf")
print("Total pages:", len(doc))
# Page 2 has contents
print("Page 2 Contents:")
print(doc[1].get_text())

# Let's check Chapter 1 page 3
print("Page 3 sample:")
print(doc[2].get_text()[:400])

# Check a few problem headers across pages
problems = []
for p in range(2, min(50, len(doc))):
    text = doc[p].get_text()
    for line in text.splitlines():
        if line.strip().startswith(('1.', '2.', '3.')) and len(line.strip()) < 15:
            problems.append((p+1, line.strip()))
print("Some problem numbers found:", problems[:20])
