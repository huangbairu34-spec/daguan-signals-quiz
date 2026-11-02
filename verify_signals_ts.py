import re
import json

with open('src/data/signalsQuestions.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# remove TS prefix
prefix = "import { Question } from '../types';\n\nexport const signalsAndSystemsQuestions: Question[] = "
json_str = text[len(prefix):].rstrip(';\n')

try:
    data = json.loads(json_str)
    print("Parsed JSON successfully! Count:", len(data))
    chapters = {}
    for q in data:
        chapters[q['chapter']] = chapters.get(q['chapter'], 0) + 1
    for ch, c in sorted(chapters.items()):
        print(f"  {ch}: {c} questions")
    
    # Check for empty stems, answers, analyses
    missing = []
    for q in data:
        if not q.get('stem') or not q.get('answer') or not q.get('analysis'):
            missing.append(q['id'])
    print(f"Questions missing stem/answer/analysis: {len(missing)}")

    # Check for duplicate IDs
    ids = [q['id'] for q in data]
    duplicates = [x for x in ids if ids.count(x) > 1]
    print(f"Duplicate IDs: {set(duplicates)}")

except Exception as e:
    print("JSON parsing error:", e)
