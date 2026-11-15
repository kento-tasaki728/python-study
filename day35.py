while True:
    try:
      number = int(input("購入数量を入力してください："))
    except ValueError:
        print("数字を入力してください")
        continue
    if number <= 0:
        print("1以上の数字を入力してください")
        continue
    print(f"購入数量： {number} 個")
    break