from animal import Animal

class Mammal(Animal):

    def __init__(self):
        Animal.__init__(self, 4, 10)

    @Animal.require_alive
    def make_sound(self): 
        print("*mammal breathing*")
        