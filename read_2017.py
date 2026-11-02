with open('ocr_2017.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines()[:60]:
    try:
        print(line)
    except:
        print(line.encode('ascii', 'replace').decode('ascii'))
