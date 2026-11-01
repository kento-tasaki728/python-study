apple_price = "150"
orange_price = "120"
banana_price = "180"

apple_quantity = 5
orange_quantity = 8
banana_quantity = 4

apple_price_number = int(apple_price)
orange_price_number = int(orange_price)
banana_price_number = int(banana_price)

apple_total = apple_price_number * apple_quantity
orange_total = orange_price_number * orange_quantity
banana_total = banana_price_number * banana_quantity

total = apple_total + orange_total + banana_total

tax_rate = "0.1"
tax_number = float(tax_rate)
tax_amount = (total * tax_number)

total_with_tax = tax_amount + total

print("りんごの売上金額は" + str(apple_total) + "円です")
print("みかんの売上金額は" + str(orange_total) + "円です")
print("バナナの売上金額は"+ str(banana_total) + "円です")
print("税抜合計金額は" + str(total) + "円です")
print("消費税額は" + str(tax_amount) + "円です")
print("税込合計金額は" + str(total_with_tax)  + "円です")