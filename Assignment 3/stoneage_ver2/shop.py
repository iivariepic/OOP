from character import Character
from item import Item

class Shop:
    def __init__(self, shopkeeper:Character, initial_items:list[Item] = []):
        self.__shopkeeper:Character = shopkeeper
        self.__items:list[Item] = initial_items

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