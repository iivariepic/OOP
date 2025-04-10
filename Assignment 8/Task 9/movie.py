from item import Item

class Movie(Item):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.__director = director

    @property
    def director(self):
        return self.__director

    @property
    def description(self):
        description = super().description()
        return description + f", Director {self.director}"

    def update_info(self, **kwargs):
        super().update_info(**kwargs)
        if kwargs["director"]:
            self.__director = kwargs["director"]
