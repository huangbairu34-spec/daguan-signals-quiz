import json

data = json.load(open('classic_837_blocks.json', encoding='utf-8'))
with open('blocks_preview.txt', 'w', encoding='utf-8') as out:
    for p in data[:5]:
        out.write(f"=== PAGE {p['page']} ===\n")
        for b in p['blocks'][:6]:
            b_clean = b.replace('\n', ' ')[:100]
            out.write("  - " + b_clean + "\n")

print("Saved to blocks_preview.txt")
