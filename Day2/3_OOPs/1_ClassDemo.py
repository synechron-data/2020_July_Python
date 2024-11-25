# class Employee:
#     pass

# print(Employee)
# e = Employee()
# print(e)
# print(type(e))

# i = int(10)
# print(i)
# print(type(i))


class Employee:
    def __init__(self, id=0, name="NA", desig="NA", sal=0):
        self._id = id
        self._name = name
        self._desig = desig
        self._sal = sal

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getDesig(self):
        return self._desig

    def getSal(self):
        return self._sal

    def setSal(self, sal):
        if sal < 10000:
            raise ValueError("I will not work less than this amount")
        self._sal = sal


# e = Employee()
e = Employee(1, "Manish", "Trainer", 12345)
print("Id: ", e.getId())
print("Name: ", e.getName())
print("Designation: ", e.getDesig())
print("Salary: ", e.getSal())

e.setSal(10000)
print("Salary: ", e.getSal())

e.setSal(-10000)
print("Salary: ", e.getSal())