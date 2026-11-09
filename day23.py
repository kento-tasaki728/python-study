def show_menu():
    print("===== 商品管理メニュー =====")
    print("1. 商品登録")
    print("2. 商品一覧表示")
    print("3. 商品検索")
    print("4.在庫数変更")
    print("5. 終了")
    
while True:
    show_menu()
    choice = input("選択してください（1-5）：")
    if choice == "5":
        print("終了します。")
        break