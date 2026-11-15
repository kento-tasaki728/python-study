name = input("商品名を入力してください：")
result = name.split(",")
for item in result:
    if item.strip() == "":
        continue
    print(item.strip())
