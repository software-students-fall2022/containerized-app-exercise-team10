import pytest
import pytest_flask
from app import app
from app import get_db
from app import results
from app import download_image_from_db
#from requests import HTTPError
import mongomock
from mongomock.gridfs import enable_gridfs_integration
from flask import url_for
 
 
client = mongomock.MongoClient()
collection = client.db.collection
def test_homepage_route():
   url='/'
   client = app.test_client()
   response = client.get(url)
   assert response.status_code==302
 
#def test_results_route():
#   url='/results'
#   client = app.test_client()
#   response = client.get(url)
#   assert response.status_code==200


# def test_results():
#    url = "/results"
#    db = get_db(client)
#    results(db)
#    response = client.get(url,db)
#    assert response.status_code==200

def test_invalid_route(flask_app):
   url='/home'
   client = flask_app.test_client()
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

def test_get_db_exception_found(capsys):
   db = get_db('notAClient')
   captured = capsys.readouterr()
   print(captured.out)
   assert db != client.project_four
   assert "* Failed to connect to MongoDB\n" in captured.out

# def test_download_image_from_db():
#    mockDb = mongomock.MongoClient().db
#    mongomock.gridfs.enable_gridfs_integration()
#    files = mockDb.files
#    imgObj = {
#       'filename': 'test',
#       '_id': 68
#    }
#    # files.insert_one(imgObj)
#    files.insert_one(imgObj)
#    download_image_from_db(mockDb, imgObj, True)








