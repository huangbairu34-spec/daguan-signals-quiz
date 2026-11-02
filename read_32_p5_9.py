with open('ocr_32_p5_9.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines()[:100]:
    try:
        print(line)
    except:
        print(line.encode('ascii', 'replace').decode('ascii'))
