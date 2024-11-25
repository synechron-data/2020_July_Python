# def greetings(msg, name):
#     return msg + ", "+name


# print(greetings("Good Morning", "Dip"))
# print(greetings("Good Morning", "Gyanranjan"))
# print(greetings("Good Morning", "Kirti"))


# def Converter(toUnit, factor, offset, inp):
#     return (str((offset+inp)*factor)+" "+toUnit)


# print(Converter('km', 1.6, 0, 10))
# print(Converter('km', 1.6, 0, 100))
# print(Converter('km', 1.6, 0, 240))
# print(Converter('km', 1.6, 0, 890))

# --------------------------------------------------------- Currying

# def greetings(msg):
#     def greet(name):
#         return msg + ", "+name
#     return greet

# mGreet = greetings("Good Morning")

# print(mGreet("Dip"))
# print(mGreet("Gyanranjan"))
# print(mGreet("Kirti"))


def getConverter(toUnit, factor, offset):
    def converter(inp):
        return (str((offset+inp)*factor)+" "+toUnit)
    return converter


milesToKm = getConverter('km', 1.6, 0)

print(milesToKm(10))
print(milesToKm(100))
print(milesToKm(240))
print(milesToKm(890))

usdToInr = getConverter('INR', 75, 0)

print(usdToInr(10))
print(usdToInr(100))
print(usdToInr(240))
print(usdToInr(890))
