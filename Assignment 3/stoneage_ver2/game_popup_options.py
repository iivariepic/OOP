import pygame

class GamePopupOption:
    def __init__(self, text, number):
        text_font = pygame.font.SysFont('Posterama', 24)
        self.__text = text_font.render(text, True, (255, 255, 255))
        self.__text_rect = self.__text.get_rect()
        self.__number = number

    def set_position(self, coordinates: tuple[int, int]):
        self.__text_rect.topleft = coordinates

    def get_rect(self):
        return self.__text_rect

    def get_text(self):
        return self.__text

    def get_number(self):
        return self.__number

    def set_text(self, text: str):
        text_font = pygame.font.SysFont('Posterama', 24)
        self.__text = text_font.render(text, True, (255, 255, 255))
        self.__text_rect = self.__name_text.get_rect()