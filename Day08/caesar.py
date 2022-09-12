print("Welcome to Caesar cipher")

# def crypt(crypt_func, message):
#     result = ""

#     for char in message:
#         result += crypt_func(ord(char))

#     return result

# def encode(message, shift):
#     return crypt(lambda code: chr(code + shift), message)

# def decode(message, shift):
#     return crypt(lambda code: chr(code - shift), message)


def caesar(message, shift, direction):
    result = ""

    if direction == 'decode':
        shift *= -1

    for char in message:
        code = ord(char) + shift
        result += chr(code)

    return result


restart = True

while restart:
    # is_encode = input(
    #     "Type 'encode' to encrypt, type 'decode to decrypt: ") == 'encode'
    direction = input("Type 'encode' to encrypt, type 'decode to decrypt: ")
    msg = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    print(caesar(msg, shift, direction))

    restart = input("Type 'yes' if you want to go again: ") == 'yes'
