# def hello(name):
#     print("hello" + str(name))


# hello("little ming")
# def my_min(a, b):
#     if a < b:
#         return a
#     else:
#         return b
# x = my_min(1, 2)
# print("my_min:" + str(x))
# def my_func(a, b):
#     print(a, b)
# my_func(1, 2)
# print(a) a在外面沒有用
# length = 5
# area = 3.14 * 10**2
# def caculatesquarearea():
#     global area
#     area = length**2
# caculatesquarearea()
# print("面積是", area)
# import random
# def dicetime(x: int):
#     """擲骰子的指令，X代表次數(整數)"""
#     dice = []
#     for i in range(x):
#         dice.append(random.randint(1, 6))
#     return dice


# n = int(input("丟骰子的次數:"))
# print(dicetime(n))
def my_func(a, b, c=0, d=0):
    print("a = ", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)


my_func(1, 2)
my_func(1, 2, 3)
my_func(1, 2, 3, 4)
my_func(1, 2, d=4)
my_func(d=4, a=1, b=2)
