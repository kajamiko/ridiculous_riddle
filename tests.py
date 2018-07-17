import os
from run import app
import unittest


class TestIntegrations(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        resp = self.app.get('/')
        self.assertEqual(resp._status_code, 200)
        
    def test_homepage_post(self):
        resp = self.app.post('/', data=dict(username="test"))
        self.assertEqual(resp._status_code, 302)
        # now it won't work because the name is in file already
        resp2 = self.app.post('/', data=dict(username="test"))
        self.assertEqual(resp2._status_code, 200)
        resp = self.app.post('/', data=dict(username="test2"))
        self.assertEqual(resp._status_code, 302)
        resp2 = self.app.post('/', data=dict(username="test2"))
        self.assertEqual(resp2._status_code, 200)
        # delete data file content
        open('data/users.txt', 'w').close()
        
       
    def test_user_page(self):
        resp = self.app.get('/test')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Hello test!", str(resp.data))
        self.assertNotIn("Whatever", str(resp.data))
    
    def test_user_page_for_okay(self):
        resp = self.app.post('/test')
        self.assertEqual(resp._status_code, 302)
        
    #def test_
                
if __name__ == '__main__':
    
    unittest.main()
