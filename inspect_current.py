import re

with open('src/data/signalsQuestions.ts', 'r', encoding='utf-8') as f:
    content = f.read()

ids = re.findall(r'"id":\s*["\']([^"\']+)["\']', content)
print("Total questions in signalsQuestions.ts:", len(ids))

# Count per chapter
from collections import Counter
chapters = re.findall(r'"chapter":\s*["\']([^"\']+)["\']', content)
print("Chapter distribution:")
for ch, count in sorted(Counter(chapters).items()):
    print(f"  {ch}: {count}")
