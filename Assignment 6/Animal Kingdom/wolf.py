from mammal import Mammal
from animal import Animal

class Wolf(Mammal):

    def __init__(self, pack:str):
        assert len(pack) > 0, "Pack must have a name"

        Mammal.__init__(self)
        self.pack_name = pack

    @Animal.require_alive
    def another_make_sound(self):
        print("*wolf howling*")
        