import pandas

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {v.letter: v.code for _, v in nato_dataframe.iterrows()}
# print(nato)

word = input("Enter a word: ")
codes = [nato[letter.upper()] for letter in word]

print(codes)
