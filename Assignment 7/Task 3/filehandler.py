class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers

        return names


    def save_file(self, phonebook: list):
        with open(self.__filename, "w") as f:
            for person in phonebook:
                line = [person.name] + person.numbers
                f.write(";".join(line) + "\n")