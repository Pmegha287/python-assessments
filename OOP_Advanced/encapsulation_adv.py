class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

acc = BankAccount()
print(acc.get_balance())
acc.set_balance(5000)
print(acc.get_balance())