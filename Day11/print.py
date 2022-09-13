def print_msg(msg):
    print(f"#### {msg} ####")


from enum import Enum


class Result(Enum):
    WIN = "win"
    DRAW = "draw"
    LOSE = "lose"


msg = {
    Result.WIN: "Win 🥳",
    Result.DRAW: "Draw 😐",
    Result.LOSE: "Lose 😭",
}


def print_result(result):
    print(f"Player: [{msg[result]}]")


def print_status(status):
    print()
    print("------Player Status-------")
    print(
        f"Match History: [ W{status[Result.WIN]} D{status[Result.DRAW]} L{status[Result.LOSE]} ]"
    )
    print(f"Chips: [C{status['chip']}]")
    print("--------------------------")
