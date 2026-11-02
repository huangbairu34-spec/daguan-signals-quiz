with open('build_full_database.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if r'\u' in line or r'\U' in line:
        print(f"Line {i+1}: {repr(line)}")
