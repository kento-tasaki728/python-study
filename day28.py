products = [
    {"name": "りんご", "stock": 10},
    {"name": "みかん", "stock": 0},
    {"name": "バナナ", "stock": 5},
    {"name": "ぶどう", "stock": 0},
    {"name": "メロン", "stock": 3}
]

for product in products:
    if product["stock"] == 0 or product["stock"] > 5:
      continue
    print(f"{product['name']}: 在庫数 {product['stock']}")