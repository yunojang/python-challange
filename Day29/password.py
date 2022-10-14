from random import shuffle, choice

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def getRandomItems(arr, itemLen=1):
    return [choice(arr) for _ in range(itemLen)]


def getRandomLetter(len):
    return getRandomItems(letters, len)


def getRandomNumber(len):
    return getRandomItems(numbers, len)


def getRandomSymbol(len):
    return getRandomItems(symbols, len)


def getRandomPassword(**kw):
    number = kw.get("numbers") if kw.get("numbers") else 0
    letter = kw.get("letters") if kw.get("letters") else 0
    symbol = kw.get("symbols") if kw.get("symbols") else 0

    password_items = (
        getRandomLetter(letter) + getRandomNumber(number) + getRandomSymbol(symbol)
    )

    shuffle(password_items)

    return "".join(password_items)


if __name__ == "__main__":
    print(f"Your password is {getRandomPassword(numbers=5, symbols=2)}")
