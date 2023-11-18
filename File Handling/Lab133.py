import csv

data = [
    ['Name', 'Age', 'ID'],
    ['Alice', 30, '1'],
    ['Bob', 25, '2'],
    ['Charlie', 22, '3']
]

with open('test2.csv', 'w') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
#
# with open('test2.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row[0], row[1], row[2], sep='|')


temp_data = []
id_update = 2
new_age = 26

with open('test2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp_data.append(row)

# for row in temp_data:
#     print(row[0])
#     print(row[2])
#     if row[0] == id_update:
#         row[2] = new_age

temp_data[2][2] = 26
print(temp_data)

with open('satish.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(temp_data)
