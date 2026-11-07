products = [
    {"name": "りんご", "price": 200},
    {"name": "バナナ", "price": 150}
]

while True:
    name = input("商品名：")

    if name == "終了":
        break

    price = int(input("価格："))

    new_product = dict(name=name, price=price) 

    products.append(new_product)

print("【商品一覧】")
for product in products:
    print(f"商品名：{product['name']}  価格：{product['price']}")
print(f"登録商品数：{len(products)}")  # 商品の数を表示