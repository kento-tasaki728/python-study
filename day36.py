product = input("商品名を入力：")
try:
    number = int(input("商品価格を入力："))
except ValueError:
    print("入力エラーです")
else:
    print("正常に入力できました")
    print(f"商品名：{product}")
    print(f"商品価格：{number}")
finally:
    print("商品登録処理を終了します")