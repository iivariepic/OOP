class PhoneBookEntry:
    def __init__(self, name, number):
        self.name = name
        self.number = number

phone_book:list[PhoneBookEntry] = [] # List to keep track of the entries

def search_phonebook(query:str):
    # Searches the phone book for names containing the query
    # Returns a list of objects
    result:list[PhoneBookEntry] = []
    for entry in phone_book:
        if query.lower() in entry.name.lower():
            result.append(entry)

    return result

def make_search():
    # Function that asks the user for a query and displays the search results
    user_input = input("Please search a name: ")
    results = search_phonebook(user_input)
    print(f"{len(results)} entries found")
    for result in results:
        print(f"\nName: {result.name}")
        print(f"Number: {result.number}")

    input("Press Enter to Continue...")

def add_entry():
    # Function to add a phone book entry
    name = input("Please enter the name: ")
    number = input("Please enter the phone number: ")
    while True:
        is_valid = check_number_validity(number)
        if is_valid:
            phone_book.append(PhoneBookEntry(name, number))
            print("Entry Added Successfully.")
            input("Press Enter to Continue...")
            break

        number = input("Please enter a valid phone number: ")

def check_number_validity(number:str):
    # Function to check that a phone number only contains digits, dashes, pluses and spaces
    for character in number:
        if not (character.isdigit() or character in ["-", "+", " "]):
            return False

    return True

def main():
    print("Welcome to Digital Phone Book!")
    exit_program = False
    while not exit_program:
        print("""
Make A Selection!
1. Search for a name
2. Add an entry
3. Quit the app""")
        user_input = input()
        while True:
            if user_input == "1":
                make_search()
                break
            elif user_input == "2":
                add_entry()
                break
            elif user_input == "3":
                print("Quitting...")
                exit_program = True
                break
            else:
                input("Please enter a valid input!: ")

if __name__ == "__main__":
    main()