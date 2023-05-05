import csv
import matplotlib.pyplot as plt

labels = []
values = []

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        labels.append(row[0])
        values.append(int(row[1]))

fig, ax = plt.subplots()

ax.barh(labels, values)

plt.show()
