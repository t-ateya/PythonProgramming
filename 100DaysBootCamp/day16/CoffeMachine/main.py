from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""Program Requirements
1. Print Report
2. Check resource sufficient?

3. Process Coins

4. Check transaction successful?

5. Make coffee
"""

### 1. Print Report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



#2 Check Resources sufficient

is_machine_on = True
while is_machine_on:
    choice = input(f"Choose your menu from {menu.get_items()}:  ").lower()

    if choice == "report":
        money_machine.report()
        coffee_maker.report()
    elif choice == "off":
        is_machine_on = False
    else:
        drink_name = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_name) and money_machine.make_payment(drink_name.cost):
            coffee_maker.make_coffee(drink_name)
