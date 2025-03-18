class Animal:

    def __init__(self, number_of_legs):
        self.legs = number_of_legs

    def number_of_legs(self): 
        return self.legs

    def make_sound(self):
        print("*it's quiet*")
        
        