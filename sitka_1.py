import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# The enumerate() fcn returns both the index of each item and the value of each
# item as you loop trough a list

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

# Get high temps
highs = []

for row in csv_file:
    highs.append(int(row[5]))

# p0rint(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()