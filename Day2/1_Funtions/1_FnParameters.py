# non-default argument follows default argument
# def add(x=0, y=0):
#     return x+y


# print(add(2, 3))
# print(add(2))
# print(add())

# non-keyworded, variable-length argument list
# def addAll(*numbers):
#     print(numbers)
#     print(type(numbers))
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum


# # print(addAll())
# # print(addAll(1))
# # print(addAll(1, 2))
# # print(addAll(1, 2, 3, 4, 5))
# # print(addAll(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(addAll(*[1, 2, 3, 4, 5, 6, 7, 8, 9]))

# keyworded, variable-length argument list
# def printData(id, name = "Abhijeet", city = "Mumbai"):
#     print(id)
#     print(name)
#     print(city)


# # printData(1, "Manish", "Pune")
# # printData(id=1, name="Manish", city="Pune")
# # printData(city="Pune", name="Manish", id=1)

# printData(1, "Pune")
# printData(1, city = "Pune")

# def printData(**kwargs):
#     print(kwargs)
#     print(type(kwargs))


# printData(1, "Manish", "Pune") #printData() takes 0 positional arguments but 3 were given
# printData(id=1, name="Manish", city="Pune")

# myEmployee = {"id": 1, "name": "Manish", "city": "Pune"}
# print(myEmployee)
# print(type(myEmployee))

# printData(myEmployee)
# printData(**myEmployee)

# print(myEmployee)
# print(*myEmployee)
# -------------------------------------------------------
# import copy

# data1 = [10, 20, 30, 40, 50]
# # data2 = data1
# data2 = data1[::]

# # Shallow Copy
# # data2 = copy.copy(data1)

# # Deep Copy
# # data2 = copy.deepcopy(data1)

# data2[0] = 1000

# print("data1: ", data1)
# print("data2: ", data2)

# ------------------------------------------------- Destructuring

# data1 = [10, 20, 30, 40, 50]

# # a = data1[0]
# # b = data1[1]

# # a, b, *rest = data1
# # a, _, _, _, b = data1
# # a, b, _, _, _ = data1
# # a, *rest, b = data1

# *rest, a, b = data1

# print(a)
# print(b)
# print(rest)

# ---------------------------------------------------- Query
# def printData(arg1, *numbers, **kwargs):
#     print(arg1)
#     print(numbers)
#     print(kwargs)


# printData(*[10, 20, 30], **{"one": 1, "two": 2})

# printData(10, 20, 30, "one": 1, "two": 2)


# ---------------------------------------------------- Query
# def printData(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)


# printData(10, 20, 30)
# printData(arg1=100, arg2=200, arg3=300)

# args = (1000, 2000, 3000)
# printData(*args)

# kwargs = {"arg1": 10000, "arg2": 20000, "arg3": 30000}
# printData(*kwargs)

# kwargs = {"arg1": 10000, "arg2": 20000, "arg3": 30000}
# printData(**kwargs)

def printData(arg1, *arg2, **kwargs3):
    print(arg1)
    print(arg2)
    print(kwargs3)


printData(10)
printData(10, "hello", "hi")
printData(10, "hello", "hi", name="Manish", city="Pune")
