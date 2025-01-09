import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def new_calc():
    """The initial/new calculation starts with this function"""
    print(art.logo)
    first_number = float(input("What's the first number?:  "))
    print("+\n-\n*\n/\n")
    operation_input = input("Pick an operation:  ")
    second_number = float(input("What's the second number?:  "))

    return calculator_operation(first_number, operation_input, second_number)

def continues_calc(n1):
    """allows for continues calculations with the results of the first calculation"""
    first_number = n1
    print("+\n-\n*\n/\n")
    operation_input = input("Pick an operation:  ")
    second_number = float(input("What's the second number?:  "))

    return calculator_operation(first_number, operation_input, second_number)

def calculator_operation(number1_input, operation_input, number2_input):
    """Handles the calculations based on picked operation"""
    calculator_actions = {
        "+": add(number1_input, number2_input),
        "-": subtract(number1_input, number2_input),
        "*": multiply(number1_input, number2_input),
        "/": divide(number1_input, number2_input)
    }

    calc_result = float(calculator_actions[operation_input])
    continue_calculation = input(f'Type "y" to continue calculating with {calc_result}, or type "n" to start a new calculation: ')

    return continue_calculation, calc_result

#Starts the calculator
calc_action = new_calc()

while True:
    if calc_action[0] == "y" or calc_action[0] == "Y":
        calc_action = continues_calc(calc_action[1])
    else:
        calc_action = new_calc()
