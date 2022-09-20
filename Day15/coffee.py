# coffe machine program

# 1. print report

# 2. check resources -> sorry

# 3. process coins -> 구분

# 4. check transaction successful

# 5. make coffe

from menu import MENU


resource = {"water": 0, "milk": 0, "coffee": 0, "income": 0}


HELP_COMMAND = """
  report - Current resources of the coffee machine.
  supply - Supply coffee ingredients
  exit - Exit this program
"""


def print_report():
    for k, v in resource.items():
        print(k, v)


def get_oper():
    oper = input("What would you like? (espresso/latte/cappuccino/help): ")
    return oper


def exit_program():
    print("Exit coffe machine")
    exit(0)


def supply():
    ingredient = input("What kind of ingredients? (water/milk/coffee): ")
    amount = int(input("amount: "))

    if ingredient in resource:
        resource[ingredient] += amount


def income(money): 
    resource["income"] += money


INGREDIENTS = ["water", "milk", "coffee"]


def make_coffe(menu):
    require = menu["ingredients"]

    for ingredient in INGREDIENTS:
        if resource[ingredient] < require[ingredient]:
            print(f"❌ Not enough {ingredient}, Please supply!")
            return False
        else:
            resource[ingredient] -= require[ingredient]

    income(menu["cost"])
    return True


print("Welcome coffe machine")
loop = True


def coffe_process():
    oper = get_oper()

    is_help = oper == "help"
    is_exit = oper == "exit"
    is_report = oper == "report"
    is_supply = oper == "supply"

    if is_help:
        print(HELP_COMMAND)
        return

    if is_report:
        print_report()
        return

    if is_exit:
        exit_program()

    if is_supply:
        supply()
        return

    if oper not in MENU:
        print(f"Enter the correct menu, {oper} is not valid")
        return

    menu = oper

    cost = MENU[menu]["cost"]
    thousand = int(input("How much money do you have? 1000: "))
    f_hundred = int(input("How much money do you have? 500: "))
    hundred = int(input("How much money do you have? 100: "))

    total = thousand * 1000 + f_hundred * 500 + hundred * 100

    if total > cost:
        print(f"💵 Change: [{total - cost}]")
    elif total < cost:
        print(f"❌ Not enough money [{menu} is {cost}]")
        return

    success = make_coffe(MENU[menu])

    if success:
        print(f"✔ Here's your {menu}, Have a nice day!")


while loop:
    coffe_process()
