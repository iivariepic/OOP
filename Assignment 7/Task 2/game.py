from dice import Dice

def round(dices:list[Dice]):
    result:int = 0

    for dice in dices:
        dice.roll()
        result += dice.sideup

    return result

def game(dices:list[Dice]):
    player1_score:int = round(dices)
    player2_score:int = round(dices)

    while player1_score == player2_score:
        player1_score: int = round(dices)
        player2_score: int = round(dices)

    print("Game over")
    print(f"Player 1 score: {player1_score}")
    print(f"Player 2 score: {player2_score}")

def main():
    user_input = input("How many die would you like to use? ")
    while not user_input.isnumeric():
        user_input = input("Please enter a valid number of die: ")

    user_input = int(user_input)
    dices = [Dice() for _ in range(user_input)]
    game(dices)

if __name__ == "__main__":
    main()
