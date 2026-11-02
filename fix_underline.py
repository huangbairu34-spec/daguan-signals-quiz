with open('build_full_database.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any variant of \underline
import re
text = re.sub(r'\\+underline\{(\d+)\}', r'\\mathbf{\1}_{k=0}', text)

with open('build_full_database.py', 'w', encoding='utf-8') as f:
    text = f.write(text)

print("Replaced all underline tags cleanly!")
