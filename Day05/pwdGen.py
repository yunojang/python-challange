#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# 전부 뽑은 뒤 -> 하나씩 랜덤으로 뽑아서(splice) 배치하기


def getRandomOfArray(arr, itemLen=1):
    item = ''

    for a in range(0, itemLen):
        # index = random.randint(0, len(arr) - 1)
        # item += arr[index]
        item += random.choice(arr)

    return item


def getRandomLetter(len):
    return getRandomOfArray(letters, len)


def getRandomNumber(len):
    return getRandomOfArray(numbers, len)


def getRandomSymbol(len):
    return getRandomOfArray(symbols, len)


pick_password = getRandomLetter(nr_letters) + getRandomSymbol(
    nr_symbols) + getRandomNumber(nr_numbers)

print(pick_password)

mixed_password = ''

length = len(pick_password)

for cnt in range(length):
    idx = random.randint(0, len(pick_password) - 1)
    mixed_password += pick_password[idx]
    pick_password = pick_password[0:idx] + pick_password[idx + 1:]

print(f"Your password is: {mixed_password}")

# shuffle
passwords = []  # letter array
passwords = random.shuffle(passwords)