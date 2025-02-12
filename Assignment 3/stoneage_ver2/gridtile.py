import pygame

class GridTile:
    def __init__(self, x_coordinate:int, y_coordinate:int):
        self.__x = x_coordinate
        self.__y = y_coordinate
        self.__image:pygame.Surface = pygame.image.load(".\\game_assets\\gridtile.png")
        self.__rect:pygame.Rect = self.__image.get_rect()

        self.initialize_place()

    def initialize_place(self):
        self.__rect.x = (self.__x - 1) * 32
        self.__rect.y = (self.__y - 1) * 32

    def blit(self, game):
        game.get_screen().blit(self.__image, self.__rect)

    def get_coordinates(self):
        return self.__rect.topleft

    def get_simple_coordinates(self):
        return self.__x, self.__y