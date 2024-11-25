def add(a, b):
    if(isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return a+b

    raise ValueError("Parameters should be numeric")


try:
    print(add(2, 3))
    print(add("a", "b"))
except Exception as e:
    print(e)