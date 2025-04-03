from dice import Dice
from player import Player

def game(playerdict:dict):
    result_dict:dict = {}
    player_number:int = 1

    for dice in playerdict.values():
        dice.roll()
        result_dict[f"Player {player_number}"] = dice.sideup
        player_number += 1

    return result_dict

def main():
    user_input = input("How many players? ")
    while not user_input.isnumeric():
        user_input = input("Please enter a number: ")

    user_input = int(user_input)

    players: dict = {}
    for i in range(user_input):
        player_name:str = input(f"Enter a name for Player {i + 1}: ")
        player = Player(player_name, i+1)
        dice = Dice()
        players[player.player_id] = dice

    print(game(players))


if __name__ == "__main__":
    main()
