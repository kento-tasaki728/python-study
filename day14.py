numbers = []

while True:
    number = input("数字を入力：")

    if number == "0":
        break

    numbers.append(int(number))

print("登録した数字：", (numbers))
print("登録件数：", len(numbers))      