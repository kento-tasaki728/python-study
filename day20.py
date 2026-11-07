products = []

while True:
    print("===== 商品管理メニュー =====")
    print("1. 商品登録")
    print("2. 商品一覧表示")
    print("3. 終了")

    choice = input("選択してください（1-3）：")

    if choice == "1":
        name = input("商品名：")
        price = int(input("価格："))
        stock = int(input("在庫数："))
        new_product = dict(name=name, price=price, stock=stock)
        products.append(new_product)
        print(f"{name}を登録しました。")
    elif choice == "2":
        print("【商品一覧】")
        if len(products) == 0:
            print("登録されている商品はありません。")
        else:
            for product in products:
                print(f"商品名：{product['name']}  価格：{product['price']} 在庫数：{product['stock']}")
        print(f"登録商品数：{len(products)}")  # 商品の数を表示
    elif choice == "3":
        print("終了します。")
        break
    else:
        print("無効な選択です。もう一度入力してください。")
