import sys
import os

# Get the parent directory of the current file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Assignment 2')))

# Now you can import from Task2.py
from Task2 import Carriage

class Train:
    def __init__(self, initial_carriage):
        self.carriages:list[Carriage] = [initial_carriage]

    def attach_carriage(self, carriage):
        if carriage not in self.carriages:
            self.carriages.append(carriage)



def main():
    pendolino = Train(Carriage(1))
    print(pendolino.carriages)

if __name__ == '__main__':
    main()