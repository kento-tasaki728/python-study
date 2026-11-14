products = [
    {"name": "りんご", "stock": 10, "price": 150},
    {"name": "みかん", "stock": 5},
    {"name": "バナナ", "stock": 8, "price": 200},
    {"name": "ぶどう", "price": 500}
]
for product in products:
  if product.get("stock", 0) <= 0:
        continue
  print(f"{product['name']}:{product.get('stock', 0)}個、 価格{product.get('price', 0)}円")