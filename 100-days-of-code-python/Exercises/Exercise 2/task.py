print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))

print((1 + int(tip) / 100))

payment_each = round((bill / people) * (1 + int(tip) / 100), 2)

print(f"Your total each person is: {payment_each}")


