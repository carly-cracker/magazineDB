import pytest
from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine
from lib.db.connection import CONNECTION

def setup_function():
    cursor = CONNECTION.cursor()
    cursor.execute("DELETE FROM authors")
    CONNECTION.commit()

def test_author_save_and_find():
    author = Author(None, "Shee", "shee@example.com", "Nairobi", "Tech")
    author.save()

    assert author.id is not None

    found = Author.find_by_id(author.id)
    
    assert found is not None
    assert found.name == "Shee"
    assert found.email == "shee@example.com"
    assert found.location == "Nairobi"
    assert found.category == "Tech"

def test_author_articles_relationship():
    author = Author(None, "Shee", "shee@example.com", "Nairobi", "Tech")
    author.save()

    magazine = Magazine(None, "Tech Weekly", "Tech")
    magazine.save()

    article = Article(None, "AI News", "AI is big!", author.id, magazine.id)
    article.save()

    articles = author.articles()

    assert len(articles) == 1
    assert articles[0].title == "AI News"