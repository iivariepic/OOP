import random

class Coin:
    def __init__(self):
        self.state = 'Heads'

    def toss_the_coin(self) -> None:
        rng_value = random.randint(1, 9)

        match rng_value:
            case 1 | 2 | 3: self.state = 'Heads'
            case 4 | 5 | 6: self.state = 'Tails'
            case 7: self.state = 'Upright'
            case 8: self.state = 'In a rabbit Hole'
            case 9: self.state = 'In a wormhole'

    def get_state(self) -> str:
        return self.state


def main() -> None:

    my_coin = Coin()

    print(f"This is the current state: {my_coin.get_state()}")
    my_coin.toss_the_coin()

    print(f"Now this is the state: {my_coin.get_state()}")

if __name__ == "__main__":
    main()