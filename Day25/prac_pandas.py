import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))

temperatures = data["temp"]
# print(type(temperatures))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# pandas API

# avg = sum(temp_list) / len(temp_list)
# print(avg)

print(temperatures.mean())  # Series API
print(data["temp"].max())

