import datetime
import sqlite3
from decimal import *
import pytz

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL,"
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):
    _qb = Decimal('0.00')

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

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
            print("Account created for {}. ".format(self.name), end="")
        self.show_balance()

    def _save_update(self, amount):
        new_balance = round(self._balance + float(amount), 2)
        deposit_time = Account._current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, str(self.name), round(float(amount), 2)))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if decimal_amount > Account._qb:
            # new_balance = self._balance + float(decimal_amount)
            # deposit_time = Account._current_time(self)
            # db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (float(new_balance), self.name,))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount,))
            # db.commit()
            # self._balance = new_balance
            self._save_update(decimal_amount)
            print("{} deposited".format(decimal_amount))
            round(self._balance, 2)
        return self._balance

    def withdraw(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if Account._qb < decimal_amount <= self._balance:
            # new_balance = round((self._balance - float(decimal_amount)), 2)
            # withdrawal_time = Account._current_time(self)
            # db.execute("UPDATE accounts SET balance = ? WHERE (name=?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdrawal_time, -amount, self.name))
            self._save_update(-decimal_amount)
            print("{} withdrawn".format(amount))
            return decimal_amount
        else:
            print("The amount must be greater than zero, or you have insufficient account balance")
            return decimal_amount

    def show_balance(self):
        print("Balance on account {} is equal to {}".format(self.name, self._balance))


if __name__ == '__main__':
    john = Account("John")
    john.deposit(100.05)
    john.withdraw(200.15)
    john.deposit(200.05)
    john.withdraw(300)
    john.show_balance()

    terry = Account("Terry", 10000)
    niko = Account("Niko", 0.1)
    terryG = Account("TerryG")
    terryJ = Account("TerryJ")

db.close()