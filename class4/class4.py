# password = input("請輸入密碼:")
# if password == "Taipei 1o1":
#     print("歡迎光臨")
# elif password == "minecraft":
#     print("歡迎不光臨")
# elif password == "tr. little名":
#     print("you are so bad!")
# else:
#     print("haha!密碼這麼簡單也能錯!so bad!")


# number = int(input("enter a number:"))
# if number % 2 == 0:
#     print("this is an even number")
# else:
#     print("this is an odd number")

import turtle

# for IDK in range(4):
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(50)

turtle.color("blue")
turtle.shape("turtle")
turtle.penup()
turtle.stamp()
turtle.speed(0.1)
for IDK in range(4, 1000000, 5):
    turtle.right(50)
    turtle.forward(IDK)
    turtle.stamp()


turtle.done()
