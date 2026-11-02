with open('837_classic_full_text.txt', 'r', encoding='utf-8') as f:
    lines = [f.readline() for _ in range(60)]

with open('837_preview.txt', 'w', encoding='utf-8') as out:
    out.writelines(lines)

print("Saved preview to 837_preview.txt")
