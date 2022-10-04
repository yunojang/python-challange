import pandas

data = pandas.read_csv("weather_data.csv")

# get Data in Columns
print(data["day"])
print(data.condition)

# get Data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

print(monday.condition)
monday_temp_F = monday.temp * 1.8 + 32

print(monday_temp_F)
