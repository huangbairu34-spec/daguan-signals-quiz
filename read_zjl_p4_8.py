with open('zjl_p4_8.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

for l in txt.splitlines()[:60]:
    try:
        print(l)
    except:
        print(l.encode('ascii', 'replace').decode('ascii'))
