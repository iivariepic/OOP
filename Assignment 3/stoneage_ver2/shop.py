import random
from character import Character
from item import Item
import pygame

class Shop:
    def __init__(self, shopkeeper:Character, initial_items:list[Item] = []):
        self.__shopkeeper:Character = shopkeeper
        self.__items:list[Item] = initial_items

        self.__image = None
        self.__rect = None
        self.__inside_tile = None

    def add_item(self, item:Item):
        self.__items.append(item)

    def remove_item(self, item:Item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            raise ValueError(f'Item {item} not found in shop')

    def get_items_from_shopkeeper(self):
        # Function to empty the shopkeepers hands into the shop
        left_hand = self.__shopkeeper.get_left_hand_item()
        right_hand = self.__shopkeeper.get_right_hand_item()

        if left_hand:
            self.add_item(left_hand)
            self.__shopkeeper.set_left_hand(None)

        if right_hand:
            self.add_item(right_hand)
            self.__shopkeeper.set_right_hand(None)


    def make_shopkeeper_grab_item(self, item:Item):
        # Function to make a shopkeeper grab an item from the shop
        if item not in self.__items:
            raise ValueError(f'Item {item} not found in shop')

        if not self.__shopkeeper.has_free_hand():
            raise ValueError('Shopkeeper has no free hand')

        self.__shopkeeper.set_free_hand(item)

    def get_items(self):
        return self.__items

    def get_keeper(self):
        return self.__shopkeeper

    def print_items(self):
        for item in self.get_items():
            print(f"{item.get_name()}: {item.get_value()}")

    def sell_transaction(self, item_to_sell:Item, seller:Character):
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


        seller.give_item(self.get_keeper(), item_to_sell)
        self.get_items_from_shopkeeper()

    def buy_transaction(self, item_to_buy:Item, buyer:Character):

        if not buyer.enough_money(item_to_buy.get_value()):
            raise ValueError("Not Enough Money!")

        if not buyer.has_free_hand():
            raise ValueError("Buyer does not have a free hand!")

        self.make_shopkeeper_grab_item(item_to_buy)
        buyer.change_money(-item_to_buy.get_value())
        self.get_keeper().give_item(buyer, item_to_buy)
        buyer.get_backpack().put(item_to_buy)

        # Remove the item from the buyers hand
        buyer.remove_item_from_hand(item_to_buy)

    def gamble_item(self, gambler_item:Item, target_item:Item, gambler:Character) -> bool:
        """Gamble an item for an item in the shop, returns boolean value based on
        the success of the gamble"""

        odds:float = gambler_item.get_value() / target_item.get_value() * 100
        if odds >= 75:
            odds = 75

        if random.randrange(0, 100) <= odds:
            gambler.give_item(self.__shopkeeper, gambler_item)

            self.make_shopkeeper_grab_item(target_item)
            self.__shopkeeper.give_item(gambler, target_item)
            self.get_items_from_shopkeeper()

            gambler.remove_item_from_hand(target_item)
            gambler.get_backpack().put(target_item)
            return True

        return False

    # Game processing
    def initialize_game(self):
        self.__image: pygame.Surface = pygame.image.load(".\\game_assets\\shop.png").convert_alpha()
        self.__rect: pygame.Rect = self.__image.get_rect()
        self.__inside_tile: GridTile = None

    def blit(self, screen:pygame.Surface):
        screen.blit(self.__image, self.__rect)

    def __set_coordinates(self, coordinates:tuple[int, int]):
        self.__rect.topleft = coordinates

    def set_inside_tile(self, tile):
        self.__inside_tile = tile
        self.__set_coordinates(tile.get_coordinates())

    def get_inside_tile(self):
        return self.__inside_tile