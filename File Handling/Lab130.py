# csv - format

import csv

with open('A:/Python_Test/data.csv') as csvfile:
    reader = csv.reader(csvfile)
    print(reader)
    print("---------------")
    for row in reader:
        print(row[0], row[1], row[2], sep='|')
