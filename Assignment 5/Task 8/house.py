from property import Property
from check_input import check_input

class House(Property):
    def __init__(self, square_feet: float, num_bedrooms: int, num_bathrooms: int,
                 num_stories:int, garage:bool, fenced_yard:bool):
        super().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard

    @classmethod
    def prompt_init(cls):
        init = super().prompt_init()

        init.update({
        "num_stories": cls.get_valid_input("Enter the number of stories: ", int),
        "garage": cls.convert_to_bool(
            cls.get_valid_input("Does the house have a garage? (yes/no) ", str, ["yes", "no"])),
        "fenced_yard": cls.convert_to_bool(
            cls.get_valid_input("Does the house have a fenced yard? (yes/no) ", str, ["yes", "no"])),
        })
        return init

    def display(self):
        super().display()
        added_data = f"""
        Number of bedrooms: {self.num_bedrooms}
        Garage: {"▣" if self.garage else "□"}
        Fenced Yard: {"▣" if self.fenced_yard else "□"}""".split("\n")
        for line in added_data[1:]:
            print(line.lstrip())

def main():
    house_details = House.prompt_init()
    print(house_details)
    house = House(**house_details)
    house.display()

if __name__ == "__main__":
    main()