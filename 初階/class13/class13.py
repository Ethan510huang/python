# ans = eval("1+2")
# print(ans)


# ans = eval("a+b")
# print(ans)


# x = input("請輸入一個算數")
# ans = eval(x)
# print(ans)


# import os

# filepath = "class13/hw13.py"
# if os.path.isfile(filepath):
#     print("here")
# else:
#     print("no here")


# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()


# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)


# filename = "test.txt"
# mode = "w"
# myfile = open(filename, mode)
# myfile.write("hi\n")
# myfile.write("how old are you?")
# myfile.close()
# filename = "test.txt"
# mode = "w"
# myfile = open(filename, mode)
# myfile.write("hi\n")
# myfile.write("i am 12345657890876543789 years old")
# myfile.close()


# path = "course/class13/test.txt"
# f = open(path, 'r')
# total = f.read()
# print(total)
# f.close


path = "course/class13/test.txt"
f = open(path, "r")
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close


path = "course/class13/test.txt"
f = open(path, "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close
