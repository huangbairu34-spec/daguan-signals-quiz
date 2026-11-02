with open('ocr_2019.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# print safely
for line in text.splitlines()[:80]:
    try:
        print(line)
    except:
        print(line.encode('ascii', 'replace').decode('ascii'))
