import pygame, sys
from game_popup_options import GamePopupOption

class GamePopup:

    def __init__(self, game):
        self.__game = game
        self.__image: pygame.Surface = pygame.image.load(".\\game_assets\\popup_bg.png")

        text_font = pygame.font.SysFont('Posterama', 30)
        self.__header_text = text_font.render("Default", True, (255, 255, 255))
        self.__header_text_rect = self.__header_text.get_rect()
        self.__options:list[GamePopupOption] = []

    def set_text(self, text:str):
        text_font = pygame.font.SysFont('Posterama', 30)
        self.__header_text = text_font.render(text, True, (255, 255, 255))
        self.__header_text_rect = self.__header_text.get_rect()
        self.__header_text_rect.centerx = self.__game.get_screen().get_rect().centerx
        self.__header_text_rect.top = 3

    def add_option(self, option_text:str):
        option_number = len(self.__options) + 1
        option_text = f"{str(option_number)}. {option_text}"

        new_option = GamePopupOption(option_text, option_number)

        option_x = self.__game.get_screen().get_rect().centerx
        option_y = self.__header_text_rect.bottom + 10

        # If there are other options, move this one below it
        if len(self.__options) > 0:
            option_y = self.__options[-1].get_rect().bottom + 3

        new_option.get_rect().centerx = option_x
        new_option.get_rect().y = option_y

        self.__options.append(new_option)

    def blit(self):
        self.__game.get_screen().blit(self.__image, (0, 0))
        self.__game.get_screen().blit(self.__header_text, self.__header_text_rect)

    def blit_option(self, option:GamePopupOption):
        self.__game.get_screen().blit(option.get_text(), option.get_rect())

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.unicode.isdigit():
                    pressed_number = int(event.unicode)
                    if pressed_number <= len(self.__options):
                        return self.__options[int(event.unicode) - 1].get_number()

            self.blit()
            for option in self.__options:
                self.blit_option(option)

            pygame.display.flip()