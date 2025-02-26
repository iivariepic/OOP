class  NumberStats:
    def __init__(self):
        #no need to add any new varibales here, just change the
        #initialization of the self.numbers variable.
        self.__numbers:list[int] = []

    def add_number(self, number:int):
        self.__numbers.append(number)

    def count_numbers(self):
        return len(self.__numbers)

    def get_sum(self):
        return sum(self.__numbers)

    def average(self):
        return sum(self.__numbers) / len(self.__numbers)

if __name__ == "__main__":
    #Part 1 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    #Part 2 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())