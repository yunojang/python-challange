for num in range(1, 101):
    out = num

    if num % 3 == 0 and num % 5 == 0:
        out = "Fizz Buzz"
    elif num % 3 == 0:
        out = "Fizz"
    elif num % 5 == 0:
        out = "Buzz"
    print(out)