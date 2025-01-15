import random
import time

def get_input():
    # Function to get a valid input from the user
    print("""
Please select an option:
1. Rock
2. Paper
3. Scissors""")

    # Mapping to allow the user to type the word or number
    option_mapping = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors"}

    option = input().capitalize()

    while True:
        if option in option_mapping.keys():
            option = option_mapping[option]

        is_valid = check_input(option)
        if is_valid:
            break
        option = input("Invalid option. Please select properly!: ")

    return option

def check_input(target):
    # Function to check the validity of an option
    valid_options = ["Rock", "Paper", "Scissors"]
    if target not in valid_options:
        return False
    return True

def generate_computer_input():
    # Function to generate the computer input
    option_mapping = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors"}

    return option_mapping[str(random.randint(1, 3))]

def check_victory(user_choice, computer_choice):
    # Function to check the winner
    winner = []

    # Check for draw
    if user_choice == computer_choice:
        return winner

    if user_choice == "Rock":
        if computer_choice == "Scissors":
            winner.append("player")
        else:
            winner.append("computer")

    elif user_choice == "Paper":
        if computer_choice == "Rock":
            winner.append("player")
        else:
            winner.append("computer")

    else: # User chose scissors
        if computer_choice == "Paper":
            winner.append("player")
        else:
            winner.append("computer")

    return winner

def main():
    user_score = 0
    computer_score = 0

    while True:
        # Get choices
        user_choice = get_input()
        computer_choice = generate_computer_input()
        print(f"You chose {user_choice}")
        time.sleep(2.0)
        print(f"Computer chose {computer_choice}")
        time.sleep(2.0)

        # Get Winner
        winner = check_victory(user_choice, computer_choice)
        if "player" in winner:
            user_score += 1
        elif "computer" in winner:
            computer_score += 1

        if len(winner) > 0:
            print(f"The winner is {winner[-1].capitalize()}")
        else:
            print("It's a draw!")
        time.sleep(2.0)
        print(f"\nYour score is {user_score}")
        print(f"The computer's score is {computer_score}")
        input("Press Enter to continue...")

        # Check if game should be ended
        if user_score == 3 or computer_score == 3:
            break

    if user_score > computer_score:
        print("You win!")

    else:
        print("Computer wins!")

if __name__ == "__main__":
    main()