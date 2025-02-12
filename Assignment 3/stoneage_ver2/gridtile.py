from item import Item
from shop import Shop

class GridTile:
    def __init__(self, x_coordinate:int, y_coordinate:int):
        self.__x = x_coordinate
        self.__y = y_coordinate
        self.__item:Item = None
        self.__shop:Shop = None

    def set_item(self, item:Item):
        self.__item = item

    def get_item(self):
        return self.__item

    def set_shop(self, shop:Shop):
        self.__shop = shop

    def get_shop(self):
        return self.__shop