
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False f ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True


def process_coin():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if the total coins inserted are enough to place an order. Otherwise, False"""
    transaction_successful = True
    if drink_cost > money_received:
        print("Sorry that's not enough money. Money refunded.")
        print(f"The total cost is: ${drink_cost} but you inserted ${money_received}")
        return not transaction_successful

    change = round(money_received - drink_cost, 2)
    print(f"Here's ${change} in change")
    global profit
    profit += drink_cost
    return transaction_successful


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕️")


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice not in ["espresso", "latte", "cappuccino", "off", "report"]:
        print("You entered a wrong choice!!!")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink_chosen = MENU[user_choice]
        if is_resource_sufficient(drink_chosen["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(money_received=payment, drink_cost=drink_chosen["cost"]):
                make_coffee(user_choice, drink_chosen["ingredients"])


