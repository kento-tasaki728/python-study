prices = []

for i in range(5):
    price = int(input("商品価格を入力："))
    prices.append(price)
    
total = sum(prices)
print(f"合計金額：{total}円")

max_price = max(prices)
min_price = min(prices)
print(f"最高価格：{max_price}円")
print(f"最低価格：{min_price}円")

average_price = total / len(prices)
print(f"平均価格：{average_price:.2f}円")