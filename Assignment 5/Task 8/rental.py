from check_input import check_input

class Rental:
    def __init__(self, rent: float, utilities: float, furnished: bool):
        self.rent = rent
        self.utilities = utilities
        self.furnished = furnished

    @classmethod
    def prompt_init(cls):
        def prompt_for_float(prompt_text: str) -> float:
            while True:
                value = input(prompt_text)
                if check_input(value, float):
                    return float(value)
                print("Invalid input, please enter a numeric value.")

        def prompt_for_bool(prompt_text: str) -> bool:
            while True:
                value = input(prompt_text).casefold()
                if check_input(value, check_text=True, target_texts=["yes", "no"]):
                    if value == "yes":
                        return True
                    if value == "no":
                        return False
                print("Invalid input, please enter yes or no.")

        rent = prompt_for_float("What is the monthly rent? ")
        utilities = prompt_for_float("What are the estimated utilities? ")
        furnished = prompt_for_bool("Is the property furnished? (yes/no) ")

        return {'rent': rent, 'utilities': utilities, 'furnished': furnished}

    def display(self):
        display_data = f"""
        PURCHASE DETAILS
        ================
        Rent: {self.rent}
        Estimated utilities: {self.utilities}
        Furnished: {"▣" if self.furnished else "□"}""".split("\n")
        for line in display_data[1:]:
            print(line.lstrip())

def main():
    rental_details = Rental.prompt_init()
    print(rental_details)
    rental = Rental(**rental_details)
    rental.display()


if __name__ == '__main__':
    main()