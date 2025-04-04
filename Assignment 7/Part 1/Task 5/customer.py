from loan import Loan

class Customer:
    id_counter = 0

    def __init__(self):
        Customer.id_counter += 1
        self.id = Customer.id_counter
        self.loans:list[Loan] = []