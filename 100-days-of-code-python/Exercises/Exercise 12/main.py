from random import randint

import art

def game_difficulty_choice():
    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    game_difficulty_chosen = False

    while not game_difficulty_chosen:
        if game_difficulty == "easy":
            game_difficulty_chosen = True
            lives = 10
            return lives
        elif game_difficulty == "hard":
            game_difficulty_chosen = True
            lives = 5
            return lives
        else:
            print(f"{game_difficulty} isn't a valid option, please choose 'easy' or 'hard'")
            game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def guess_number_game():
    # Game startup dialog
    print(art.custom_logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Allows users to select their desired difficulty
    lives = game_difficulty_choice()
    # Generates the number to be guessed
    target_number = randint(1, 100)
    print(target_number)

    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = input("Make a guess: ")

        try:
            guess = int(guess)
            if guess == target_number:
                print(art.player_win)
                print("You found the number I was thinking of you win!")
                print(f"You had {lives} lives remaining!")
                break
            elif guess > target_number:
                print("Too high.")
                lives -= 1
            elif guess < target_number:
                print("Too low.")
                lives -= 1
        except ValueError:
            print(f"{guess}, is not a number. please guess a number")
    else:
        print(art.player_lose)
        print("You ran out of lives. You lose!")

# Runs the game
guess_number_game()
