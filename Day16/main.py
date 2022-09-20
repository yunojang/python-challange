from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()


def coffee_process():
    order = input("What's you want? (espresso, latte, cappuccino): ")
    if order == "off":
        return False
    elif order == "report":
        coffeeMaker.report()
        moneyMachine.report()
        return True

    drink = menu.find_drink(order)

    if not drink:
        return True

    if not coffeeMaker.is_resource_sufficient(drink):
        return True

    enogh_money = moneyMachine.make_payment(drink.cost)

    if not enogh_money:
        return True

    coffeeMaker.make_coffee(drink)
    return True


loop = True
while loop:
    loop = coffee_process()
