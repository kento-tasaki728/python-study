name = input("商品名を入力してください：")
result = name.split(",")
before = input("置き換える文字列：")
after = input("置き換え後の文字列：")

for item in result:
    cleaned = item.strip()
    changed = cleaned.replace(before, after)
    print(changed)