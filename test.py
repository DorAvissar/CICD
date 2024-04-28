import pytest
from app import app  # Importing your Flask app

# Define a test class for better organization
class TestFlaskApp:
    @pytest.fixture
    def client(self):
        """Fixture for setting up a test client."""
        app.config['TESTING'] = True  # Set Flask app to testing mode
        with app.test_client() as client:
            yield client  # Provide the test client

    def test_hello_world(self, client):
        """Test that the root endpoint returns 'Hello World!'"""
        response = client.get('/')  # Get response from the root endpoint
        assert response.status_code == 200  # Check that the status code is 200
        assert b"Hello World!" in response.data  # Check that the response contains "Hello World!"
