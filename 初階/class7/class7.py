# import random

# print(random.randrange(3))

# print(random.randint(1, 10))

import random

# ans = random.randint(1, 100)
# # print(ans)
# min = 0
# max = 100
# while True:
#     n = int(input("請猜一個" + str(min) + "~" + str(max) + "之間的數字:"))
#     if n < ans:
#         print("在大一點")
#     elif n > ans:
#         print("在小一點")
#     else:
#         print("恭喜猜中了!")
#         break
# 新增list
# L = []
# print(L)
# L = [1, 2, 3]
# print(L)
# L = [1, 2, 3, "Hello", "World"]
# print(L)
# L = [1, 2, 3, "Hello", "World", [4, 5, 6]]
# print(L)
# x = ["明", "小明", "小小小小小明", "little ming", "littlelittlelittlelittlelittelelittleming"]
# print(x[3:6])


# l = ["a", "b", "c"]
# for index in range(len(l)):
#     print(l[index])

# l = ["a", "b", "c"]
# for element in l:
#     print(element)

juices_list = ["蘋果汁", "Cola", "柳橙汁", "葡萄汁", "系統關閉"]

while True:
    for i in range(len(juices_list)):
        print(str(i + 1) + ". " + str(juices_list[i]))
    try:
        select = int(input("請輸入編號:"))
    except:
        print("請重新輸入!")
        continue

    if select == len(juices_list):
        print("close")
        break
    elif select < len(juices_list):
        print("你點的商品是" + juices_list[select - 1])
    else:
        print("查無此商品請重新輸入!!!歡迎不光臨")
