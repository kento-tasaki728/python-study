def check_stock(stock):
    if stock == 0:
        return "在庫なし"
    elif stock < 6:
        return "在庫わずか"
    else:
        return "在庫あり"

apple_result = check_stock(10)
banana_result = check_stock(3)
orange_result = check_stock(0)

print(f"りんごの在庫状況: {apple_result}")
print(f"バナナの在庫状況: {banana_result}")
print(f"オレンジの在庫状況: {orange_result}")