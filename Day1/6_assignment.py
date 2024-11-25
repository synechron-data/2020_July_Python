a = [2, 4, 3, 1, 1, 4]

# r = set(a)
# print(r)

# Result - {2: 1, 4: 2, 3: 1, 1: 2}

# r = {}
# print(type(r))

# --------------------------------
# for i in a:
#     if i in r:
#         r[i] = r[i]+1
#     else:
#         r[i] = 1

# print(r)

# ----------------------------------
# r = {}
# for i in a:
#     r[i] = a.count(i)

# print(r)

# ---------------------------
# r = dict((i, a.count(i)) for i in a)
# print(r)

# ---------------------------
from collections import Counter
r = Counter(a)
print(r)