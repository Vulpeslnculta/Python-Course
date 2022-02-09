class Account:
    """ Simple account with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    niko = Account("Niko", 0)
    niko.show_balance()

    niko.deposit(10000)
    niko.show_balance()