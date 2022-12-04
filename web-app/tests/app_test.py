import pytest
from app import app
from app import get_db
import mongomock


client = mongomock.MongoClient()
collection = client.db.collection
def test_homepage_route():
    url='/'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code==302

"""def test_results_route():
    url='/results'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code==200
"""
def test_invalid_route():
    url='/home'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code==404

def test_allowed_file():
    from app import allowed_file
    test_file = "writing.png"

def test_get_db():
    client = mongomock.MongoClient()
    get_db(client)
    db = get_db(client)
    #captured = capsys.readouterr()
    assert db == client.project_four
