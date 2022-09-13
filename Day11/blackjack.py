# blackjack capstone
import random
import time
from print import print_msg, print_result, Result, print_status

print("Welcome to the Blackjack game land")
print()
cards = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def get_score(card):
    if card.isdigit():
        return int(card)
    else:
        if card == "A":
            return 11
        else:
            return 10


def get_sum_cards(cards):
    scores = list(map(get_score, cards))

    while 11 in scores and sum(scores) > 21:
        scores[scores.index(11)] = 1

    return sum(scores)


def print_card(player, dealer):
    print("-----------------")
    print(f"Your Card: {player} = {get_sum_cards(player)}")
    print(f"Dealer Card: {dealer} = {get_sum_cards(dealer)}")
    print("-----------------")


def get_card(num=1):
    result = []
    time.sleep(0.3)

    for _ in range(num):
        result.append(random.choice(cards))

    return result


def bet_chip(status, chip):
    if chip < 0:
        print_msg("You are cheeter")
        status['chip'] = -9999
        gameover()

    if chip == 0 or chip > status["chip"]:
        print("Enter the correct value")
        bet_chip(status, int(input(f"Bet again [have: C{status['chip']}]: ")))

    return chip


def record_result(status, result, bet):
    status[result] += 1

    if result == Result.WIN:
        status["chip"] += bet
    elif result == Result.LOSE:
        status["chip"] -= bet


def restart_question():
    if player_status["chip"] <= 0:
        gameover()

    yes = input(
        "Do you want to restart a game of Blackjack? Type 'y' or 'n': ") == 'y'

    print_status(player_status)

    if yes:
        play()
    else:
        print_msg("Bye")
        exit(0)


def gameover():
    print_status(player_status)
    print_msg("Game over")
    exit(0)


player_status = {
    "chip": 200,
    Result.WIN: 0,
    Result.DRAW: 0,
    Result.LOSE: 0,
}


def play():
    player = []
    dealer = []

    print_msg("Draw first cards")

    player += get_card()
    dealer += get_card()
    print_card(player, dealer)

    bet = bet_chip(
        player_status,
        int(input(f"Bet your chip [have: {player_status['chip']}]: ")))

    is_hit = True
    is_busted = False

    while is_hit:
        print_msg("Draw next cards")

        player += get_card()
        print_card(player, dealer)

        if get_sum_cards(player) > 21:
            print_msg("You are Busted!")
            is_busted = True
            break

        is_hit = input(
            "Input your turn, Type 'h' to hit, another to stop: ") == 'h'

    if is_busted:
        print_result(Result.LOSE)
        record_result(player_status, Result.LOSE, bet)
        restart_question()

    while get_sum_cards(dealer) < 16:
        print_msg("Draw dealer's next card")

        dealer += get_card()
        print_card(player, dealer)

    if get_sum_cards(dealer) > 21:
        print_msg("Dealer Busted!")

        print_result(Result.WIN)
        record_result(player_status, Result.WIN, bet)
        restart_question()

    result = ""

    if get_sum_cards(player) == get_sum_cards(dealer):
        result = Result.DRAW
    elif get_sum_cards(player) > get_sum_cards(dealer):
        result = Result.WIN
    else:
        result = Result.LOSE

    print_result(result)
    record_result(player_status, result, bet)
    restart_question()


play()
