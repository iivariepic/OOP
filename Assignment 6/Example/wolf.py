from mammal import Mammal

class Wolf(Mammal):

    def __init__(self, pack):
        Mammal.__init__(self)
        self.pack_name = pack

    def another_make_sound(self):
        print("*wolf howling*")
        