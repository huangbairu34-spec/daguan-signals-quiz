import os

files = os.listdir("题库")
with open("pdf_names.txt", "w", encoding="utf-8") as f:
    for item in sorted(files):
        if item.endswith(".pdf"):
            size = os.path.getsize(os.path.join("题库", item)) / 1024 / 1024
            f.write(f"{item} ({size:.2f} MB)\n")

print(f"Written {len(files)} items to pdf_names.txt")
