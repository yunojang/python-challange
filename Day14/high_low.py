from celeb import get_random_celeb, get_intro_str, print_winner

print("Welcome high low game!")

score = 0
failed = False
next_celeb = get_random_celeb()

while not failed:
    print("---Who has more Instagram followers?---")
    print()
    print(f"'A'. {get_intro_str(next_celeb)}")

    random_celeb = get_random_celeb()
    print(f"'B'. {get_intro_str(random_celeb)}")

    choice = input("Who has more followers? Pick 'A' or 'B': ")

    a_count = next_celeb["follower_count"]
    b_count = random_celeb["follower_count"]

    is_correct = (a_count > b_count and choice == "A") or (
        a_count < b_count and choice == "B"
    )

    if a_count == b_count or is_correct:
        score += 1
    else:
        failed = True

    print_winner(next_celeb, random_celeb)

    next_celeb = random_celeb

print(f"Your score is {score}")
