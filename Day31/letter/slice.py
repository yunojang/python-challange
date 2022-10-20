with open("en.txt") as f:
    words = [line.split(" ")[0] for line in f.readlines()]

with open("letter.txt", "w") as f:
    f.write("\n".join(words))
