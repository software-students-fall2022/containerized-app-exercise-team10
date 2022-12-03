import pytest
from app import app


#ROUTE: route handler for GET request to '/'
def test_homepage_route():
    url='/'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code==200

#ROUTE: (invalid) route handler for GET request to '/'
def test_invalid_route():
    url='/home'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code==404

#FUNCTION: homepage renders expected information
def test_homepage_route_content():
     url='/'
     client = app.test_client()
     response = client.get(url)
     html = response.data.decode()
     assert 'Welcome to Handscribe!' in html
     assert 'Extract text from PDFs and images' in html

#ROUTE: route handler for POST request to '/'
# def test_homepage_POST_request():
#     url='/'
#     client = app.test_client()
#     response = client.post(url)
#     assert response.status_code==200


# def test_result_rendering():