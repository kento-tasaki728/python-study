products = []

while True:
    print("===== 商品管理メニュー =====")
    print("1. 商品登録")
    print("2. 商品一覧表示")
    print("3. 商品検索")
    print("4.在庫数変更")
    print("5. 終了")

    choice = input("選択してください（1-5）：")

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
        print("商品検索を開始します。")
        search_name = input("検索する商品名：")
        found = False
        for product in products:
            if product['name'] == search_name:
                print(f"商品名：{product['name']}  価格：{product['price']} 在庫数：{product['stock']}")
                found = True
                break
            if not found:
              print("指定された商品は見つかりませんでした。")
    elif choice == "4":
        change_name = input("変更する商品名：")
        found = False
        for product in products:
            if product['name'] == change_name:
              print(f"現在の在庫数：{product['stock']}")
              new_stock = int(input("新しい在庫数："))
              product['stock'] = new_stock
              print(f"{change_name}の在庫数を{new_stock}に変更しました。")
              found = True
              break
        if not found:
            print("指定された商品は見つかりませんでした。")
    elif choice == "5":
        print("終了します。")
        break
    else:
        print("無効な選択です。もう一度入力してください。")
