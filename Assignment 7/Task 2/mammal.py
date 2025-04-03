class Mammal:
    def __init__(self, ID:int, species:str, name:str,
                 size:float, weight:float):
        self.__ID = ID
        self.__species = species
        self.__name = name
        self.__size = size
        self.__weight = weight

    @property
    def ID(self):
        return self.__ID

    @property
    def species(self):
        return self.__species

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.name}: {self.species}, ({self.ID})"