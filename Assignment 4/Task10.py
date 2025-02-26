class BankAccount:
    def __init__(self, owner:str, accountNumber:str, balance:float):
        self.__owner = owner
        self.__accountNumber = accountNumber
        self.__balance = balance

    def deposit(self, amount:float):
        self.__service_charge()
        self.__balance += amount

    def withdraw(self, amount:float):
        self.__service_charge()
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance -= (self.__balance * 0.01)

def main():
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)

if __name__ == '__main__':
    main()