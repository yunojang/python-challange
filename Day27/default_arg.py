def add(a=10, *args):
    return a + sum(args)
    # sum = 0
    # for num in args:
    #   sum += num

    # return sum


print(add())
print(add(15))
