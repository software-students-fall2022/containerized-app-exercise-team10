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
     