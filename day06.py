price = input("購入金額を入力してください：")

price_number = int(price)

if price_number >= 5000:
    print("送料無料です")
elif price_number >= 3000:
    print("送料300円です")
else :
    print("送料500円です")