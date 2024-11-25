import collections
import csv

# myData = [
#     ["fname", "lname", "city"],
#     ["Manish", "Sharma", "Pune"],
#     ["Abhijeet", "Gole", "Pune"]
# ]

# myFile = open('test.csv', 'w', newline='')

# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)

# print("CSV File Created....")

# ------------------------------------------ Read

# with open('test.csv') as file:
#     reader = csv.reader(file, delimiter=",")

#     for row in reader:
#         print(row)

result = []
with open('test.csv') as file:
    reader = csv.DictReader(file)

    for row in reader:
        result.append(row)

# print(result)
# print(type(result))


grouped = collections.defaultdict(list)
# print(grouped)

for item in result:
    grouped[item['city']].append(item)

# print(grouped)

# for item in grouped.items():
#     print()
#     print(item)

for key, value in grouped.items():
    print()
    print(key)
    print(str(value))
