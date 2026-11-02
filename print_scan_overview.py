import json

with open("pdf_scan_overview.json", "r", encoding="utf-8") as f:
    overview = json.load(f)

for item in overview:
    name = item.get("name", "")
    pages = item.get("pages", 0)
    has_text = item.get("has_native_text", False)
    preview = item.get("preview", "")[:60]
    print(f"[{'TEXT' if has_text else 'SCAN'}] {pages:3d}p | {name[:45]} | {preview}")
