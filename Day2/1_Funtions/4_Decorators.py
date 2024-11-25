# def hello():
#     print("Hello World!")

# def hello_decorator(func):
#     def extentedLogic():
#         print("Some extra implementation added");
#         func()
#     return extentedLogic

# # hello()
# # extended_hello = hello_decorator(hello)
# # extended_hello()

# hello = hello_decorator(hello)
# hello()

# ------------------------------------------------------

# def hello_decorator(func):
#     def extentedLogic():
#         print("Some extra implementation added")
#         func()
#     return extentedLogic

# @hello_decorator
# def hello():
#     print("Hello World!")


# hello()

# ------------------------------------------------------
# Once back from the break
# Create a decorator to log the following when function is called
# print("{} called with arguments {}".format(add.__name__, (a, b)))

def log(func):
    def logger(*args, **kwargs):
        print("{} called with arguments {}".format(func.__name__, args or kwargs))
        return func(*args, **kwargs)
    return logger

@log
def add(a, b):
    return a+b

@log
def sub(a, b, c):
    return a-b-c


print(add(2, 3))
print(add(a=20, b=30))
print(sub(20, 10, 5))
