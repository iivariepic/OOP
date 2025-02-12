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
    def run():
        pygame.init()

        fps = 60
        fpsClock = pygame.time.Clock()

        width, height = 512, 512
        screen = pygame.display.set_mode((width, height))

        grid:list[GridTile] = Game.create_grid()
        conan = Character("Conan", 20.0, 20.0, 20.0)
        conan.initialize_game()
        conan.set_inside_tile(grid[0], screen)

        # Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    conan.process_input(event.key, grid, screen)

            # Update Things
            conan.update()

            # Blit images
            for tile in grid:
                tile.blit(screen)
            conan.blit(screen)

            pygame.display.flip()
            fpsClock.tick(fps)

if __name__ == '__main__':
    Game.run()