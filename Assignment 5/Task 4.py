class Computer:
    def __init__(self, model, speed):
        self.__model = model
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @property
    def model(self):
        return self.__model

class LaptopComputer(Computer):
    def __init__(self, model, speed, weight):
        super().__init__(model, speed)
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.model}, {self.speed} MHz, {self.weight} kg"

def main():
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
    print(laptop)

if __name__ == "__main__":
    main()