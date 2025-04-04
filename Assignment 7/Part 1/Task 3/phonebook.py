from person import Person

class PhoneBook:
    def __init__(self):
        self.__persons:list[Person] = []

    def add_number(self, name: str, number: str):
        if name not in ([person.name for person in self.__persons]):
            new_person = Person(name)
            new_person.add_number(number)
            self.__persons.append(new_person)

    def add_address(self, person:Person, address:str):
        if person not in self.__persons:
            raise ValueError("Person not in Phonebook")
        person.add_address(address)


    def get_number(self, name: str):
        if not name in ([person.name for person in self.__persons]):
            return None

        for person in self.__persons:
            if person.name == name:
                return person.numbers

    def get_entry(self, name: str):
        if not name in ([person.name for person in self.__persons]):
            return None

        for person in self.__persons:
            if person.name == name:
                return person

    # return all entries (in dictionary format)
    def all_entries(self):
        return self.__persons