from libraryitem import LibraryItem

class Book(LibraryItem):
    def __init__(self, name, description, genre):
        super().__init__(name, description)
        self.genre = genre
