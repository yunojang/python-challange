with open("file1.txt") as f1:
    first = [int(n.strip()) for n in f1.readlines()]

with open("file2.txt") as f1:
    second = [int(n.strip()) for n in f1.readlines()]

multiple = [n for n in first if n in second]
print(multiple)
