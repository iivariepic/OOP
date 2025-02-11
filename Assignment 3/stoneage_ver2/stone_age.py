
from item import Item
from character import Character
from backpack import Backpack
from tools import Tools


class StoneAge:
    """
        Root class for testing components of 
        the adventure game.
    
        Copyright: Sami Pyöttilä, 2006
    """


    
    @staticmethod
    def main():
        StoneAge.test_items_and_characters()

    @staticmethod
    def test_items_and_characters():
        stone = Item("small stone", 0.0, 2.0, 5.0, 10000.0)
        small_axe = Item("camping axe", 25.0, 6.0, 30.0, 42.0)

        print(small_axe)
        print(stone)
        
        leather_backpack = Backpack(100.0)
        print(leather_backpack)
        print(leather_backpack.is_empty())
 
        if (small_axe.get_volume() < leather_backpack.get_remaining_capacity()):
            leather_backpack.put(small_axe)

        print(leather_backpack.__str__())
        print(leather_backpack.is_empty())







 
        
        conan = Character("Conan", 20.0, 30.0, 15.0)
        jay = Character("Jay", 30.0, 20.0, 17.0)

        conan.set_backpack(leather_backpack)
        leather_backpack.put(stone)
        print(conan)

        """
        print(conan)
        print(jay)
       

        
        conan = Character("Conan", 20.0, 30.0, 15.0)
        jay = Character("Jay", 30.0, 20.0, 17.0)

        conan.set_left_hand(stone)
        conan.set_right_hand(small_axe)
        print(conan)
        print(jay)

        print("\n\n\n")
        print("Conan gives the axe to Jay...")
        conan.give_item(jay, conan.get_right_hand_item())
        print(conan)
        print(jay)

        print("\n\n\n")
        print("... Jay attacks Conan with the axe!")
        jay.attack(conan, True)
        jay.attack(conan, True)
        print(conan)
        print(jay)
        """


if __name__ == "__main__":
    StoneAge.main()

