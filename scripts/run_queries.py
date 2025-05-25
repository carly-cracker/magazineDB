from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

author = Author(None, "Shee", "shee@example.com", "Nairobi", "Tech")
author.save()

magazine = Magazine(None, "Tech World", "Technology")
magazine.save()

article1 = Article(None, "AI Trends", "AI is transforming industries.", author.id, magazine.id)
article1.save()

article2 = Article(None, "Cybersecurity Tips", "Stay safe online.", author.id, magazine.id)
article2.save()

print("Author of article1:", article1.author())
print("Magazine of article1:", article1.magazine())
print("Articles by Shee:", [a.title for a in author.articles()])
print("Articles in Tech World:", [a.title for a in magazine.articles()])
