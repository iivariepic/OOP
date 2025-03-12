from item import Item

class Suitcase:
    def __init__(self, maxWeight:int):
        self.__maxWeight = maxWeight
        self.__items:list = []

    def __get_weight(self):
        return sum(item.weight for item in self.__items)

    def add_item(self, item:Item):
        if self.__get_weight() + item.weight < self.__maxWeight:
            self.__items.append(item)

    def __str__(self):
        return f"{len(self.__items)} items ({self.__get_weight()} kg)"


def main():
    book = Item("ABC Book", 200)
    phone = Item("Nokia 3210", 100)
    brick = Item("Brick", 400)
    suitcase = Suitcase(500)
    print(suitcase)
    suitcase.add_item(book)
    print(suitcase)
    suitcase.add_item(phone)
    print(suitcase)
    suitcase.add_item(brick)
    print(suitcase)

if __name__ == "__main__":
    main()