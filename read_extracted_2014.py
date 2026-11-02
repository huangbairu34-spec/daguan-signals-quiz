with open("text_2014_2021.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Print lines 1 to 100
for i in range(min(120, len(lines))):
    print(f"{i+1:3d}: {lines[i].strip()}")
