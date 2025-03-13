from check_input import check_input

class Property:
    def __init__(self, square_feet:float, num_bedrooms:int, num_bathrooms: int):
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms

    @staticmethod
    def get_valid_input(prompt: str, input_type: type, text_options:list[str] = None):
        # Function to handle processing the user input and ask for reinput if it's not valid

        while True:
            user_input = input(prompt).casefold()

            # Handle case where text_options are provided
            if text_options:
                if check_input(user_input, input_type, True, text_options):
                    return input_type(user_input)
                print(f'Invalid input. Choose from the following options: {", ".join(text_options)}')
                continue

            # Handle case without text_options
            elif check_input(user_input, input_type):
                return input_type(user_input)

            print(f'Invalid input, input needs to be of type {input_type.__name__}')

    @classmethod
    def prompt_init(cls):
        # Prompts the user for the details and returns a dictionary with the data
        return {
            "square_feet": cls.get_valid_input("Enter square feet: ", float),
            "num_bedrooms": cls.get_valid_input("Enter the number of bedrooms: ", int),
            "num_bathrooms": cls.get_valid_input("Enter the number of bathrooms: ", int)
        }

    def display(self):
        display_data = f"""
        PROPERTY DETAILS
        ================
        Square feet: {self.square_feet}
        Number of bedrooms: {self.num_bedrooms}
        Number of bathrooms: {self.num_bathrooms}""".split("\n")
        for line in display_data[1:]:
            print(line.lstrip())

def main():
    property_details = Property.prompt_init()
    print(property_details)
    property = Property(**property_details)
    property.display()

if __name__ == "__main__":
    main()