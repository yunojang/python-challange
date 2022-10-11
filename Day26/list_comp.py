numbers = [1, 2, 3, 4]
new_list = [n + 1 for n in numbers]

print(new_list)


new_list = [n**2 for n in numbers]
print(new_list)


name = "Yuno"
new_list = [c for c in name]
print(new_list)

print(name.split())


new_list = [n * 2 for n in range(1, 5) if n % 2 == 0]
print(new_list)


new_list = [n for n in range(1, 11) if n % 2 == 0]
print(new_list)


names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
upper_long_names = [n.upper() for n in names if len(n) >= 5]

print(upper_long_names)
