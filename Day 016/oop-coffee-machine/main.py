from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    is_on = True
    while is_on:
        options = menu.get_items()
        order = input(f"​What would you like? ({options}): ").lower()
        if order == "off":
            print("Turning off... Goodbye!")
            is_on = False
        elif order == "report":
            coffee_maker.report()
            money_machine.report()
        elif menu.find_drink(order) != None:
            order_item = menu.find_drink(order)
            sufficient_resources = coffee_maker.is_resource_sufficient(order_item)
            if sufficient_resources and money_machine.make_payment(order_item.cost):
                coffee_maker.make_coffee(order_item)
        else:
            print("Invalid input. Try again.")

main()