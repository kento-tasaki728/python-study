age = 25
height = 170.5
name = "Python"

print(type(age))
print(type(height))
print(type(name))

product_name = "book"
product_price = 1100
tax_rate = 0.1

print(type(product_name))
print(type(product_price))
print(type(tax_rate))

tax = product_price * tax_rate
total_price = product_price + tax

print("商品名：", product_name)
print("税抜価格：",product_price)
print("消費税額：",tax)
print("税込価格：",total_price)

print(type(total_price))