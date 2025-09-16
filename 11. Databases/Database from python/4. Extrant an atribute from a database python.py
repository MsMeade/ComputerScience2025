import csv
file = open("patients.csv","r")
records = list(csv.reader(file))
file.close()
for record in records:
    print(record[4])