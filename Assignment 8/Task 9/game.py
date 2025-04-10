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

    def update_info(self, **kwargs):
        super().update_info(**kwargs)
        if kwargs["developer"]:
            self.__developer = kwargs["developer"]