import pytest
from lib.models.magazine import Magazine

def test_magazine_save_and_find():
    mag = Magazine(None, "Tech Monthly", "Technology")
    mag.save()
    assert mag.id is not None  

    found = Magazine.find_by_id(mag.id)
    assert found is not None
    assert found.name == "Tech Monthly"
    assert found.category == "Technology"

def test_magazine_find_by_name():
    mag = Magazine(None, "Health Weekly", "Health")
    mag.save()

    found_mags = Magazine.find_by_name("Health Weekly")
    assert any(m.id == mag.id for m in found_mags)

def test_magazine_name_and_category_validation():
    with pytest.raises(ValueError):
        Magazine(None, "", "Tech")  

    with pytest.raises(ValueError):
        Magazine(None, "Some Mag", "")  

def test_magazine_articles_relationship():
    from lib.models.author import Author
    from lib.models.article import Article

    author = Author(None, "Test Author", "author@example.com")
    author.save()

    mag = Magazine(None, "Science Daily", "Science")
    mag.save()

    article = Article(None, "New Discoveries", "Content here", author.id, mag.id)
    article.save()

    articles = mag.articles()
    assert any(a.id == article.id for a in articles)
