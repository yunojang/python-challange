from operator import mod


with open("my_file.txt", mode="a") as file:
    file.write("any string")

with open("new_created_file.txt", mode="w") as file:
    file.write("Hi!!")
