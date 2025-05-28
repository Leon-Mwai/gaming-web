import pytest
from lib.models.magazine import Magazine

def test_magazine_creation():
    mag = Magazine(name="Code Ninja", category="Coding")
    mag.save()
    assert mag.id is not None

def test_find_magazine_by_name():
    mag = Magazine.find_by_name("Tech Weekly")
    assert mag is not None
    assert mag.category == "Technology"

def test_article_titles_in_magazine():
    mag = Magazine.find_by_name("Manga Digest")
    titles = mag.article_titles()
    assert "Battle of The Gods" in titles

def test_contributors():
    mag = Magazine.find_by_name("Tech Weekly")
    contributors = mag.contributors()
    names = [c["name"] for c in contributors]
    assert "Leon" in names

def test_contributing_authors():
    mag = Magazine.find_by_name("Tech Weekly")
    result = mag.contributing_authors()
    assert isinstance(result, list)
