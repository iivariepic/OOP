
from item import Item
from character import Character
from backpack import Backpack
from shop import Shop


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
    def sell_transaction(item_to_sell:Item, seller:Character, shop:Shop):
        seller_backpack:Backpack = seller.get_backpack()

        # Rummage through the backpack for the item
        if seller_backpack.contains(item_to_sell):
            while True:
                if seller_backpack.show_topmost() == item_to_sell:
                    seller_backpack.remove_topmost()
                    break
                else:
                    seller_backpack.rummage()

        else:
            raise ValueError(f'Item not found on player: {item_to_sell}')


        seller.give_item(shop.get_keeper(), item_to_sell)
        shop.get_items_from_shopkeeper()

    @staticmethod
    def buy_transaction(item_to_buy:Item, buyer:Character, shop:Shop):

        if not buyer.enough_money(item_to_buy.get_value()):
            raise ValueError("Not Enough Money!")

        if not buyer.has_free_hand():
            raise ValueError("Buyer does not have a free hand!")

        shop.make_shopkeeper_grab_item(item_to_buy)
        shop.get_keeper().give_item(buyer, item_to_buy)
        buyer.get_backpack().put(item_to_buy)


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
 
        if (small_axe.get_volume() < leather_backpack.get_remaining_capacity()):
            leather_backpack.put(small_axe)

        print(leather_backpack.__str__())
        print(leather_backpack.is_empty())
        
        conan = Character("Conan", 20.0, 30.0, 15.0)
        jay = Character("Jay", 30.0, 20.0, 17.0)
        maurice = Character("Maurice", 100.0, 100.0, 100.0)
        maurices_goods = Shop(maurice)
        maurices_goods.add_item(gold_chain)

        conan.set_backpack(leather_backpack)
        leather_backpack.put(stone)
        print(conan)
        print("\nMAURICE'S GOODS:")
        maurices_goods.print_items()

        StoneAge.sell_transaction(small_axe, conan, maurices_goods)


        print("\nMAURICE'S GOODS:")
        maurices_goods.print_items()

        conan.change_money(40000.0)
        StoneAge.buy_transaction(gold_chain, conan, maurices_goods)

        print(conan.get_backpack().show_topmost())


if __name__ == "__main__":
    StoneAge.main()

