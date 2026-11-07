products = [
    {"name": "りんご", "price": 200},
    {"name": "バナナ", "price": 150}
]

name = input("商品名を入力してください：")
price = int(input("価格を入力してください："))

new_product = {
    "name": name,
    "price": price
}

products.append(new_product)

for product in products:
    print(f"商品名：{product['name']}  価格：{product['price']}")
    
print(len(products))  # 商品の数を表示