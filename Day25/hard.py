data = []

with open("weather_data.csv") as f:
    lines = f.readlines()[1:]
    for line in lines:
        data.append(line.strip().split(","))

print(data)
