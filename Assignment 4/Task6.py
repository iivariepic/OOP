class Present:
    def __init__(self, name:str, weight:int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight})"

class Box:
    def __init__(self, initial_presents:list[Present] = None):
        if initial_presents is None:
            initial_presents = []
        self.presents:list[Present] = initial_presents

    def add_present(self, present:Present) -> None:
        self.presents.append(present)
        return

    def total_weight(self) -> int:
        return sum(present.weight for present in self.presents)


def main():
    book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present:", book)

    box = Box()
    box.add_present(book)
    print(box.total_weight())
    cd = Present("Pink Floyd: Dark Side of the Moon", 50)
    box.add_present(cd)
    print(box.total_weight())

if __name__ == "__main__":
    main()