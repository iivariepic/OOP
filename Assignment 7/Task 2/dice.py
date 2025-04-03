import random

class Dice:
    options = [1, 2, 3, 4, 5, 6]

    def __init__(self):
        self.__sideup:int = 1

    def roll(self):
        self.__sideup = random.choice(Dice.options)

    @property
    def sideup(self):
        return self.__sideup