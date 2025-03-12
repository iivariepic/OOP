from suitcase import Suitcase
from item import Item

class CargoHold:
    def __init__(self, maxWeight:float):
        self.__maxWeight:float = maxWeight
        self.__suitcases:list = []

    @property
    def weight(self):
        weight_in_g = sum(suitcase.weight for suitcase in self.__suitcases)
        weight_in_kg:float = weight_in_g / 1000
        return weight_in_kg

    def remaining_weight(self):
        return self.__maxWeight - self.weight

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight + suitcase.weight/1000 < self.__maxWeight:
            self.__suitcases.append(suitcase)

    def __str__(self):
        if len(self.__suitcases) == 1:
            return f"1 suitcase, space for {self.remaining_weight()} kg"
        else:
            return f"{len(self.__suitcases)} suitcases, space for {self.remaining_weight()} kg"

def main():
    cargo_hold = CargoHold(100)
    print(cargo_hold)
    book = Item("ABC Book", 200)
    phone = Item("Nokia 3210", 100)
    brick = Item("Brick", 400)
    adas_suitcase = Suitcase(1000)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)
    peters_suitcase = Suitcase(1000)
    peters_suitcase.add_item(brick)
    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)
    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)

if __name__ == "__main__":
    main()