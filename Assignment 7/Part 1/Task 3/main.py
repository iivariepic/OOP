from person import Person
from phonebook import PhoneBook

def main():
    person = Person("Eric")
    print(person.name)
    print(person.numbers)
    print(person.address)
    person.add_number("040-123456")
    person.add_address("Mannerheimintie 10 Helsinki")
    print(person.numbers)
    print(person.address)

    phonebook = PhoneBook()
    phonebook.add_number("Eric", "02-123456")
    print(phonebook.get_number("Eric"))
    print(phonebook.get_number("Emily"))

if __name__ == "__main__":
    main()