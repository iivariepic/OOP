from check_input import check_input

class Purchase:
    def __init__(self, price: float, taxes: float):
        self.price = price
        self.taxes = taxes

    @classmethod
    def prompt_init(cls):
        def prompt_for_value(prompt_text: str) -> float:
            while True:
                value = input(prompt_text)
                if check_input(value, float):
                    return float(value)
                print("Invalid input, please enter a numeric value.")

        price = prompt_for_value("What is the selling price? ")
        taxes = prompt_for_value("What are the estimated taxes? ")

        return {'price': price, 'taxes': taxes}

    def display(self):
        display_data = f"""
        PURCHASE DETAILS
        ================
        Selling price: {self.price}
        Estimated taxes: {self.taxes}""".split("\n")
        for line in display_data[1:]:
            print(line.lstrip())

def main():
    purchase_details = Purchase.prompt_init()
    print(purchase_details)
    purchase = Purchase(**purchase_details)
    purchase.display()

if __name__ == '__main__':
    main()