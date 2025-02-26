class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        pass
        # The amount should be subtracted from the balance only if
        # there is enough money on the card.
        # If the payment is successful, the method returns True.
        # Otherwise it returns False.


class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.ordinaries = 0
        self.luxuries = 0

    def eat_ordinary(self, payment: float):
        # A ordinary lunch costs 2.95 euros.
        # Increase the value of the funds at the terminal by the
        # price of the lunch, increase the number of lunches sold,
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        pass

    def eat_luxury(self, payment: float):
        # A sluxury lunch costs 5.90 euros.
        # Increase the value of the funds at the terminal by the
        # price of the lunch, increase the number of lunches sold,
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        pass

    def eat_ordinary_lunchcard(self, card: LunchCard):
        # A ordinary lunch costs 2.95 euros.
        # If there is enough money on the card,
        # subtract the price of the lunch from the balance
        # and return True. If not, return False.
        pass

    def eat_luxury_lunchcard(self, card: LunchCard):
        # A luxury lunch costs 5.90 euros.
        # If there is enough money on the card,
        # subtract the price of the lunch from the balance
        # and return True. If not, return False.
        pass

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        pass


# You may use the following code to test your function:

if __name__ == "__main__":
    # Part1
    """ card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance) """

    # Part2
    """ exactum = PaymentTerminal()

    change = exactum.eat_ordinary(10)
    print("The change returned was", change)

    change = exactum.eat_ordinary(5.9)
    print("The change returned was", change)

    change = exactum.eat_luxury(5.9)
    print("The change returned was", change)

    print("Funds available at the terminal:", exactum.funds)
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries) """

    # Part 3
    """ exactum = PaymentTerminal()

    change = exactum.eat_ordinary10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_ordinary_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials) """

    # Part4
    """ exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials) """