import random

class Coin:
    def __init__(self):
        self.state = 'Heads'

    def toss_the_coin(self) -> None:
        rng_value = random.randint(1, 5)

        match rng_value:
            case 1: self.state = 'Heads'
            case 2: self.state = 'Tails'
            case 3: self.state = 'Upright'
            case 4: self.state = 'In a rabbit Hole'
            case 5: self.state = 'In a wormhole'

    def get_state(self) -> str:
        return self.state


def main() -> None:

    my_coin = Coin()

    print(f"This is the current state: {my_coin.get_state()}")
    my_coin.toss_the_coin()

    print(f"Now this is the state: {my_coin.get_state()}")

if __name__ == "__main__":
    main()