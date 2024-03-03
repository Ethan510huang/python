import turtle

# turtle.pensize(5)
# turtle.pencolor("yellow")
# turtle.fillcolor("yellow")
# turtle.begin_fill()
# turtle.end_fill()
# for IDK in range(5):
#     turtle.forward(50)
#     turtle.right(144 )
# turtle.done()


# x = int(input("請輸入一個數字"))
# total = 0
# for x in range(x + 1):
#     print(x)
#     total = total + x
# print(total)


# for i in range(1, 10):
#     for j in range(1, 10):
#         print(str(i) + "x" + str(j) + "=" + str(i * j))


# i = 0
# while i < 5:
#     print(i)
#     i = i + 1


# a += 2
# a -= 2
# a *= 2
# a /= 2
# a //= 2
# a %= 2
# a **= 0.5

password = ""
while password != "Taipei 1o1":
    password = input("請輸入密碼:")
    if password == "Taipei 1o1":
        print("歡迎光臨")
    else:
        print("密碼錯誤，請重新輸入!!!")
