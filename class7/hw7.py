import random

ans = random.randint(1, 100)
# print(ans)
min = 0
max = 100
while True:
    n = int(input("請猜一個" + str(min) + "~" + str(max) + "之間的數字:"))
    if n < ans:
        print("在大一點")
        if min < n < max:
            min = n
    elif n > ans:
        print("在小一點")
        if min < n < max:
            max = n
    else:
        print("恭喜猜中了!")
        break
