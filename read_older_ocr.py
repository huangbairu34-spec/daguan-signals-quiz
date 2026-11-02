for f in ['ocr_2020.txt', 'ocr_2019.txt', 'ocr_2018.txt']:
    print(f"=== {f} ===")
    try:
        content = open(f, encoding='utf-8').read()
        print(content[:600])
        print("...\n")
    except Exception as e:
        print(e)
