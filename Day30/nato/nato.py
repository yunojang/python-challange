import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {v.letter: v.code for _, v in nato_dataframe.iterrows()}
# print(nato)


def get_word():
    return input("Enter a word: ").upper()


# retry = True

# while retry:
#     word = get_word()  # all string
#     try:
#         # key가 input에 의존한다 -> expection 발생 가능성
#         codes = [nato[letter] for letter in word]
#     except KeyError:
#         # key error except에 대응한다.
#         print("Please only letters in the alphabet")
#     else:
#         print(codes)
#         retry = False


def gen_phonetic():
    word = get_word()
    try:
        codes = [nato[letter] for letter in word]
    except KeyError:
        print("Please only letters in the alphabet")
        gen_phonetic()
    else:
        print(codes)


gen_phonetic()
