from item import Item

class Movie(Item):
    def __init__(self, title, year, artist):
        super().__init__(title, year)
        self.__artist = artist

    @property
    def artist(self):
        return self.__artist

    @property
    def description(self):
        description = super().description()
        return description + f", Artist {self.artist}"