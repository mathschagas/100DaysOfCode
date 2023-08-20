MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(order):
    for key in MENU[order]['ingredients']:
        if MENU[order]['ingredients'][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def consume_resources(order):
    for key in MENU[order]['ingredients']:
        resources[key] -= MENU[order]['ingredients'][key]

def process_coins():
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def main():
    money = 0.0
    is_on = True
    while is_on:
        order = input("​What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "off":
            print("Turning off... Goodbye!")
            is_on = False
        elif order == "report":
            print_report(money)
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            sufficient_resources = check_resources(order)
            if sufficient_resources:
                inserted_money = process_coins()
                if inserted_money < MENU[order]['cost']:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    consume_resources(order)
                    money += MENU[order]['cost']
                    change = inserted_money - MENU[order]['cost']
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    print(f"Here is your {order} ☕️. Enjoy!")
        else:
            print("Invalid input. Try again.")

main()