char = input("charater: ")
shift_num = int(input("shift number: "))


def shift(char, num):
    code = ord(char) + num

    if code - 97 > 25:
        code = (code - 97) % 26
        code += 97

    return chr(code)


print(shift(char, shift_num))
