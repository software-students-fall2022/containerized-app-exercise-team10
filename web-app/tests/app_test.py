import pytest
from app import app


#ROUTE: route handler for GET request to '/' (redirection)
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

#ROUTE: (invalid) route handler for GET request to '/'
def test_invalid_route():
    url='/home'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code==404

def test_allowed_file():
    from app import allowed_file
    test_file = "writing.png"
    assert allowed_file(test_file) == True