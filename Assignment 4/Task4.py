class LunchCard:
    def __init__(self, balance:float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {round(self.balance * 10)/10} euros"

    def __subtract_balance(self, amount:float):
        new_balance = self.balance - amount
        if new_balance < 0:
            return False

        self.balance = new_balance
        return True

    def eat_ordinary(self):
        if not self.__subtract_balance(2.95):
            print("Payment Unsuccessful")
        return

    def eat_luxury(self):
        if not self.__subtract_balance(5.9):
            print("Payment Unsuccessful")
        return

    def deposit_money(self, amount:float):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")

        self.balance += amount


def main():
    peterCard = LunchCard(20)
    graceCard = LunchCard(30)
    peterCard.eat_luxury()
    graceCard.eat_ordinary()
    print(f"Peter: {peterCard}")
    print(f"Grace: {graceCard}")
    peterCard.deposit_money(20)
    graceCard.eat_luxury()
    print(f"Peter: {peterCard}")
    print(f"Grace: {graceCard}")
    peterCard.eat_ordinary()
    peterCard.eat_ordinary()
    graceCard.deposit_money(50)
    print(f"Peter: {peterCard}")
    print(f"Grace: {graceCard}")

if __name__ == '__main__':
    main()