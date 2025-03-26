from mammal import Mammal
from animal import Animal

class Wolf(Mammal):

    def __init__(self, pack):
        Mammal.__init__(self)
        self.pack_name = pack

    @Animal.require_alive
    def another_make_sound(self):
        print("*wolf howling*")
        