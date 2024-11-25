# Defaultdict
# from collections import defaultdict
# numbers = defaultdict(int)
# numbers = dict()

# numbers['one'] = 1
# numbers['two'] = 2
# numbers['three'] = 3

# print(numbers)
# print(numbers['five'])
# print(type(numbers))

# ----------------------------- Counter
# from collections import Counter
# list = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 1, 2, 2]
# r = Counter(list)
# print(r)

# ----------------------------- Named Tuple
# Employee = ("Manish", "Sharma", 38)
# print(type(Employee))
# print(Employee[0])
# print(Employee[1])
# print(Employee[2])

# from collections import namedtuple
# Employee = namedtuple('MyEmployee', 'fname, lname, age')
# e1 = Employee("Manish", "Sharma", 38)
# print(e1)
# print(type(e1))
# print(e1.fname)
# print(e1.lname)
# print(e1.age)

# ------------------------------------------ Itertools
# from itertools import groupby
# arr = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
# # r = [(i, len(list(c))) for i,c in groupby(arr)]
# r = [(i, len(list(c))) for i,c in groupby(sorted(arr))]
# print(r)

# from itertools import accumulate
# arr = [1, 2, 3, 4, 5]
# result = accumulate(arr)

# for r in result:
#     print(r)

from itertools import accumulate
from operator import mul

arr = [1, 2, 3, 4, 5]
result = accumulate(arr, mul)

for r in result:
    print(r)
