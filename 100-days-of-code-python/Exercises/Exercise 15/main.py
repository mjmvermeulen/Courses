from time import sleep

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
    "money": 0,
}

def coffee_machine():
    """
    Simulates a coffee machine that is turned on
    :return: machine_status
    """
    user_choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()
    choice_made = False

    # Checks if there is enough of each ingredient in order to make the requested drink
    # And handles the entire process of a user purchasing a drink
    while not choice_made:
        if user_choice == "espresso":
            resource_check(user_choice)
            payment_handler(user_choice)
            product_handler(user_choice)
            choice_made = True
        elif user_choice == "latte":
            resource_check(user_choice)
            payment_handler(user_choice)
            product_handler(user_choice)
            choice_made = True
        elif user_choice == "cappuccino":
            resource_check(user_choice)
            payment_handler(user_choice)
            product_handler(user_choice)
            choice_made = True
        # Added commands off and report these are maintainers commands for managing the machine
        elif user_choice == "off":
            return "off"
        elif user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
            user_choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()
        # If a non-existing command is used reset to command prompt
        else:
            print(f"Sorry we do not have {user_choice}")
            user_choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()

    return machine_status

def resource_check(user_choice):
    """
    Checks whether the machine has enough ingredients to make the drink requested
    :param user_choice:
    """
    for ingredient in MENU[user_choice]["ingredients"].keys():
        if MENU[user_choice]["ingredients"][ingredient] <= resources[ingredient]:
            continue
        else:
            print(f"Sorry there is not enough {ingredient} in the machine to make {user_choice}, please refill")

def payment_handler(user_choice):
    """
    Handles the user payments for their drinks
    :param user_choice:
    :return:
    """
    product_price = MENU[user_choice]["cost"]
    print(f"A {user_choice} will cost ${product_price}")
    owed_amount = round(product_price, 2)
    paid_amount = 0
    while owed_amount > 0:
        print(f"You still owe ${owed_amount}")
        print(f"Your balance ${paid_amount}, Please insert more coins.")
        # Because we are simulating a machine, we are going to assume that you can only put in the coins
        # that would mean that it would be impossible to insert a letter here normally since it would just be coins being counted
        # Hence I will not add a function to make sure the input here are only numeral.
        quarter_amount = int(input("how many quarters? "))
        dime_amount = int(input("how many dimes? "))
        nickle_amount = int(input("how many nickles? "))
        penny_amount = int(input("how many pennies? "))

        paid_amount += round(quarter_amount * 0.25, 2)
        paid_amount += round(dime_amount * 0.10, 2)
        paid_amount += round(nickle_amount * 0.05, 2)
        paid_amount += round(penny_amount * 0.01, 2)

        owed_amount = round(owed_amount - paid_amount, 2)

    resources["money"] += product_price

    if owed_amount < 0:
        print(f"Your Change: ${abs(owed_amount):.2f}")

def product_handler(user_choice):
    """
    Simulates the machine creating the drink and resetting to get ready for next customer
    :param user_choice:
    """
    for ingredient in MENU[user_choice]["ingredients"].keys():
        resources[ingredient] -= MENU[user_choice]["ingredients"][ingredient]

    print(f"Wait a moment while we make your {user_choice}")
    sleep(5)
    print(f"Done enjoy your {user_choice}")
    sleep(1)
    print("\n" * 90)

# Ensures that the machine will stay on when turned on : Acts like an on/off button
machine_status = "on"
while machine_status == "on":
    machine_status = coffee_machine()