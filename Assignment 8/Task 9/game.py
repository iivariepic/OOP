from item import Item

class Game(Item):
    def __init__(self, title, year, developer:str):
        super().__init__(title, year)
        self.__developer = developer

    @property
    def developer(self):
        return self.__developer

    @property
    def description(self):
        description = super().description()
        return description + f", Developer {self.developer}"