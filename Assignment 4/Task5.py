class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        new_balance = self.balance - amount
        if new_balance < 0:
            return False
        self.balance = new_balance
        return True


class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.ordinaries = 0
        self.luxuries = 0
        self.ordinaryPrice:float = 2.95
        self.luxuryPrice:float = 5.90

    def eat_ordinary(self, payment: float):
        if payment < self.ordinaryPrice:
            return payment

        self.ordinaries += 1
        self.funds += self.ordinaryPrice
        return payment - self.ordinaryPrice


    def eat_luxury(self, payment: float):
        if payment < self.luxuryPrice:
            return payment

        self.luxuries += 1
        self.funds += self.luxuryPrice
        return payment - self.luxuryPrice

    def eat_ordinary_lunchcard(self, card: LunchCard):
        if not card.subtract_from_balance(self.ordinaryPrice):
            return False

        self.ordinaries += 1
        self.funds += self.ordinaryPrice
        return True

    def eat_luxury_lunchcard(self, card: LunchCard):
        if not card.subtract_from_balance(self.luxuryPrice):
            return False

        self.luxuries += 1
        self.funds += self.luxuryPrice
        return True

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount


# You may use the following code to test your function:

if __name__ == "__main__":
    # Part1
    card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)

    # Part2
    exactum = PaymentTerminal()

    change = exactum.eat_ordinary(10)
    print("The change returned was", change)

    change = exactum.eat_ordinary(5.9)
    print("The change returned was", change)

    change = exactum.eat_luxury(5.9)
    print("The change returned was", change)

    print("Funds available at the terminal:", round(exactum.funds, 2))
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries)

    # Part 3
    exactum = PaymentTerminal()

    change = exactum.eat_ordinary(10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_ordinary_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.ordinaries)
    print("Special lunches sold:", exactum.luxuries)

    # Part4
    exactum = PaymentTerminal()

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
    print("Regular lunches sold:", exactum.ordinaries)
    print("Special lunches sold:", exactum.luxuries)