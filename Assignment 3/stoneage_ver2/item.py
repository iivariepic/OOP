import pygame
from gridtile import GridTile

class Item:
    """
        Models a general item in an adventure game.
    
        Copyright: Sami Pyöttilä, 2006
    """

    def __init__(self, name, value, volume, damage, max_durability):
        """ Initializes a new item.

            Arguments:
            name : the name of the item
            value : the value of the item in money
            volume : the volume of the item for storage
            damage : the damage the item can cause, e.g., when used as a weapon
            max_durability : the maximum durability of the item when fully intact

            Preconditions: 
            (name is not None) and (len(name) > 0) and 
            (value > 0.0) and (volume > 0.0) and (damage > 0.0) and (max_durability > 0.0)
        """
        self.__name = name
        self.__value = value
        self.__volume = volume
        self.__damage = damage
        self.__max_durability = max_durability
        self.__durability = max_durability
        self.__is_on_ground: bool = False

        self.__image = None
        self.__rect = None
        self.__inside_tile = None


    def is_functional(self):
        """ Is the item still in working condition?
            Preconditions: True
        """
        return self.__durability > 0.0

    def get_damage(self):
        """ Returns the damage value.
            Preconditions: True
        """
        return self.__damage

    def get_max_durability(self):
        """ Returns the maximum durability when intact.
            Preconditions: True
        """
        return self.__max_durability

    def get_volume(self):
        """ Returns the volume.
            Preconditions: True
        """
        return self.__volume

    def get_value(self):
        """ Returns the value.
            Preconditions: True 
        """
        return self.__value

    def get_name(self):
        """ Returns the name.
            Preconditions: True
        """
        return self.__name

    def __str__(self):
        """ Returns a string representation of the item.
            Preconditions: True
        """
        return f"{self.__class__.__name__}: [{self.__name} {self.__value} {self.__volume} {self.__damage} ({self.__durability} / {self.__max_durability})]"

    def repair(self):
        """ Repairs the item to full durability.
            Preconditions: True
        """
        self.__durability = self.__max_durability

    # Game processing
    def initialize_game(self):
        self.__image: pygame.Surface = pygame.image.load(".\\game_assets\\item.png").convert_alpha()
        self.__rect: pygame.Rect = self.__image.get_rect()
        self.__inside_tile: GridTile = None

    def blit(self, game):
        if self.__is_on_ground:
            game.get_screen().blit(self.__image, self.__rect)

    def __set_coordinates(self, coordinates: tuple[int, int]):
        self.__rect.topleft = coordinates

    def get_picked_up(self):
        self.__is_on_ground = False

    def set_inside_tile(self, tile: GridTile):
        self.__inside_tile = tile
        self.__is_on_ground = True
        self.__set_coordinates(self.__inside_tile.get_coordinates())

    def get_inside_tile(self):
        return self.__inside_tile