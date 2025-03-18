from animal import Animal

class Bird(Animal):

    def __init__(self):
        Animal.__init__(self, 2)

    def make_sound(self):
        print("*clear bird singing*")
        