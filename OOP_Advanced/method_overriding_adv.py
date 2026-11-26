class Bank:
    def interest(self):
        print("Bank interest 5%")

class SBI(Bank):
    def interest(self):
        print("SBI interest 7%")

b = SBI()
b.interest()