import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter your name: \n")

for name, phone, email in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(name)
    print(phone)
    print(email)
    print("_"*20)


conn.close()
