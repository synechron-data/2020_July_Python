# class Employee:
#     def __init__(self, id=0, name="NA", desig="NA", sal=0):
#         self._id = id
#         self._name = name
#         self._desig = desig
#         self._sal = sal

#     def getId(self):
#         return self._id

#     def getName(self):
#         return self._name

#     def getDesig(self):
#         return self._desig

#     def getSal(self):
#         return self._sal

#     def setSal(self, sal):
#         if sal < 10000:
#             raise ValueError("I will not work less than this amount")
#         self._sal = sal


# class Manager(Employee):
#     def __init__(self, id=0, name="NA", desig="NA", sal=0, location="Pune"):
#         # Employee.__init__(self, id, name, desig, sal)
#         super().__init__(id, name, desig, sal)
#         self._location = location

#     def getLocation(self):
#         return self._location

#     def setSal(self, sal):
#         if sal < 100000:
#             raise ValueError("Manager Impl")
#         self._sal = sal


# e = Manager(1, "Manish", "Trainer", 12345)
# print(type(e))
# print("Id: ", e.getId())
# print("Name: ", e.getName())
# print("Designation: ", e.getDesig())
# print("Salary: ", e.getSal())
# print("Location: ", e.getLocation())

# e.setSal(10000)
# print("Salary: ", e.getSal())

# -------------------------------------------- Multiple

class A:
    def __init__(self):
        print("Class A init")

    def method(self):
        print("Class A")


class B:
    def __init__(self):
        print("Class B init")

    def method(self):
        print("Class B")

# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("Class C init")

#     # def method(self):
#     #     print("Class C")


class C(B,A):
    def __init__(self):
        super().__init__()
        print("Class C init")

    # def method(self):
    #     print("Class C")


obj = C()
obj.method()
