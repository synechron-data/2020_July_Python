# def convert(s):
#     x = int(s)
#     return x

# print(convert("10"))
# # print(convert("ab"))
# print("I am the last line")


# def convert(s):
#     try:
#         x = int(s)
#         print("Conversion Success")
#     except ValueError:
#         x = -1
#         print("Conversion Failed")
#     except TypeError:
#         x = -1
#         print("Conversion Failed")
#     return x

# def convert(s):
#     try:
#         x = int(s)
#         print("Conversion Success")
#     except (ValueError, TypeError):
#         x = -1
#         print("Conversion Failed")
#     return x

# def convert(s):
#     x = -1
#     try:
#         x = int(s)
#         print("Conversion Success")
#     except (ValueError, TypeError) as e:
#         print(str(e))
#     return x

# def convert(s):
#     x = -1
#     try:
#         x = int(s)
#         print("Conversion Success")
#     except Exception as e:
#         print(str(e))
#     return x

def convert(s):
    x = -1
    try:
        x = int(s)
        print("Conversion Success")
    except:
        print("Error")
    return x

print(convert("10"))
print(convert("ab"))
print(convert(list()))
print(convert("-1"))
print("I am the last line")
