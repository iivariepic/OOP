import pygame

class GamePopupOption:
    def __init__(self, text, function):
        text_font = pygame.font.SysFont('Posterama', 24)
        self.__text = text_font.render(text, True, (255, 0, 0))
        self.__text_rect = self.__name_text.get_rect()
        self.__function = function

    def set_position(self, coordinates: tuple[int, int]):
        self.__text_rect.topleft = coordinates

    def get_rect(self):
        return self.__text_rect

    def get_function(self):
        return self.__function

    def set_text(self, text: str):
        text_font = pygame.font.SysFont('Posterama', 24)
        self.__text = text_font.render(text, True, (255, 0, 0))
        self.__text_rect = self.__name_text.get_rect()