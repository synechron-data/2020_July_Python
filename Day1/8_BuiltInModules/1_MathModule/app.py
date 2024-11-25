# import math
# print(math)

# result = math.sqrt(81)
# print(result)

# print(math.factorial(5))
# print(math.factorial(6))

# n = 5
# k = 3
# r = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
# print(r)

# -------------------------------------------------------
# from math import factorial, sqrt

# n = 5
# k = 3
# r = factorial(n) / (factorial(k)*factorial(n-k))
# print(r)

# result = sqrt(81)
# print(result)

# -------------------------------------------------------
from math import factorial as fac, sqrt as srt

n = 5
k = 3
r = fac(n) / (fac(k)*fac(n-k))
print(r)

result = srt(81)
print(result)

