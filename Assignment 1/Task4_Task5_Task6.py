# Task 4
def check_input(target:str, target_type:type):
    # Check if input matches the target type
    try:
        target_type(target)
        return True
    except ValueError:
        return False

def get_input():
    # Get an input and check if it's an integer
    user_input = input("Enter an integer or input 0 to exit: ")
    while True:
        is_valid = user_input == "0" or check_input(user_input, int)
        if is_valid:
            return int(user_input)

        user_input = input("Input not valid (integer), try again: ")

def calculate_negatives(target:list):
    # Calculate the amount of negative numbers in a list
    result = 0
    for number in target:
        if number < 0:
            result += 1

    return result

def main():
    input_list:list = []
    # Ask for user input until 0 is entered
    while True:
        user_input = get_input()
        if user_input == 0:
            break

        input_list.append(user_input)

    negatives = calculate_negatives(input_list)
    evens = calculate_evens(input_list)
    print(f"There were {negatives} negative numbers and {evens} even numbers in the list.")
    divisible_positives = calculate_positives_divisible_by_3(input_list)
    print(f"There were {divisible_positives} positive numbers that were divisible by 3 in the list.")

# Task 5
def calculate_evens(target:list):
    # Calculate the amount of even numbers in a list
    result = 0
    for number in target:
        if number % 2 == 0:
            result += 1
    return result

# Task 6
def calculate_positives_divisible_by_3(target:list):
    # Calculate the amount of positive numbers in a list divisible by 3
    result = 0
    for number in target:
        if number % 3 == 0 and number > 0:
            result += 1
    return result

if __name__ == "__main__":
    main()