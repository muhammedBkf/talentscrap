from os import close
import sqlite3
from sqlite3.dbapi2 import connect
class Database :
    def __init__(self,path):
        self.path=path


    def create(self):
        self.connection=sqlite3.connect(self.path)
        self.connection.execute(
            '''
            CREATE TABLE Student(
                promo INTEGER,
                id INTEGER,
                familyName TEXT,
                name TEXT,
                email TEXT,
                image TEXT,
                PRIMARY KEY(promo,id)
                    )                    
            ''')
        self.connection.commit()
        self.connection.close()
    
    def insert_student(self,student):
        self.connection=sqlite3.connect(self.path)
        self.connection.execute("INSERT INTO Student VALUES ({},{},'{}','{}','{}','{}')".format(student.promo,student.id,student.familyName,student.name,student.email,student.image))
        self.connection.commit()
        self.connection.close()
        print("{}-{} added sucessfully".format(student.familyName,student.name))


