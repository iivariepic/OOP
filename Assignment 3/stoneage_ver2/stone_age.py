from item import Item
from character import Character
from backpack import Backpack
from shop import Shop
from gridtile import GridTile
from game import Game


class StoneAge:
    """
        Root class for testing components of
        the adventure game.

        Copyright: Sami Pyöttilä, 2006
    """



    @staticmethod
    def main():
        StoneAge.test_items_and_characters()
        new_game = Game()
        new_game.run()

    @staticmethod
    def test_items_and_characters():
        stone = Item("small stone", 0.0, 2.0, 5.0, 10000.0)
        small_axe = Item("camping axe", 25.0, 6.0, 30.0, 42.0)
        gold_chain = Item("gold chain", 1000.0, 10.0, 1.0, 1.0)

        print(small_axe)
        print(stone)

        leather_backpack = Backpack(100.0)
        print(leather_backpack)
        print(leather_backpack.is_empty())

        if small_axe.get_volume() < leather_backpack.get_remaining_capacity():
            leather_backpack.put(small_axe)

        print(leather_backpack.__str__())
        print(leather_backpack.is_empty())

        conan = Character("Conan", 20.0, 30.0, 15.0)
        maurice = Character("Maurice", 100.0, 100.0, 100.0)
        maurices_goods = Shop("Maurice's Goods", maurice)
        maurices_goods.add_item(gold_chain)

        conan.set_backpack(leather_backpack)
        leather_backpack.put(stone)
        print(conan)
        print("\nMAURICE'S GOODS:")
        maurices_goods.print_items()

        maurices_goods.sell_transaction(small_axe, conan)


        print("\nMAURICE'S GOODS:")
        maurices_goods.print_items()

        conan.change_money(40000.0)
        maurices_goods.buy_transaction(gold_chain, conan)

        print("\nConan's backpack's topmost slot and money:")
        print(conan.get_backpack().show_topmost())
        print(conan.get_money())

        print("\nTrying to gamble the gold chain for a stone axe")
        if maurices_goods.gamble_item(conan.get_backpack().show_topmost(),
                                      maurices_goods.get_items()[0], conan):
            print("Gamble Successful!")
        else:
            print("Gamble Failed!")
        print("Conan's topmost item:")
        print(conan.get_backpack().show_topmost())


if __name__ == "__main__":
    StoneAge.main()

