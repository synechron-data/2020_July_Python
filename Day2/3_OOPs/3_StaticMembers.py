# class Example:
#     name = "Manish"

#     @staticmethod
#     def testMethod():
#         print("Name is: ", Example.name)

# e = Example()
# Example.testMethod()

# -------------------------------------------------
class Example:
    name = "Manish"

    @staticmethod
    def testMethod1():
        print("Name is: ", Example.name)

    @classmethod
    def testMethod2(c):
        print("Name is: ", c.name)

e = Example()
e.testMethod2()
Example.testMethod2()

# @staticmethod function is nothing more than a function defined inside a class. 
# It is callable without instantiating the class first. It’s definition is immutable via inheritance.

# @classmethod function also callable without instantiating the class, 
# but its definition follows Sub class, not Parent class, via inheritance