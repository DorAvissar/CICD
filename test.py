import unittest  # Importing the unittest framework
from app import app  # Importing your Flask app

class TestFlaskApp(unittest.TestCase):
    """Tests for the Flask application"""

    def setUp(self):
        """Set up the test client for each test"""
        app.config['TESTING'] = True  # Set the app to testing mode
        self.client = app.test_client()  # Create a test client

    def test_hello_world(self):
        """Test that the root endpoint returns 'Hello World!'"""
        response = self.client.get('/')  # Get response from the root endpoint
        self.assertEqual(response.status_code, 200)  # Assert that the status code is 200
        self.assertIn(b"Hello World!", response.data)  # Assert that "Hello World!" is in the response data

    def tearDown(self):
        """Clean up after each test"""
        pass  # You can add cleanup code here if needed
