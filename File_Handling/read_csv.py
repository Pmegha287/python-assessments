import csv
with open("data.csv") as f:
    for row in csv.reader(f):
        print(row)