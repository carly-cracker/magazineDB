from lib.db.connection import CONNECTION

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title 
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

   
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) :
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string.")
        
    def save(self):
        cursor = CONNECTION.cursor()
        cursor.execute(
            "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
            (self.title, self.content, self.author_id, self.magazine_id)
            )
        CONNECTION.commit()
        self.id = cursor.lastrowid
        return self
    @classmethod
    def find_by_id(cls, id):
        cursor = CONNECTION.cursor()
        row = cursor.execute("SELECT * FROM articles WHERE id = ?", (id,)).fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_title(cls, title):
        cursor = CONNECTION.cursor()
        rows = cursor.execute("SELECT * FROM articles WHERE title = ?", (title,)).fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_author_id(cls, author_id):
        cursor = CONNECTION.cursor()
        rows = cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,)).fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_magazine_id(cls, magazine_id):
        cursor = CONNECTION.cursor()
        rows = cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (magazine_id,)).fetchall()
        return [cls(*row) for row in rows]