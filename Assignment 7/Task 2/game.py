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
    dice1 = Dice()
    dice2 = Dice()
    dice3 = Dice()

    dices:list = [dice1,dice2,dice3]
    game(dices)

if __name__ == "__main__":
    main()
