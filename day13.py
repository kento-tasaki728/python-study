total = 0

while True:
    number = input("数字を入力してください：")
    
    x = int(number)
    
    if number == "0":
      print("プログラムを終了します")
      break
    
    total += x
print(total)