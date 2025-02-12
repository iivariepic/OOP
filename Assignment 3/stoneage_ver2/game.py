import sys
import pygame
from pygame.locals import *
from item import Item
from character import Character
from backpack import Backpack
from shop import Shop
from gridtile import GridTile


class Game:
    def __init__(self):
        # Setting up pygame
        pygame.init()

        self.__fps = 60
        self.__fps_clock = pygame.time.Clock()

        width, height = 512, 512
        self.__screen = pygame.display.set_mode((width, height))

        # Setting up the grid
        self.__grid: list[GridTile] = Game.create_grid()

        # Setting up the characters
        conan = Character("Conan", 20.0, 20.0, 20.0)
        maurice = Character("Maurice", 10.0, 10.0, 10.0)
        self.__characters: list[Character] = [conan, maurice]
        self.__player_character: Character = conan
        for character in self.__characters:
            character.initialize_game()
        conan.set_inside_tile(self.__grid[1], self.__screen)

        # Setting up the items
        stone = Item("Stone", 0.0, 20.0, 10.0, 100.0)
        jewel = Item("Jewel", 100.0, 50.0, 5.0, 200.0)
        spear = Item("Spear", 20.0, 50.0, 5.0, 200.0)
        self.__items: list[Item] = [stone, jewel, spear]
        for item in self.__items:
            item.initialize_game()

        stone_tile = Game.get_tile_with_coordinates(self.__grid, (3, 13))
        jewel_tile = Game.get_tile_with_coordinates(self.__grid, (15, 4))
        stone.set_inside_tile(stone_tile)
        jewel.set_inside_tile(jewel_tile)

        # Setting up the shop
        maurices_goods = Shop(maurice)
        self.__shops: list[Shop] = [maurices_goods]
        for shop in self.__shops:
            shop.initialize_game()
        maurice_tile = Game.get_tile_with_coordinates(self.__grid, (10, 7))
        maurices_goods.set_inside_tile(maurice_tile)
        maurice.set_inside_tile(maurices_goods.get_inside_tile(), self.__screen)
        maurices_goods.add_item(spear)

        # Setting up the text box
        self.__font = pygame.font.SysFont("Posterama", 20)
        self.__info_text:pygame.Surface = None
        self.__info_text_rect:pygame.Rect = None
        self.__info_text_countdown = 0
        self.set_info_text("Game Start")


    @staticmethod
    def create_grid():
        gridtile_list:list[GridTile] = []
        for x_coordinate in range(1, 17):
            for y_coordinate in range(1, 17):
                gridtile_list.append(GridTile(x_coordinate, y_coordinate))

        return gridtile_list

    @staticmethod
    def get_tile_with_coordinates(tile_list, coordinates: tuple[int, int]):
        for tile in tile_list:
            if tile.get_simple_coordinates() == coordinates:
                return tile

    def set_info_text(self, info_text: str, countdown_frames:int = 60 * 3):
        self.__info_text = self.__font.render(info_text, True, (255, 0, 0))
        self.__info_text_rect = self.__info_text.get_rect()
        self.__info_text_rect.centerx = self.__screen.get_rect().centerx
        self.__info_text_rect.top = self.__screen.get_rect().top + 3
        self.__info_text_countdown = countdown_frames

    def run(self):
        # Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    self.__player_character.process_input(event.key, self.__grid, self.__screen)

            # Update Things
            for character in self.__characters:
                character.update()

            # Blit images
            for tile in self.__grid:
                tile.blit(self.__screen)
            for item in self.__items:
                item.blit(self.__screen)
            for character in self.__characters:
                character.blit(self.__screen)
            for shop in self.__shops:
                shop.blit(self.__screen)

            # Blit info text
            if self.__info_text_countdown != 0:
                self.__info_text_countdown -= 1
                self.__screen.blit(self.__info_text, self.__info_text_rect)

            pygame.display.flip()
            self.__fps_clock.tick(self.__fps)

if __name__ == '__main__':
    new_game = Game()
    new_game.run()