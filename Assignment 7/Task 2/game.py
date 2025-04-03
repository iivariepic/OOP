from dice import Dice
from player import Player
from mammal import Mammal

def game(playerdict:dict):
    result_dict:dict = {}

    for player in playerdict.keys():
        dice = playerdict[player]
        dice.roll()
        result_dict[player] = dice.sideup

    return result_dict

def main():
   player1 = Player("A", 1)
   player2 = Player("B", 2)
   player3 = Player("C", 3)
   player1.pet = Mammal(1, "Dog", "Haukku", 10, 100)
   player2.pet = Mammal(2, "Cat", "Miukku", 8, 80)
   player3.pet = Mammal(3, "Gerbil", "Germa", 2, 20)

   players:dict = {
       player1: Dice(),
       player2: Dice(),
       player3: Dice(),
   }

   result:dict = game(players)
   print(f"The winner is {max(result, key=result.get)} with a score of {max(result.values())}")



if __name__ == "__main__":
    main()
