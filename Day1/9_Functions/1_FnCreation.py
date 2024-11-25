# def hello():
#     pass


# def hello():
#     print('hello world!')


# # hello()
# print(hello)
# print(type(hello))

# def add(x, y):
#     return x+y


# print(add(2, 3))
# print(add(2, 3, 5))     #TypeError: add() takes 2 positional arguments but 3 were given
# print(add(2))   # TypeError: add() missing 1 required positional argument: 'y'


def addAll(numbers):
    print(type(numbers))
    sum = 0
    for n in numbers:
        sum += n
    return sum


print(addAll(2))
print(addAll([2, 3, 4]))
print(addAll(["2", "3"]))
print(addAll({1: 23}))