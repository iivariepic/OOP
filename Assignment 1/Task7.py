def generate_AP(max):
    # Function to create an arithmetic progression until the max value
    if max < 3:
        return []

    result = [3]
    while True:
        new_number = result[-1] + 3
        if new_number > max:
            break
        result.append(new_number)

    return result


def sum_of_squares(target:list[int]):
    # Function to return the sum of terms squared of an integer list
    result = 0
    for number in target:
        result += number ** 2
    return result

def check_input(target:str, target_type:type):
    # Check if input matches the target type
    try:
        target_type(target)
        return True
    except ValueError:
        return False

def main():
    max_value = input("Please enter the max value of the AP: ")
    while True:
        is_valid = check_input(max_value, int)
        if is_valid:
            break
        max_value = input("Invalid input, Please enter an integer: ")

    AP = generate_AP(int(max_value))
    square_sum = sum_of_squares(AP)

    print("Number of terms:", len(AP))
    print("Sum of terms:", sum(AP))
    print("Sum of the square of the terms:", square_sum)


if __name__ == '__main__':
    main()