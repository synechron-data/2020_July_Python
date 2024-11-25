# fileRead = open("python.png", "rb")
# fileWrite = open("python-copy.png", "wb")

# while True:
#     byte = fileRead.read(1)
#     if not byte:
#         break
#     fileWrite.write(byte)

# fileRead.close()

# fileWrite = open("python1-copy.png", "wb")

# with open("python.png", "rb") as fileRead: 
#     while True:
#         byte = fileRead.read(1)
#         if not byte:
#             break
#         fileWrite.write(byte)

# print("File Copied....")

import shutil
shutil.copy("python.png", "python-copy.png")