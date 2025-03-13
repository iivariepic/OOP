class Item:
    def __init__(self, name:str, weight:int):
        self.__name:str = name
        self.__weight:int = weight

    @property
    def name(self):
        return self.__name

    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.name} ({self.weight} g)"

def main():
    book = Item("ABC Book", 200)
    phone = Item("Nokia 3210", 100)
    print("Name of the book:", book.name)
    print("Weight of the book:", book.weight)
    print("Book:", book)
    print("Phone:", phone)

if __name__ == "__main__":
    main()