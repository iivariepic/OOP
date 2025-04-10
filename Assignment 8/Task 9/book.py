from item import Item

class Book(Item):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.__author = author

    @property
    def author(self):
        return self.__author

    @property
    def description(self):
        description = super().description()
        return description + f", Author {self.author}"

    def update_info(self, **kwargs):
        super().update_info(**kwargs)
        if kwargs["author"]:
            self.__author = kwargs["author"]
