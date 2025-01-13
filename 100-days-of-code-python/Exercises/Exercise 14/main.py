import random
import art
import game_data

def higher_lower_game():
    print(art.logo)
    player_score = compare_data()
    print(f"Sorry, that's wrong. Final score: {player_score}")

def compare_data():
    game_running = True
    player_score = 0
    while game_running:
        option_list = random.choices(game_data.data, k=2)
        option_a = option_list[0]
        option_b = option_list[1]

        # Displays the choices
        print(f"Compare A: {option_a['name']}, {option_a['description']} from {option_a['country']}")
        print(art.vs)
        print(f"Compare B: {option_b['name']}, {option_b['description']} from {option_b['country']}")

        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        player_choice_made = False
        # Makes sure the player choose either A or B
        while not player_choice_made:
            if player_choice == "a" or player_choice == "b":
                break
            else:
                print("Please make sure you choose between A or B")
                player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Checks whether the Players choice was right or wrong
        if player_choice == "a":
            if option_a["follower_count"] > option_b["follower_count"]:
                player_score += 1
                print(f"You're right!, Current score: {player_score}")
            elif option_a["follower_count"] < option_b["follower_count"]:
                game_running = False
            else:
                player_score += 1
                print(f"They have the same amount of followers!, Current score: {player_score}")
        elif player_choice == "b":
            if option_a["follower_count"] < option_b["follower_count"]:
                player_score += 1
                print(f"You're right!, Current score: {player_score}")
            elif option_a["follower_count"] > option_b["follower_count"]:
                game_running = False
            else:
                player_score += 1
                print(f"They have the same amount of followers!, Current score: {player_score}")
    return player_score

higher_lower_game()
