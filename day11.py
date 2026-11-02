prices = [100, 200, 300, 400]

prices.append(500)
prices[1] = 250
prices.remove(300)

print(len(prices))
    
for x in prices:
    print(x)

    if x >= 300:
        print("高額商品")