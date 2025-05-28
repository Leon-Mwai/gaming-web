import pytest
from lib.models.article import Article
from lib.db.connection import get_connection

def test_article_creation():
    article = Article(title="Tech Future", author_id=1, magazine_id=1)
    article.save()

    assert article.id is not None

def test_find_article_by_id():
    article = Article.find_by_id(1)
    assert article is not None
    assert article.title == "The Rise of AI"

def test_find_by_title():
    article = Article.find_by_title("Python vs JS")
    assert article is not None
    assert article.magazine_id == 1

def test_article_relationships():
    article = Article.find_by_title("Battle of The Gods")
    author = article.get_author()
    magazine = article.get_magazine()

    assert author["name"] == "Uzumaki"
    assert magazine["name"] == "Manga Digest"
