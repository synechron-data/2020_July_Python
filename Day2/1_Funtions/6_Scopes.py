# L - Local
# E - Enclosing
# G - Global
# B - Built In

# def len(inp):
#     print('my len called....')
#     return 0

# print(len("Hello World"))

# ---------------------------------------
# x = 10

# # def show():
# #     x = 1000
# #     print("Inside, x:", x)

# def show():
#     global x
#     x = x + 1000
#     print("Inside, x:", x)

# show()
# print("Outside, x:", x)

# -----------------------------------------
# x = 10

# def show():
#     x = 0
#     def check():
#         # global x
#         nonlocal x
#         x = 1000
#         print("Inside Check, x:", x)

#     check()
#     print("Inside Show, x:", x)

# show()
# print("Global, x:", x)

# -----------------------------------------
i = "Hello"
print("Before, i:", i)

# for i in range(5):
#     print("Inside Loop, i: ", i)

def iterate():
    for i in range(5):
        print("Inside Loop, i: ", i)

iterate()

print("After, i:", i)

# --------------------------------------------
# following constructs create scope:

# module
# class
# function (incl. lamda)
# generator expressions
# comprehensions