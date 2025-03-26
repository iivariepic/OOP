import random

class Trick:
    def __init__(self, action:str, difficulty:int):
        self.action = action
        self.difficulty = difficulty
        if self.difficulty > 10:
            self.difficulty = 10

    def perform(self):
        # Function to perform a trick, returns true is successful
        return random.randint(0,10) >= self.difficulty