# ------------------------------------ List
# data = [1, 2, 3, 4, 5, "Pune"]
# print(data)
# print(type(data))

# print(data[0])
# print(data[1:3])

# print(id(data))
# data = [1,2]
# # data[0] = "Test"
# print(id(data))

# # ------------------------------------ Tuple

# data = (1, 2, 3, 4, 5, "Pune")
# print(data)
# print(type(data))

# # print(id(data))
# # data[0] = "Test"
# # print(id(data))

# for a in data:
#     print(a)

# print("Check")

# ------------------------------------ Set

# data = {1, 2, 3, 4, 5, "Pune", 1, 2, 3, 4, 5, 6, 7}
# print(data)
# print(type(data))

# for a in data:
#     print(a)

# ------------------------------------ Dict
# data = {
#     "Manish":"123456789",
#     "Rohit":"111111111",
#     "Ramakant":"222222222",
#     "Manish":"333333333",
# }
# # print(data)
# # print(type(data))

# for a in data:
#     print(a)

# -------------------------------------------- Range
# xRange = range(0, 20)
# print(xRange)
# print(type(xRange))

# for a in xRange:
#     print(a)

# data = list(range(0, 20))
# data = list(range(6))
# print(data)
# print(type(data))

numList = []

n = int(input("Enter number of items: "))

for i in range(0, n):
    inp = int(input())
    numList.append(inp)

# for i in numList:
#     print(i, end=" ")

print(numList)
print(numList + [45, 67])
print(numList * 3)

print(10 in numList)
print(10 not in numList)

print(numList[1])
print(numList[1:3])
print(numList[1:5:2])
