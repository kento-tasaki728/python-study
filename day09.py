apple_price = 150

for i in range(1,6):
    apple_total = i * apple_price
    print(str(i) + "個購入:" + str(apple_total))
    
    if apple_total >= 500:
      print("送料無料")
    else :
      print("送料200円")
    