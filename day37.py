product = input("商品名を入力：")
try:
    stock = int(input("商品在庫を入力："))

    if stock < 0:
        raise ValueError("在庫は0以上にしてください")

except ValueError as e:
    print(f"入力エラー：{e}")

else:
    print(f"商品名：{product}")
    print(f"商品在庫：{stock}個")

finally:
    print("処理を終了します")