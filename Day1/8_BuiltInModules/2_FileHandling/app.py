# r, w, a, x / rt, wt, at / rb, wb, ab / +

import json
# fo = open("test1.txt", "wb+")

# print("Name of the file", fo.name)
# print("Status of the file", fo.closed)
# print("Mode of the file", fo.mode)

# input = "This is just an example of FIle Write.\nUsing Python"
# binp = bytearray(input, "utf-8")
# fo.write(binp)

# position = fo.tell()
# print("Current Cursor position", position)

# position = fo.seek(0)
# print("Current Cursor position", position)

# str = fo.read()
# str = fo.read(10)
# str = fo.readline()
# str = fo.readlines()

# print(str)

# while True:
#     s = fo.readline()
#     if not s:
#         break;
#     print(s)

# print(fo.readlines())
# print(type(fo.readlines()))

# for line in fo.readlines():
#     print(line)
#     print(type(line))

# fo.close()
# print("Name of the file", fo.name)
# print("Status of the file", fo.closed)
# print("Mode of the file", fo.mode)


employee = {
    "name": "Manish",
    "age": 38,
    "city": "Pune"
}

print(employee)
print(type(employee))

y = json.dumps(employee)
print(y)
print(type(y))

# fo = open('data.json', "w")
# json.dump(employee, fo)
# fo.close()

fo = open('data.json', "r")
data = json.load(fo)
print(data)
print(type(data))

