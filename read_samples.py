with open('sample_zhengjunli.txt', 'r', encoding='utf-8') as f:
    text_zjl = f.read()

print("=== SAMPLE ZHENG JUNLI ===")
for line in text_zjl.splitlines()[:70]:
    try:
        print(line)
    except:
        print(line.encode('ascii', 'replace').decode('ascii'))

print("\n=== SAMPLE OPPENHEIM ===")
with open('sample_oppenheim.txt', 'r', encoding='utf-8') as f:
    text_obh = f.read()
for line in text_obh.splitlines()[:70]:
    try:
        print(line)
    except:
        print(line.encode('ascii', 'replace').decode('ascii'))
