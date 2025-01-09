print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("Left of right?\n")
wait_or_swim = ""
red_yellow_blue = ""

if left_or_right == "Left" or left_or_right == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input('Type "Wait" to wait for a boat. type "swim" to swim across\n')
else:
    print("You fell into a hole. Game Over.")
    exit()

if wait_or_swim == "Wait" or wait_or_swim == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors.")
    red_yellow_blue = input("One red, one yellow, one blue. Which colour do you choose?\n")
else:
    print("Attacked by trout. Game Over.")
    exit()

if red_yellow_blue == "Yellow" or red_yellow_blue == "yellow":
    print("You Win!")
elif red_yellow_blue == "Blue" or red_yellow_blue == "blue":
    print("Eaten by beasts. Game Over.")
    exit()
elif red_yellow_blue == "Red" or red_yellow_blue == "red":
    print("Burned by fire. Game Over.")
    exit()
else:
    print("Game Over.")
    exit()
