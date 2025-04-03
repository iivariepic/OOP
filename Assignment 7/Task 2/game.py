from dice import Dice
from player import Player
from mammal import Mammal

def game(playerdict:dict):
    result_dict:dict = {}

    for player in playerdict.keys():
        result_dict[player] = 0

        for dice in playerdict[player]:
            dice.roll()
            result_dict[player] += dice.sideup

    return result_dict

def main():
    player1 = Player("A", 1)
    player2 = Player("B", 2)
    player3 = Player("C", 3)
    pet1 = Mammal(3, "Gerbil", "Germa", 2, 20)
    pet2 = Mammal(2, "Cat", "Miukku", 8, 80)
    pet3 = Mammal(1, "Dog", "Haukku", 10, 100)

    players:dict = {
       player1: [Dice(), Dice()],
       player2: [Dice(), Dice()],
       player3: [Dice(), Dice()],
    }

    ## Pet selection
    print("Selecting Pets")
    for player in players:
       for dice in players[player]:
           dice.roll()

    playersums: dict = {}
    for player in players:
        player_sum: int = 0
        for dice in players[player]:
            player_sum += dice.sideup

        playersums[player] = player_sum

    sorted_rolls = sorted(players, key=playersums.get, reverse=True)
    sorted_rolls[0].pet = pet3
    sorted_rolls[1].pet = pet2
    sorted_rolls[2].pet = pet1


    # Run game
    result:dict = game(players)
    print(f"The winner is {max(result, key=result.get)} with a score of {max(result.values())}")



if __name__ == "__main__":
    main()
