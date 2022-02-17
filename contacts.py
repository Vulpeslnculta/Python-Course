import sqlite3

db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Niko', 46343523, 'niko@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Jimmy', 5058425662, 'jimmymcgill@BCS.com')")


cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())


for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('_'*40)
db.close()