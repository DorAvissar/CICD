import pytest
from app import app  # Import your Flask app

@pytest.fixture
def client():
    """Fixture for creating a test client."""
    app.config['TESTING'] = True  # Set Flask app to testing mode
    with app.test_client() as client:
        yield client  # Provide a test client for Flask tests

def test_hello_world(client):
    """Test that the root endpoint returns 'Hello World!'"""
    response = client.get('/')  # Send a GET request to the root endpoint
    assert response.status_code == 200  # The HTTP status code should be 200
    assert b"Hello World!" in response.data  # The response data should contain "Hello World!"

def test_404_error(client):
    """Test that a non-existent route returns a 404 error"""
    response = client.get('/nonexistent')  # Send a GET request to a non-existent route
    assert response.status_code == 404  # The HTTP status code should be 404
