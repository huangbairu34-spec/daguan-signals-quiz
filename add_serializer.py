# -*- coding: utf-8 -*-
import json
import os

with open('build_full_database.py', 'a', encoding='utf-8') as f:
    f.write('''
# Export as TypeScript
def export_to_typescript(output_path):
    header = """import { Question } from '../types';

export const signalsAndSystemsQuestions: Question[] = """
    
    formatted_json = json.dumps(all_questions, ensure_ascii=False, indent=2)
    
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(header + formatted_json + ";\\n")
    print(f"Successfully generated {output_path} with {len(all_questions)} questions!")

if __name__ == '__main__':
    print("Total questions in bank:", len(all_questions))
    export_to_typescript('src/data/signalsQuestions.ts')
''')

print("Added serialization logic to build_full_database.py")
