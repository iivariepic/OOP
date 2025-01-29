import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):

        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup


def main():

    my_coin = Coin()

    print(f"This side is up: {my_coin.get_sideup()}")
    my_coin.toss_the_coin()

    print(f"Now this side is up: {my_coin.get_sideup()}")

if __name__ == "__main__":
    main()