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
    assert response.status_code == 200  # Check that the status code is 200
    assert b"Hello World!" in response.data  # Check that 'Hello World!' is in the response
