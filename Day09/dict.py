dict = {"key": "string"}

print(dict["key"])
# print(dict.key)

dict["key"] = 10

print(dict)

for key in dict:
    print(key)
    print(dict[key])

for v in dict.values():
    print(v)

for k, v in dict.items():
    print(k, v)

dict[1] = 20

print(dict)