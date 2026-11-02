import os

found = []
for root, dirs, files in os.walk('src'):
    for f in files:
        if f.endswith(('.ts', '.tsx', '.json', '.html')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                for idx, line in enumerate(fp):
                    if '408' in line:
                        found.append((path, idx + 1, line.strip()))

print(f"Total 408 mentions found in src: {len(found)}")
for p, l, text in found:
    print(f"{p}:{l} -> {text}")
