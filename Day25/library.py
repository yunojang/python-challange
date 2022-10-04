import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    temperatures = []
    for row in list(data)[1:]:
            temperatures.append(int(row[1]))

print(temperatures)
