def safe_print(filename, max_lines=60):
    print(f"=== {filename} ===")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for l in lines[:max_lines]:
        try:
            print(l.rstrip())
        except:
            print(l.rstrip().encode('ascii', 'replace').decode('ascii'))

safe_print('zjl_p4_8.txt', 50)
print("\n" + "="*40 + "\n")
safe_print('obh_p4_8.txt', 50)
