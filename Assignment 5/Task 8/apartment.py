from property import Property
from check_input import check_input

class Apartment(Property):
    def __init__(self, square_feet: float, num_bedrooms: int, num_bathrooms: int, balcony: bool, laundry: bool):
        super().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.balcony = balcony
        self.laundry = laundry

    @staticmethod
    def convert_to_bool(string:str) -> bool:
        if string == "yes":
            return True
        elif string == "no":
            return False
        else:
            raise ValueError("String must be either 'yes' or 'no'")

    @classmethod
    def prompt_init(cls):
        init = super().prompt_init()
        balcony = cls.get_valid_input("Does the apartment have a balcony? (yes/no) ", str, ["yes", "no"])
        laundry = cls.get_valid_input("Does the apartment have a laundry? (yes/no) ", str, ["yes", "no"])

        balcony = cls.convert_to_bool(balcony)
        laundry = cls.convert_to_bool(laundry)

        init.update({
            "balcony": balcony,
            "laundry": laundry
        })
        return init

    def display(self):
        super().display()
        added_data = f"""
        Balcony: {"▣" if self.balcony else "□"}
        Laundry: {"▣" if self.laundry else "□"}""".split("\n")
        for line in added_data[1:]:
            print(line.lstrip())

def main():
    apartment_details = Apartment.prompt_init()
    print(apartment_details)
    apartment = Apartment(**apartment_details)
    apartment.display()

if __name__ == "__main__":
    main()