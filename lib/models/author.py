import sqlite3
from lib.db.connection import CONNECTION

class Author:
    def __init__(self, id, name, email, location=None, category=None):
        self.id = id
        self.name = name
        self.email = email
        self.location = location
        self.category = category

    @classmethod
    def create(cls,name,email,location=None,category=None):
        cursor= CONNECTION.cursor()
        cursor.execute(
            "INSERT INTO authors(name,email,location,category) VALUES(?,?,?,?)",
            (name,email,location,category)
        )
        CONNECTION.commit()
        return cls(cursor.lastrowid,name,email,location,category)