# hangman game
from words import get_rand_word
from hangman_ascii import print_intro, print_lives

life = 6

print_intro()


def print_empty(target, answor_arr):
    for i in target:
        if i in answor_arr:
            print(i, end="")
        else:
            print("_", end="")
    print()


def print_result(life):
    if life <= 0:
        print("You lose...TT :(")
    else:
        print("Congraturation you win!!!!!")


target_word = get_rand_word()
target_len = len(target_word)

answer = []
correct_cnt = 0

while correct_cnt < target_len and life > 0:
    char = input("Guess target word: ")

    if char in answer:
        print("Already has answer!")
        continue

    print(f"You guess {char}, ", end="")
    answer.append(char)

    if char not in target_word:
        print("But not include, lose life")
        life -= 1
    else:  # correct char
        print("This is correct char")
        cnt = 0
        for c in target_word:
            if char == c:
                cnt += 1
        correct_cnt += cnt

    print_empty(target_word, answer)
    print_lives(life)

print_result(life)
