import datetime
import sqlite3
from decimal import *
import pytz

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL,"
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):
    _qb = Decimal('0.00')

    def __init__(self, name: str, opening_balance: float = 0.0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name =?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self. _balance = row
            print("Retrieved record for {}. ".format(self.name), end="")
        else:
            self.name = name
            self._balance = Decimal(opening_balance).quantize(Account._qb)
            cursor.execute("INSERT INTO accounts VALUES (?, ?)", (name, opening_balance))
            cursor.connection.commit()
        print("Account created for {}.".format(self.name), end="")
        self.show_balance()

    def deposit(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if decimal_amount > Account._qb:
            new_balance = self._balance + int(decimal_amount)
            deposit_time = pytz.utc.localize(datetime.datetime.utcnow())
            db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (float(new_balance), self.name,))
            db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount,))
            db.commit()
            self._balance = new_balance
            print("{} deposited".format(decimal_amount))
        return self._balance

    def withdraw(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if Account._qb < decimal_amount <= self._balance:
            self._balance -= self._balance - int(decimal_amount)
            print("{} withdrawn".format(amount))
            return decimal_amount
        else:
            print("The amount must be greater than zero, or you have insufficient account balance")
            return decimal_amount

    def show_balance(self):
        print("Balance on account {} is equal to {}".format(self.name, self._balance))


if __name__ == '__main__':
    john = Account("John")
    john.deposit(100.10)
    john.withdraw(200.05)
    john.deposit(200)
    john.withdraw(300)
    john.show_balance()

    terry = Account("Terry", 10000)
    niko = Account("Niko", 0.1)
    terryG = Account("TerryG")
    terryJ = Account("TerryJ")

db.close()