def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiple(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": sub,
    "*": multiple,
    "/": divide,
}


def calc():
    restart = True
    num1 = float(input("What's the first Number: "))

    while restart:
        # print(f"Current number is {num1}")

        oper = input("What's the operator ['+', '-', '*', '/'] : ")
        num2 = float(input("What's the next Number: "))
        result = operators[oper](num1, num2)

        print(f"{num1} {oper} {num2} = {result}")

        num1 = result
        restart = input(f"Restart with [{result}]? 'y' or 'n': ") == 'y'

        if not restart:
            calc()


calc()
