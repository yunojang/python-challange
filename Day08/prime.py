def is_prime(n):
    if n < 4:
        return True

    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


n = int(input("Check this number: "))
msg = "" if is_prime(n) else "not"
print(f"The number {n} is {msg} prime!")
