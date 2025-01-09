import moves
import random

answer = "y"

while answer == "y" or answer == "Y":
    print("Welcome to rock, paper and scissors, you will be playing against me!\n"
          "Now Get ready, Rock, Paper, Scissors SHOOT!")
    user_move = input('Type "rock", "paper" or "scissors" to pick your move!\n')

    # Generates the opponents pick
    rand_num = random.randint(1, 3)
    opponent_move = ""

    # uses the random number to set opponents move
    if rand_num == 1:
        opponent_move = "rock"
    elif rand_num == 2:
        opponent_move = "paper"
    elif rand_num == 3:
        opponent_move = "scissors"

    # Checks for results if user picked rock
    if user_move == "rock" and opponent_move == "rock" or user_move == "Rock" and opponent_move == "Rock":
        print(f"You: {moves.rock}\n"
              f"Opponent: {moves.rock}\n"
              f"Draw!")
    elif user_move == "rock" and opponent_move == "paper" or user_move == "Rock" and opponent_move == "Paper":
        print(f"You: {moves.rock}\n"
              f"Opponent: {moves.paper}\n"
              f"You Lose!")
    elif user_move == "rock" and opponent_move == "scissors" or user_move == "Rock" and opponent_move == "Scissors":
        print(f"You: {moves.rock}\n"
              f"Opponent: {moves.scissors}\n"
              f"You Win!")
    # Checks for results if user picked paper
    elif user_move == "paper" and opponent_move == "rock" or user_move == "Paper" and opponent_move == "Rock":
        print(f"You: {moves.paper}\n"
              f"Opponent: {moves.rock}\n"
              f"You Win!")
    elif user_move == "paper" and opponent_move == "paper" or user_move == "Paper" and opponent_move == "Paper":
        print(f"You: {moves.paper}\n"
              f"Opponent: {moves.paper}\n"
              f"Draw!")
    elif user_move == "paper" and opponent_move == "scissors" or user_move == "Paper" and opponent_move == "Scissors":
        print(f"You: {moves.paper}\n"
              f"Opponent: {moves.scissors}\n"
              f"You Lose!")
    # Checks for results if user picked scissors
    elif user_move == "scissors" and opponent_move == "rock" or user_move == "Scissors" and opponent_move == "Rock":
        print(f"You: {moves.scissors}\n"
              f"Opponent: {moves.rock}\n"
              f"You Lose!")
    elif user_move == "scissors" and opponent_move == "paper" or user_move == "Scissors" and opponent_move == "Paper":
        print(f"You: {moves.scissors}\n"
              f"Opponent: {moves.paper}\n"
              f"You Win!")
    elif user_move == "scissors" and opponent_move == "scissors" or user_move == "Scissors" and opponent_move == "Scissors":
        print(f"You: {moves.scissors}\n"
              f"Opponent: {moves.scissors}\n"
              f"Draw!")

    answer = input("Do you want to play again? (y/n)\n")
else:
    print("Goodbye")
    exit()
