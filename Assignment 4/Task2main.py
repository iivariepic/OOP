from Task2 import NumberStats
def check_input_validity(userInput:str, desiredType:type = int):
    try:
        desiredType(userInput)
        return True
    except ValueError:
        return False

def is_even(number:int):
    return number % 2 == 0

def main():
    all_numbers = NumberStats()
    even_numbers = NumberStats()
    odd_numbers = NumberStats()

    while True:
        userInput = input("Enter an integer: ")

        # Check input validity
        if not check_input_validity(userInput):
            print("Please enter an integer")
            continue

        # Convert to int
        userInput = int(userInput)

        if userInput == -1:
            break

        # Add numbers to different stats based on evenness
        if is_even(userInput):
            even_numbers.add_number(userInput)
        else:
            odd_numbers.add_number(userInput)

        # Add all numbers to the main list
        all_numbers.add_number(userInput)

    print(f"Sum of numbers: {all_numbers.get_sum()}")
    print(f"Mean of numbers: {all_numbers.average()}")
    print(f"Sum of even numbers: {even_numbers.get_sum()}")
    print(f"Sum of odd numbers: {odd_numbers.get_sum()}")


if __name__ == '__main__':
    main()