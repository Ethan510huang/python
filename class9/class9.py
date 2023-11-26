# '1,2,3' .split(',')
# '2020/1/1' .split('/')
# img = ['1', '2', '3']
# '-'.join(img)

# x = "2023/10/20".split("/")
# print("-".join(x))
# x = ['1', '2', '3']
# x.append(4)
# print(x)
# x = ['1', '2', '3']
# x.insert(0,'a')
# print(x)
order_list = []
while True:
    print("歡迎使用點餐機!")
    print("1. 新增餐點到點餐清單")
    print("2. 從點餐清單中移除特定餐點")
    print("3. 在指定位置加入餐點")
    print("4. 計算點餐清單中某餐點的數量")
    print("5. 取消點餐清單中的最後一向餐點")
    print("6. 取消點餐清單中特定位置的餐點")
    print("7. 顯示小到大排序的出餐清單")
    print("8. 顯示從大到小排序的出餐清單")
    print("9. 反轉點餐清單得出餐順序")
    print("10. 查詢餐點在點餐清單中的位置")
    print("11. leave")
    option = input("歡迎使用點餐機!請選擇你想要的功能(輸入數字):")
    if option == "1":
        x = input("請輸入想新增的餐點:")
        order_list.append(x)
    elif option == "2":
        y = input("請輸入想取消的餐點:")
        if y in order_list:
            order_list.remove(y)
            print("已移除餐點!")
        else:
            print(
                "error error error error error error error error error error error error error error"
            )
    elif option == "3":
        z = int(input("請輸入位置:"))
        r = input("請輸入想插入的餐點:")
        order_list.insert(z, r)
    elif option == "11":
        print("謝謝使用點餐機!")
        break
    else:
        print("請輸入有效的選項!")
        continue
    print("目前的點餐清單:" + str(order_list))
