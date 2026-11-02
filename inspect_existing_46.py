import re

content = open('src/data/signalsQuestions.ts', encoding='utf-8').read()

# Extract IDs and stems
pattern = r'\{\s*"id":\s*"([^"]+)",\s*"subject":\s*"([^"]+)",\s*"chapter":\s*"([^"]+)",\s*"section":\s*"([^"]+)",[\s\S]*?"stem":\s*"([^"]+)"'
matches = re.findall(pattern, content)

print(f"Extracted {len(matches)} questions.")
by_chap = {}
for m in matches:
    qid, subj, chap, sec, stem = m
    by_chap.setdefault(chap, []).append((qid, sec, stem[:40]))

for ch, qlist in sorted(by_chap.items()):
    print(f"\n=== {ch} ({len(qlist)} questions) ===")
    for qid, sec, s in qlist:
        print(f"  [{qid}] ({sec}) {s}")
