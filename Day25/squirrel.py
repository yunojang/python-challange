import pandas

squirrel = pandas.read_csv("input/squirrel_data.csv")

COLORS = ["Black", "Cinnamon", "Gray"]

data_dict = {
    "Fur Color": [],
    "count": [],
}

for color in COLORS:
    count = len(squirrel[squirrel["Primary Fur Color"] == color])
    data_dict["Fur Color"].append(color)
    data_dict["count"].append(count)

result = pandas.DataFrame(data_dict)
print(result)

result.to_csv("output/squirrel_count.csv")
