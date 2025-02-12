from item import Item
from shop import Shop
import pygame

class GridTile:
    def __init__(self, x_coordinate:int, y_coordinate:int):
        self.__x = x_coordinate
        self.__y = y_coordinate
        self.__item:Item = None
        self.__shop:Shop = None
        self.__image:pygame.Surface = pygame.image.load(".\\game_assets\\gridtile.png")
        self.__rect:pygame.Rect = self.__image.get_rect()

        self.initialize_place()

    def set_item(self, item:Item):
        self.__item = item

    def get_item(self):
        return self.__item

    def set_shop(self, shop:Shop):
        self.__shop = shop

    def get_shop(self):
        return self.__shop

    def initialize_place(self):
        self.__rect.x = (self.__x - 1) * 32
        self.__rect.y = (self.__y - 1) * 32

    def blit(self, screen:pygame.Surface):
        screen.blit(self.__image, self.__rect)

    def get_coordinates(self):
        return self.__rect.topleft