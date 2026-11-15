text = input("商品名を入力してください：")
result = text.split(",")
print(result)
for item in result:
    print(item)
len_result = len(result)
print("登録商品数：" + str(len_result) + "個")