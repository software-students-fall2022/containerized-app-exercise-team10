import pytest
from app import app
from app import get_db
from app import results
#from requests import HTTPError
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
"""
def test_results():
   url = "/results"
   db = get_db(client)
   results(db)
   response = client.get(url,db)
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
   assert allowed_file(test_file) == True
 
def test_get_db(capsys):
   client = mongomock.MongoClient()
   #get_db(client)
   db = get_db(client)
   captured = capsys.readouterr()
   assert db == client.project_four
   assert "Connected to MongoDB!" in captured.err