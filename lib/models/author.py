import sqlite3
from lib.db.connection import CONNECTION

class Author:
    def __init__(self, id, name, email, location=None, category=None):
        self.id = id
        self.name = name
        self.email = email
        self.location = location
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) :
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")
        
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if isinstance(value, str) and "@" in value :
            self._email = value
        else:
            raise ValueError("Email must be a valid  string containing '@'.")



    @classmethod
    def create(cls,name,email,location=None,category=None):
        cursor= CONNECTION.cursor()
        cursor.execute(
            "INSERT INTO authors(name,email,location,category) VALUES(?,?,?,?)",
            (name,email,location,category)
        )
        CONNECTION.commit()
        return cls(cursor.lastrowid,name,email,location,category)
    
    @classmethod
    def all(cls):
        cursor = CONNECTION.cursor()
        rows = cursor.execute("SELECT * FROM authors"). fetchall()
        return [cls(*row) for row in rows]
    
    @classmethod
    def find_by_id(cls,id):
        cursor = CONNECTION.cursor
        row = cursor.execute("SELECT * FROM authors WHERE id = ?",(id,)).fetchone()
        return cls(*row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        cursor = CONNECTION.cursor()
        rows = cursor.execute("SELECT * FROM authors WHERE name = ?", (name,)).fetchall()
        return [cls(*row) for row in rows]
    
    def articles(self):
        from lib.models.article import Article  
        return Article.find_by_author_id(self.id)
