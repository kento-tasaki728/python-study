products = [
    {"name": "りんご", "price": 200, "stock": 10},
    {"name": "バナナ", "price": 150, "stock": 20},
    {"name": "みかん", "price": 100, "stock": 15}
]

products[1]["price"] += 50
products[2]["stock"] -= 5

for product in products:
    print(f"{product['name']} {product['price']}  {product['stock']}")