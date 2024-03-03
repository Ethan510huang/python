def add_expense(date, amount):
    if date not in expenses:
        expenses[date] = []
    expenses[date].append(amount)


def query_expenses(date):
    if date not in expenses:
        return 0
    return sum(expenses[date])


def total_expenses():
    total = 0
    for value in expenses.values():
        total += sum(value)
    return total


def save_file():
    filename = "memeory.txt"
    mode = "w"
    my_file = open(filename, mode)
    for date, list in expenses.items():
        for money in list:
            print(f"{date},{money}")
            my_file.write(f"{date},{money}\n")
    my_file.close()


expenses = {}

while True:
    print("1.新增支出紀錄:")
    print("2.查詢特定日期的支出總和")
    print("3. 輸出所有記錄的總和")
    print("4. 離開系統")
    print("5. 存檔")
    select = input("請輸入功能編號")
    if select == "1":
        date = input("請輸入日期:")
        amount = int(input("請輸入金額:"))
        add_expense(date, amount)
    elif select == "2":
        date = input("請輸入日期:")
        print(f"{date}的支出總和為{query_expenses(date)}")
    elif select == "3":
        print(f"所有記錄的總和為{total_expenses()}")
    elif select == "4":
        break
    elif select == "5":
        save_file()
    else:
        print("查無此功能請重新輸入")
