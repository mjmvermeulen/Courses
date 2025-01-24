from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def coffee_machine_on():
    """
    Simulates a coffee machine that is working though orders
    """
    options = machine_menu.get_items()

    user_choice = input(f"What would you like? ({options})").lower()

    if user_choice == "off" or user_choice == "report":
        maintainers_command_handler(user_choice)
        user_choice = input(f"What would you like? ({options})").lower()

    # Initial check to see that the drink was part of the menu
    drink, drink_status = drink_choice_handler(user_choice)

    # Check if chosen drink exists
    while not drink_status:
        user_choice = input(f"What would you like? ({options})").lower()
        if user_choice == "off" or user_choice == "report":
            maintainers_command_handler(user_choice)
        else:
            drink, drink_status = drink_choice_handler(user_choice)

    payment_status = payment_handler(drink)
    while not payment_status:
        return True

    coffee_maker.make_coffee(drink)

    return True

def drink_choice_handler(user_choice):
    """
    Takes actions based on the drink that was chosen
    """
    drink = Menu.find_drink(machine_menu, order_name=user_choice)
    # Checks if drink is found if not asks user to choose again
    if not drink:
        return drink, False
    # Check if there are enough resources for the requested drink
    else:
        return drink, coffee_maker.is_resource_sufficient(drink)

def payment_handler(drink):
    """
    Handles the payment for the drink
    """
    return money_machine.make_payment(drink.cost)

def maintainers_command_handler(command):
    """
    Handles the maintainers commands
    """
    # Turns machine off
    if command == "off":
        exit()

    # Prints the resource report
    if command == "report":
        coffee_maker.report()
        money_machine.report()

# Simulates the machine being turned on
machine_status = True

# Simulates the machine being powered and active for use
while machine_status:
    machine_status = coffee_machine_on()
