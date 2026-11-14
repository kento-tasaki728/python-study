product = {
    "name": "りんご",
    "stock": 10,
    "price": 150
}

key = input("削除する項目を入力してください：")
deleted_value = product.pop(key, None)
if deleted_value is None:
    print(f"{key}は存在しません。")
else:
    print("削除しました")

print(deleted_value)
print(product)