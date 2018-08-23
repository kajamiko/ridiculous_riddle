import os
import flask
from run import app
import unittest
import json


class TestIntegrations(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.application.config['SECRET_KEY'] = 'az#5t];a5g,dfnmk34;322bum'
        # needs a SERVER_NAME to run with app context
        self.app.application.config["SERVER_NAME"] = "{0} {1}".format(os.environ.get('PORT'), os.environ.get('IP'))

    def test_homepage(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)
        
        
    def test_homepage_post(self):
        resp = self.app.post('/', data=dict(username="test2"))
        self.assertEqual(resp.status_code, 302)
        
       
    def test_user_page(self):
        """
        Function tests if a proper template is rendered, just by checking if 'hello <username>' is in the response data
        """
        resp = self.app.get('/test')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Hello <b>test</b>", str(resp.data))
        self.assertNotIn("Whatever", str(resp.data))
    
    
        
    def test_game_page_for_loading(self):
        """
        Checks if loading properly 
        """
        resp = self.app.get('/game/test/1/0')
        self.assertEqual(resp.status_code, 200)
            
    def test_game_page_for_responding(self):
        """
        Checks if processing data as required and if the correct riddle is being displayed
        """
        
        with self.app as c:
                resp = self.app.post('/', data=dict(username="test2"))
                self.assertEqual(resp.status_code, 302)
                resp1 = self.app.get('/game_over/test1/10')
                self.assertEqual(resp1.status_code, 200)
                print(resp1.location)
    
    def test_restart(self):
        with self.app as c:
            resp1 = self.app.get('/restart/test1') 
            print(resp1.location)
        
    # def test_game_over(self):
    #     """
    #     Function tests:
    #     1. if the path gives correct result
    #     2. If the result was dumped into the file as desired
    #     """
    #     with app.test_client() as c:
    #         with c.session_transaction() as sess:
    #             resp = self.app.post('/test')
    #             resp1 = self.app.post('/game/test1/1/0', data=dict(answer="yes", score_getter="25"))
    #             self.assertEqual(resp1.status_code, 200)
    #             resp2 = self.app.get('/game_over/test/25')
    #             with open("data/leaderboard.json", "r") as lb_file:
    #                 lb_data = json.load(lb_file)
    #                 self.assertIn("test1", lb_data)
                
    def test_leaderboard(self):
        resp = self.app.get('/leaderboard')
        self.assertIn("Leaderboard", str(resp.data))
        self.assertNotIn("4 pink unicorns", str(resp.data))
    
    def test_cheating_prevention(self):
        
        resp = self.app.get('/ban_me/test')
        self.assertEqual(resp.status_code, 302)
        resp2 = self.app.post('/', data=dict(username='test'))
        #won't work because name already on banned list
        self.assertEqual(resp2.status_code, 200)
             
             
if __name__ == '__main__':
    
    unittest.main()
