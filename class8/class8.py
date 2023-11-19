# weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
# x = int(input("請輸入修改天氣1~7:"))
# if x < 8:
#     print("你要修改的天氣是星期" + str(x))
#     y = input("請輸入天氣:")
#     weather[x - 1] = y
#     print(weather)
# elif x > 7:
#     print("error")
# elif x < 1:
#     print("error")
# weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
# print(weather)
# while True:
#     try:
#         ans = int(input("請輸入要改的星期(1~7):"))
#     except:
#         print("請輸入數字")
#         continue

#     if ans > len(weather) or ans < 1:
#         print("error")
#     else:
#         print("你要修改得星期是" + str(ans))
#         print("原本天氣是" + weather[ans - 1])
#         new_weather = input("請輸入新天氣:")
#         weather[ans - 1] = new_weather
#         print("修改後的天氣是" + weather[ans - 1])
#     print(weather)
#     break
# L = ['A', 'B', 'C']
# A = L.copy()
# A[0] = L
# print(A, L)


# X = ["MILK", "BREAD"]
# Y = ["APPLE", "BANANA"]
# # Z = [1, 2] + ["B", "C"]
# print(X + Y)
# [1,2] *2

X = ["火龍果", "哈密瓜", "百香果", "橘子", "蘋果", "香蕉", "梨", "李", "桃"]
print("最長的是" + max(X))
print("最短的是" + min(X))

list("abc")
list([4, 5, 6])
list(range(3))
