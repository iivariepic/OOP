import pygame
from game_popup_options import GamePopupOption

class GamePopup:

    def __init__(self, game):
        self.__game = game
        self.__image: pygame.Surface = pygame.image.load(".\\game_assets\\popup_bg.png")
        self.__header_text = None
        self.__header_text_rect = None
        self.__options:list[GamePopupOption] = []

    def set_text(self, text:str):
        text_font = pygame.font.SysFont('Posterama', 30)
        self.__header_text = text_font.render(text, True, (255, 0, 0))
        self.__header_text_rect = self.__name_text.get_rect()
        self.__header_text_rect.centerx = self.__game.get_screen().get_rect().centerx
        self.__header_text_rect.top = 3

    def add_option(self, option_text:str, option_function):
        new_option = GamePopupOption(option_text, option_function)
        self.__options.append(new_option)
        option_x = self.__game.get_screen().get_rect().centerx
        option_y = self.__header_text_rect.bottom + 3
        if len(self.__options) > 0:
            option_y = self.__options[-1].get_rect().bottom + 3

    def blit(self):
        self.__game.get_screen().blit(self.__image, self.__header_text_rect)

    def blit_option(self, option:GamePopupOption):
        self.__game.get_screen().blit(option.image, self.__header_text_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pg.KEYDOWN and event.unicode.isdigit():
                    return self.__options[int(event.unicode) - 1].get_function()

            self.blit()
            for option in self.__options:
                self.blit_option(option)

            pygame.display.flip()