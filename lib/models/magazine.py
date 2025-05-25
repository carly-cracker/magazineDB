import sqlite3
from lib.db.connection import CONNECTION

class Magazine:
    def __init__(self,id,name,category):
        self.id = id
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value)>0:
            self._name = value
        else:
            raise ValueError("name must be a string with chars")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value)>0:
            self._category = value
        else:
            raise ValueError("the category must be a string")
        
    def save(self):
        cursor = CONNECTION.cursor()
        cursor.execute(
            "INSERT INTO magazines (name, category) VALUES (?,?)",
            (self.name, self.category)
        )
        CONNECTION.commit()
        self.id = cursor.lastrowid
        return self
    
    @classmethod
    def find_by_id(cls, id):
        cursor = CONNECTION.cursor()
        row = cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,)).fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_name(cls, name):
        cursor = CONNECTION.cursor()
        row = cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,)).fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_category(cls, category):
        cursor = CONNECTION.cursor()
        rows = cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,)).fetchall()
        return [cls(*row) for row in rows]
    
    def articles(self):
        from lib.models.article import Article  # avoid circular import
        return Article.find_by_magazine_id(self.id)

    def authors(self):
        articles = self.articles()
        unique_authors = {article.author() for article in articles}
        return list(unique_authors)