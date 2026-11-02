with open('ocr_32_p1_4.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines()[:80]:
    try:
        print(line)
    except:
        print(line.encode('ascii', 'replace').decode('ascii'))
