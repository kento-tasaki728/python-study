apple_price = 150
orange_price = 100
banana_price = 120

apple_quantity = input("りんごの購入数量は？")
orange_quantity = input("みかんの購入数量は？")
banana_quantity = input("バナナの購入数量は？")

apple_number = int(apple_quantity)
orange_number = int(orange_quantity)
banana_number = int(banana_quantity)

apple_total = apple_price * apple_number
orange_total = orange_price * orange_number
banana_total = banana_price * banana_number

print("りんごの購入金額は" + str(apple_total) + "円です")
print("みかんの購入金額は" + str(orange_total) + "円です")
print("バナナの購入金額は" + str(banana_total) + "円です")

total = apple_total + orange_total + banana_total
tax_rate = "0.1"
tax_number = float(tax_rate)
tax_amount = total * tax_number
print("税抜合計金額は" + str(total) + "円です")
print("消費税額は" + str(tax_amount) + "円です")

if total >= 5000:
  shipping = 0
elif total >= 3000:
  shipping = 300
else :
  shipping = 500
  
print("送料は"+ str(shipping) + "円です")

final_total = total + tax_amount+ shipping
print("最終支払金額は" + str(final_total) + "円です")