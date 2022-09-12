# avg - only for
height_list = input("Input a list of heights: ").split(" ")
total = 0
cnt = 0

for height in height_list:
    total += int(height)
    cnt += 1

print(height_list, cnt)
print(f"avg height: {round(total/cnt)}")
