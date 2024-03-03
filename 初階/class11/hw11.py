grade = {}
# {"ch":94, "en":100}
while True:
    print(grade)
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    select = input("請輸入功能編號:")
    if select == "1":
        subject = input("請輸入科目名稱:")
        while True:
            try:
                score = int(input("請輸入成績:"))
            except:
                print("error")
                continue
            else:
                grade[subject] = score
                break
    elif select == "2":
        subject = input("請輸入要刪除的科目名稱:")
        if subject in grade:
            grade.pop(subject, "")
            print("success")
        else:
            print("error")
    elif select == "3":
        print(sum(grade.values()) / len(grade))
        break
    else:
        print("查無此功能請重新輸入")
