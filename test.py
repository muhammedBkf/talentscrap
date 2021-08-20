from os import close
import sqlite3
from sqlite3.dbapi2 import connect

connection=sqlite3.connect("Student.db")
for row in connection.execute('SELECT * FROM Student Where id<100 AND promo=17'):
        print(row)
connection.close()
