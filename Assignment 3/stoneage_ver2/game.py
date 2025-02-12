import sys
import pygame
from pygame.locals import *
from item import Item
from character import Character
from backpack import Backpack
from shop import Shop
from gridtile import GridTile


class Game:
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

    @staticmethod
    def run():
        # Setting up pygame
        pygame.init()

        fps = 60
        fps_clock = pygame.time.Clock()

        width, height = 512, 512
        screen = pygame.display.set_mode((width, height))

        # Setting up the grid
        grid:list[GridTile] = Game.create_grid()

        # Setting up the characters
        conan = Character("Conan", 20.0, 20.0, 20.0)
        maurice = Character("Maurice", 10.0, 10.0, 10.0)
        characters:list[Character] = [conan, maurice]
        player_character:Character = conan
        for character in characters:
            character.initialize_game()
        conan.set_inside_tile(grid[1], screen)

        # Setting up the shop
        maurices_goods = Shop(maurice)
        shops:list[Shop] = [maurices_goods]
        for shop in shops:
            shop.initialize_game()
        maurice_tile = Game.get_tile_with_coordinates(grid, (10, 7))
        maurices_goods.set_inside_tile(maurice_tile)
        maurice.set_inside_tile(maurices_goods.get_inside_tile(), screen)




        # Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    player_character.process_input(event.key, grid, screen)

            # Update Things
            for character in characters:
                character.update()

            # Blit images
            for tile in grid:
                tile.blit(screen)
            for character in characters:
                character.blit(screen)
            for shop in shops:
                shop.blit(screen)

            pygame.display.flip()
            fps_clock.tick(fps)

if __name__ == '__main__':
    Game.run()