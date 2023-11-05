# a = input("請輸入你的年齡:")
# a = int(a) + 10
# print("你十年後的年齡是%d歲" % (a))  # %d是整數  %s是字串  %f是小數
# 字串結束號%()裡面放想放的內容

try:
    num = int(input("請輸入數字:"))  # 要轉換成數字
except:
    pass  # 當錯誤發生時執行的程式
else:
    total = num + 999999999999  # 將數字num加999999999999並存到total
    print(total)  # 顯示total
