class Person:
    def __init__(self, name):
        self.__name = name
        self.__numbers:list[str] = []
        self.__address:str | None = None

    @property
    def name(self):
        return self.__name

    @property
    def numbers(self):
        return self.__numbers

    @property
    def address(self):
        return self.__address

    def add_number(self, number:str):
        self.__numbers.append(number)

    def add_address(self, address:str):
        self.__address = address
