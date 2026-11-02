for fname in ['ocr_2024_exam_p0.txt', 'ocr_2023_all.txt', 'ocr_2022_all.txt']:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"=== {fname} (total lines: {len(lines)}) ===")
            print(''.join(lines[:30]))
    except Exception as e:
        print(f"Error reading {fname}: {e}")
