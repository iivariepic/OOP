class Item:
    def __init__(self, title, year):
        # Initialize the item with various attributes
        self.__title = title
        self.__year = year

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @property
    def description(self):
        return f"Title: {self.title}, Year: {self.year}"

    def update_info(self, **kwargs):
        if kwargs['title']:
            self.__title = kwargs['title']
        if kwargs['year']:
            self.__year = kwargs['year']