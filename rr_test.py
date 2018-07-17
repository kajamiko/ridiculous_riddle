from run import app
from unittest import TestCase

class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_thing(self):
        response = self.app.get('/')
        
        assert response == render_template('index.html')