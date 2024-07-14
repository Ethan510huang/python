def hello(name, age=10, grade=5):
    print("Hello", name, "you are", age, "years old and in grade", grade)


hello("Alice")
hello("Bob", 12)
hello("Charlie", 11, 6)


import random

print(random.randint(1, 10))  # 一定要設定開始與結束, 範圍會包含結束的數字
print(random.randrange(10))  # 0~9
print(random.randrange(10, 20))  # 10~19
print(random.randrange(10, 20, 2))  # 10~19, 間隔2
a = "abcdefghij"
print(a[1:3])  # bc
print(a[1:3:2])  # b
print(a[::2])  # acegi


from random import randint  # 只引入randint, 不用再打random.

try:  # try必須要有最少一個except, 也可以有多個
    a = int(input("Enter a number: "))
    b = randint(1, 10)
    print("You entered", a)
    print("Random number is", b)
    print("Sum is", a + b)
except ValueError:  # except至少要有一個, 也可以有多個
    print("Please enter a number")
except Exception as e:
    print("Error:", e)
else:  # 可有可無, 但如果有的話, 必須要有except, else只能有一個
    print("No error")
finally:  # 可有可無, 但如果有的話, 必須要有except, finally只能有一個
    print("End of program")

# 檔案讀寫模式
# r: 讀取, 檔案必須存在, 檔案不存在則發生錯誤
# r+: 讀取與寫入, 檔案必須存在, 檔案不存在則發生錯誤
# w: 寫入, 檔案不存在則建立, 檔案存在則清空
# w+: 讀取與寫入, 檔案不存在則建立, 檔案存在則清空
# a: 寫入, 檔案不存在則建立, 檔案存在則接續寫入
# a+: 讀取與寫入, 檔案不存在則建立, 檔案存在則接續寫入


# math module
# math.fabs(x): 取絕對值, 把有正負號的數字轉成正數
# math.ceil(x): 無條件進位到最接近的整數
# math.floor(x): 無條件捨去到最接近的整數
# math.fmod(x, y): 小數取餘數, 會回傳浮點數
# math.frexp(x): 回傳一個tuple, 第一個是小數, 第二個是次方，例如: math.frexp(10) 回傳 (0.625, -1)
# tuple長這樣: (0.625, -1), 資料看起來像list, 但是tuple是不可變的


# assertis(x, y): x is y, 如果x和y是同一個物件, 則回傳True, 否則回傳False
# assertin(x, y): x in y, 如果x是y的元素, 則回傳True, 否則回傳False
# assertequal(x, y): x == y, 如果x等於y, 則回傳True, 否則回傳False
# assertisinstance(x, y): isinstance(x, y), 如果x是y的實例, 則回傳True, 否則回傳False
