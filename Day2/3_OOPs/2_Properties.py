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
    
#     Salary = property(getSal, setSal)
#     # Salary = property(getSal)

# e = Employee(1, "Manish", "Trainer", 12345)
# print("Id: ", e.getId())
# print("Name: ", e.getName())
# print("Designation: ", e.getDesig())
# print("Salary: ", e.Salary)

# e.Salary = 10000
# print("Salary: ", e.Salary)

# # --------------------------------------------------------------- Using Decorator
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

#     @property
#     def Salary(self):
#         return self._sal

#     @Salary.setter
#     def Salary(self, sal):
#         if sal < 10000:
#             raise ValueError("I will not work less than this amount")
#         self._sal = sal
    
# e = Employee(1, "Manish", "Trainer", 12345)
# print("Id: ", e.getId())
# print("Name: ", e.getName())
# print("Designation: ", e.getDesig())
# print("Salary: ", e.Salary)

# e.Salary = 10000
# print("Salary: ", e.Salary)

# --------------------------------------------------------------- Using Decorator
class Employee:
    def __init__(self, id=0, name="NA", desig="NA", sal=0):
        self._id = id
        self._name = name
        self._desig = desig
        self._sal = sal

    @property
    def Id(self):
        return self._id

    @Id.setter
    def Id(self, value):
        self._id = value

    @property
    def Name(self):
        return self._name

    @property
    def Designation(self):
        return self._desig

    @property
    def Salary(self):
        return self._sal

    @Salary.setter
    def Salary(self, sal):
        if sal < 10000:
            raise ValueError("I will not work less than this amount")
        self._sal = sal
    
e = Employee(1, "Manish", "Trainer", 12345)
print("Id: ", e.Id)
print("Name: ", e.Name)
print("Designation: ", e.Designation)
print("Salary: ", e.Salary)

e.Salary = 10000
print("Salary: ", e.Salary)