import csv

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        name, age, city = row
        print(name, age, city)

csv_file.close()
