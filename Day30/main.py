files = ["abc"]
try:
    file = files[0]
    with open("a_data.txt", mode="w") as f:
        # data = f.read()
        # print(data)
        a = f.write("hi")
except IndexError:
    file = "default"
except FileNotFoundError:
    print("incorrect file")
else:
    print(f"{file} {a}")
finally:
    print(file)
