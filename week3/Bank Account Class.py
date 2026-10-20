
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount!")

    def display_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount(1000)

account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()
