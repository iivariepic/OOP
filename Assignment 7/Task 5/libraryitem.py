class LibraryItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__is_available:bool = True