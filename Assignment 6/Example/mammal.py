from animal import Animal

class Mammal(Animal):

    def __init__(self):
        Animal.__init__(self, 4)

    def make_sound(self): 
        print("*mammal breathing*")
        