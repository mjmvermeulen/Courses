import random
import sys
import art

def blackjack_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print(art.logo)
    # deals cards to player and adds their total together
    player_cards = random.sample(cards, 2)
    player_score = sum(player_cards)
    # deals cards to computer and adds their total together
    computer_cards = random.sample(cards, 1)
    computer_score = computer_cards[0]

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_score}")

    # Provides the player with options to get another card or to stand.
    another_card = input("Type 'y', to get another card, type 'n' to pass:")
    while another_card == "y" or another_card == "Y":
        new_card = random.sample(cards, 1)

        # Checks whether the ace(11) is used as 1 or 11, if new total is above 21 it will default the ace to be used as a 1 instead.
        new_player_cards_total = sum(player_cards) + sum(new_card)
        if new_card == [11]:
            if sum(player_cards) + sum(new_card) > 21:
                new_card = [1]

        # Adds the new card to the players hand and total score
        player_cards += new_card
        player_score = sum(player_cards)

        # print("another card")
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_score}")
        another_card = input("Type 'y', to get another card, type 'n' to pass:")

    # If player goes over 21 computer will just draw 1 card to win game.
    if player_score > 21:
        computer_cards += random.sample(cards, 1)
    else:# Computer will keep taking cards until its score is above 17 or past 21
        while sum(computer_cards) <= 17 and sum(computer_cards) <= 21:
            new_card = random.sample(cards, 1)
            if new_card == [11]:
                if sum(computer_cards) + sum(new_card) > 21:
                    new_card = [1]
            computer_cards += new_card

    computer_score = sum(computer_cards)
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if player_score > 21:
        print(f"You went over. You lose \U0001F624")
    elif computer_score > 21:
        print(f"Opponent went over. You win \U0001F601")
    elif player_score > computer_score:
        print(f"You hand was better than the computer. You win \U0001F601")
    else:
        print(f"You hand was worse than the computer. You lose \U0001F624")

    restart = input("Do you want to play a new game of Blackjack? Type 'y' or 'n':")
    return restart
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

if start_game == "n" or start_game == "N":
    sys.exit()
while start_game == "y" or start_game == "Y":
    start_game = blackjack_game()