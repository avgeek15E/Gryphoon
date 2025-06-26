import csv

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])

    reader = csv.DictReader(file)
    