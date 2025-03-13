from item import Item

class Suitcase:
    def __init__(self, maxWeight:int):
        self.__maxWeight = maxWeight
        self.__items:list = []

    @property
    def weight(self):
        return sum(item.weight for item in self.__items)

    def add_item(self, item:Item):
        if self.weight + item.weight < self.__maxWeight:
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        return max(self.__items, key=lambda item: item.weight)

    def __str__(self):
        if len(self.__items) == 1:
            return f"1 item ({self.weight} kg)"
        else:
            return f"{len(self.__items)} items ({self.weight} kg)"


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

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight
    print(f"Combined weight: {combined_weight} g")

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")

if __name__ == "__main__":
    main()