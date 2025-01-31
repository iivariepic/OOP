class Pet:
    def __init__(self, name:str, species:str, year_of_birth:int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

def new_pet(name:str, species:str, year_of_birth:int) -> Pet:
    return Pet(name, species, year_of_birth)

def main() -> None:
    doggy = new_pet("Doggy", "Cat", 1998)
    print(doggy.name, doggy.species, doggy.year_of_birth)

if __name__ == '__main__':
    main()