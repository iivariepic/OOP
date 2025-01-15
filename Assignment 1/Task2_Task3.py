# Task 2
print("Task 2")
integer_list:list = []
string_list:list = []

# Filling with user inputs
def input_to_list(target:list, target_type:type):
    # Function to fill a list with user inputs with the target type
    result = input(f"Please enter an input of type {target_type.__name__}: ")
    while True:
        is_valid = check_input(result, target_type)
        if is_valid:
            target.append(target_type(result))
            print("Input successful.")
            break
        else:
            result = input(f"Input is not a valid {target_type.__name__}. Enter valid input: ")

def check_input(target:str, target_type:type):
    # Check if input matches the target type
    try:
        target_type(target)
        return True
    except ValueError:
        return False

def fill_list(target:list, target_type:type, amount:int = 10):
    # Function to fill a list with "amount" elements
    for i in range(amount):
        print(f"Input {i+1}/{amount}")
        input_to_list(target, target_type)

print("Filling integer list:")
fill_list(integer_list, int)
print("Filling string list:")
fill_list(string_list, str)
print("Integer list:", integer_list)
print("String list:", string_list)

# Filling with random numbers
input("Press Enter to Continue...")
import random

print("Filling integer list with random numbers")
for x in range(10):
    integer_list.append(random.randint(0,100))
print("Here's the list now:", integer_list)

# Task 3
input("Press Enter to Continue...")
print("Task 3")

sorted_integer_list = sorted(integer_list)
sorted_string_list = sorted(string_list)
print("Integer list sorted:", sorted_integer_list)
print("String list sorted:", sorted_string_list)