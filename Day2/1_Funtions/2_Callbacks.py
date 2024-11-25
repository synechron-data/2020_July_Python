# def addAll(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum

# print(addAll(*[1, 2, 3, 4, 5, 6, 7]))

# ---------------------------------------- Fn as parameter to another Fn
# def addAll(numbers, callback):
#     sum = 0
#     for n in numbers:
#         sum += n
#     callback(sum)


# def printResult(result):
#     print("Result is: ", result)


# addAll([1, 2, 3, 4, 5, 6, 7], printResult)

# ------------------------------------------------

# numArr = [1, 2, 3, 4, 5]


# # def processItem(item):
# #     return item*2

# # r = []
# # for item in numArr:
# #     r.append(processItem(item))

# # r = map(processItem, numArr)
# r = map(lambda item: item*2, numArr)

# print(list(r))

# ---------------------------------------------------- Find all numbers divisible by 2

numArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# r = []
# for item in numArr:
#     if item % 2 == 0:
#         r.append(item)

r = filter(lambda item: item % 2 == 0, numArr)
print(list(r))
