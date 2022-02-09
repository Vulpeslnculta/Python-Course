import datetime
import pytz



class Account:
    """ Simple account with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self.name)
        self.show_balance()

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

    def show_transactions(self):
        for date, amount in self.trasaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
            amount *= -1
        print('{:6} {} on (local time was {})'.format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    niko = Account("Niko", 0)
    niko.show_balance()

    niko.deposit(10000)
    niko.show_balance()
    niko.withdraw(500)
    niko.show_balance()
    niko.show_transactions()

    Anne = Account("Anne", 515)
    Anne.show_balance()
    print(Anne.__dict__)