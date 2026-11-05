product = {
    "name": "バナナ",
    "price": 150,
    "stock": 20,
    "category": "果物"
}
for key, value in product.items():
    print(key, value)
    
product["price"] += 50
product["stock"] -= 5

for key, value in product.items():
    print(key, value)