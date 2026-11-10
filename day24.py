def show_products(data):
    for product in data:
        print(f"商品名: {product['name']}, 価格: {product['price']}円")

products = [
    {"name": "りんご", "price": 150},
    {"name": "バナナ", "price": 100}
]

show_products(products)