# Using pandas Library
import pandas as pd
import csv

df = pd.read_csv('A:/Python_Test/data.csv')
print(df)

print("------------------")

with open('mydata.csv', 'r') as myfile:
    print(myfile.read())

print("-------------------")
with open('mydata.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0], row[1], row[2], sep='|')
