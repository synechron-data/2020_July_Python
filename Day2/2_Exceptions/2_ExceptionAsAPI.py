# def sqrt(x):
#     guess = x
#     i = 0
#     while guess * guess != x and i < 20:
#         guess = (guess + x/guess)/2.0
#         i += 1
#     return guess

# print(sqrt(9))
# print(sqrt(2))
# print(sqrt(-1))

# -------------------------------------------------


# def sqrt(x):
#     if(x < 0):
#         raise ValueError("Cannot use negative number {}".format(x))

#     guess = x
#     i = 0
#     while guess * guess != x and i < 20:
#         guess = (guess + x/guess)/2.0
#         i += 1
#     return guess

# def sqrt(x):
#     guess = x
#     i = 0
#     try:
#         while guess * guess != x and i < 20:
#             guess = (guess + x/guess)/2.0
#             i += 1
#     except ZeroDivisionError:
#         # Log the actual Exception
#         raise ValueError("Cannot use negative number {}".format(x))
#     return guess


# print(sqrt(9))
# print(sqrt(2))
# try:
#     print(sqrt(-1))
# except ValueError as e:
#     print(e)

# -------------------------------------------------------------

def sqrt(x):
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        # Log the actual Exception
        raise ValueError("Cannot use negative number {}".format(x))
    return guess


# def call():
#     print(sqrt(9))
#     print(sqrt(2))
#     try:
#         print(sqrt(-1))
#     except ValueError as e:
#         print(e)

def catchException(func):
    def exceptionHandler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
        finally:
            print("Hello from catchException Decorator")
    return exceptionHandler


@catchException
def call():
    print(sqrt(9))
    print(sqrt(2))
    print(sqrt(-1))


call()

# Donot apply decorator on call, apply it on function definition
# @catchException
# print(sqrt(-1))
