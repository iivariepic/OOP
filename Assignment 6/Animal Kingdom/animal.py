import random

class Animal:

    def __init__(self, number_of_legs:int, old_age:int, initial_age:int = 0):
        assert number_of_legs > 0, "The number of legs must be greater than 0"
        assert old_age > 0, "Old age must be greater than 0"
        assert initial_age >= 0, "Initial age cannot be negative"

        # Old age is a parameter where the animal is considered old and can die
        self.legs:int = number_of_legs
        self.__age:int = initial_age
        self.__old_age:int = old_age
        self.__is_alive:bool = True

    @staticmethod
    def require_alive(func):
        def wrapper(self, *args, **kwargs):
            if self.__is_alive:
                func(self, *args, **kwargs)
            else:
                print("Can't run command, animal is dead!")
        return wrapper

    def number_of_legs(self): 
        return self.legs

    @require_alive
    def make_sound(self):
        print("*it's quiet*")

    @property
    def is_alive(self):
        return self.__is_alive

    @property
    def age(self):
        return self.__age

    @require_alive
    def age_up(self):
        self.__age += 1
        if self.__age > self.__old_age:
            self.__death_lottery()

    @require_alive
    def __death_lottery(self):
        if random.randint(0, 1) == 1:
            self.__is_alive = False