import os
from flask import url_for
from run import app
import unittest
import json


class TestIntegrations(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        # needs a SERVER_NAME to run with app context
        self.app.application.config["SERVER_NAME"] = "{0} {1}".format(os.environ.get('PORT'), os.environ.get('IP'))

    def test_homepage(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        
        
    def test_homepage_post(self):
        resp = self.app.post('/', data=dict(username="test"))
        self.assertEqual(resp.status_code, 302)
        # now it won't work because the name is in file already
        resp2 = self.app.post('/', data=dict(username="test"))
        self.assertEqual(resp2.status_code, 200)
        #self.assertIn("This name has been used already.", str(resp2.data))
        resp = self.app.post('/', data=dict(username="test2"))
        self.assertEqual(resp._status_code, 302)
        resp2 = self.app.post('/', data=dict(username="test2"))
        self.assertEqual(resp2.status_code, 200)
        # delete data file content
        open('data/users.txt', 'w').close()
        
       
    def test_user_page(self):
        """
        Function tests if a proper template is rendered, just by checking if 'hello <username>' is in the response data
        """
        resp = self.app.get('/test')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Hello <b>test</b>", str(resp.data))
        self.assertNotIn("Whatever", str(resp.data))
    
    def test_user_page_for_start(self):
        """
        Function is testing if the correct values are passed to the correct path
        """
        with app.app_context():
            resp = self.app.post('/test')
            self.assertEqual(resp._status_code, 302)
            self.assertEqual(resp.location, url_for('game', username='test', level='1', score='0', _external=True))
        
    def test_game_page_for_loading(self):
        """
        Checks if loading properly 
        """
        resp = self.app.get('/game/test/1/0')
        self.assertEqual(resp.status_code, 200)
            
    def test_game_page_for_responding(self):
        """
        Checks if processing data as required and if the correct riddle s being displayed
        """
        with app.app_context():
            resp = self.app.post('/game/test/1/0', data=dict(answer="yes", score_getter="4"))
            self.assertEqual(resp.location, url_for('game', username='test', level='2', score='4', _external=True))
        
        
    def test_game_over(self):
        """
        Function tests:
        1. if the path gives correct result
        2. If the result was dumped into the file as desired
        """
        resp = self.app.get('/game_over/test1/25')
        self.assertEqual(resp.status_code, 200)
        with open("data/leaderboard.json", "r") as lb_file:
            lb_data = json.load(lb_file)
            self.assertIn("test1", lb_data)
                
    def test_leaderboard(self):
        resp = self.app.get('/leaderboard')
                
if __name__ == '__main__':
    
    unittest.main()
