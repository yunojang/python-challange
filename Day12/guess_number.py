import random


def get_number(max):
    return random.choice(list(range(max))) + 1


def guess(num):
    if num > target:
        print("Too high")
        print("Guess Again.")
        return False
    elif num < target:
        print("Too Low")
        print("Guess Again.")
        return False
    else:
        print(f"You got it! The answer was {target}")
        return True


print("Welcome to the Number guessing Game")
print("I'm thinking of a number between 1 and 100")
target = get_number(100)
difficult = input("choose a difficulty, Type 'easy' or 'hard': ")
attempt = 10 if difficult == "easy" else 5

while attempt > 0:
    print(f"You have {attempt} remaining to guess the number")
    guess_num = int(input("Make a guess: "))
    attempt -= 1

    if guess(guess_num):
        break
