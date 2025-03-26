from wolf import Wolf
from animal import Animal
from trick import Trick

class Dog(Wolf):
    def __init__(self, name):
        Wolf.__init__(self, "Human Owners")
        self.name = name
        self.__learned_tricks:list = []

    @Animal.require_alive
    def make_sound(self):
        print(f"{self.name}: *woof*")

    @Animal.require_alive
    def teach_trick(self, trick:Trick):
        self.__learned_tricks.append(trick)

    @property
    def tricks(self):
        return [trick.action for trick in self.__learned_tricks]

    @Animal.require_alive
    def do_trick(self, trick:Trick):
        if trick in self.__learned_tricks:
            success = trick.perform()
        else:
            print(f"{self.name} has not learned to {trick.action}")
            return

        if success:
            print(f"{self.name} does the trick: {trick.action}")
        else:
            print(f"{self.name} doesn't feel like doing the trick: {trick.action}")