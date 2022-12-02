import pytest
from app import app


def test_homepage_route():
    url='/'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code==200

def test_homepage_route_content():
     url='/'
     client = app.test_client()
     response = client.get(url)
     html = response.data.decode()
     assert 'Welcome to Handscribe!' in html
     assert 'Extract text from PDFs and images' in html
     
# def test_homepage_POST_request():
#     url='/'
#     client = app.test_client()
#     response = client.post(url)
#     assert response.status_code==200

def test_invalid_route():
    url='/home'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code==404

# def test_result_rendering():