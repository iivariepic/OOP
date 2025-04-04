from phonebook import PhoneBook
from filehandler import FileHandler

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 add address")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        if self.__phonebook.get_entry(name) is None:
            input("name not found in phonebook")
            return

        address = input("address: ")
        entry = self.__phonebook.get_entry(name)
        self.__phonebook.add_address(entry, address)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_number(name)
        if numbers is None:
            print("number unknown")
            return
        for number in numbers:
            print(number)


    # a method which gets executed as the program exits
    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":

                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

def main():
    app = PhoneBookApplication()
    app.execute()

if __name__ == "__main__":
    main()