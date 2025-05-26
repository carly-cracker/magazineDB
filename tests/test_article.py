import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_save_and_find():
    
    author = Author(None, "Jane Doe", "jane@example.com", "Nairobi", "Tech")
    author.save()

    mag = Magazine(None, "Tech Times", "Technology")
    mag.save()

    article = Article(None, "AI Revolution", "Content about AI", author.id, mag.id)
    article.save()

    found = Article.find_by_id(article.id)
    assert found is not None
    assert found.title == "AI Revolution"
    assert found.author_id == author.id
    assert found.magazine_id == mag.id

def test_article_find_by_title():
    author = Author(None, "John Smith", "john@example.com", "Mombasa", "Science")
    author.save()
    mag = Magazine(None, "Science Weekly", "Science")
    mag.save()

    article1 = Article(None, "Quantum Physics", "Deep dive into quantum...", author.id, mag.id)
    article1.save()
    article2 = Article(None, "Quantum Physics", "Another perspective...", author.id, mag.id)
    article2.save()

    found_articles = Article.find_by_title("Quantum Physics")
    assert isinstance(found_articles, list)
    assert len(found_articles) >= 2  

def test_article_find_by_author_id():
    author = Author(None, "Alice", "alice@example.com", "Kisumu", "Tech")
    author.save()
    mag = Magazine(None, "Tech Daily", "Technology")
    mag.save()

    article = Article(None, "Smartphones 2025", "Trends in mobile tech", author.id, mag.id)
    article.save()

    found = Article.find_by_author_id(author.id)
    assert any(a.id == article.id for a in found)

def test_article_find_by_magazine_id():
    author = Author(None, "Bob", "bob@example.com", "Nakuru", "Business")
    author.save()
    mag = Magazine(None, "Biz Insider", "Business")
    mag.save()

    article = Article(None, "Startups to Watch", "Hot new startups", author.id, mag.id)
    article.save()

    found = Article.find_by_magazine_id(mag.id)
    assert any(a.id == article.id for a in found)

def test_article_author_relationship():
    author = Author(None, "Caro", "caro@example.com", "Eldoret", "Lifestyle")
    author.save()
    mag = Magazine(None, "Life Mag", "Lifestyle")
    mag.save()

    article = Article(None, "Healthy Living", "Tips and tricks", author.id, mag.id)
    article.save()

    assert article.author().id == author.id
    assert article.author().name == "Caro"

def test_article_magazine_relationship():
    author = Author(None, "David", "david@example.com", "Thika", "Finance")
    author.save()
    mag = Magazine(None, "Money Matters", "Finance")
    mag.save()

    article = Article(None, "Saving Smart", "Finance article", author.id, mag.id)
    article.save()

    assert article.magazine().id == mag.id
    assert article.magazine().name == "Money Matters"
