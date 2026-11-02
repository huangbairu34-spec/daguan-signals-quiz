with open('build_full_database.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(620, min(635, len(lines))):
    print(f"{i+1}: {repr(lines[i])}")
