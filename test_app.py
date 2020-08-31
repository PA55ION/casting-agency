import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movies, Actors

"""This class represents the casting agency test case"""
class CastingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'casting-agency'
        self.database_path = "postgres://{}/{}".format('@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {
            "title": "Black Panther",
            "release_date": "20 August 2018"
        }

        self.update_movie = {
            "movies": {
                "id": 4,
                "release_date": "8 Nov 2019  12:03:45 GMT",
                "title": "Parasite"
            }
        }
        

        #bind the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # self.db.create_all()
    
    def tearDown(self):
        """ Executed after each test"""
        pass
    #GET movies
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    #DELETE Movies
    # def test_delete_movie(self):
    #     res = self.client().delete('/movies/1')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], 1)
    #     self.assertTrue(data['message'])

    def test_delete_movies_fail(self):
        res = self.client().delete('/movies/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 'Movie not found')
    #POST Movies
    # def test_post_new_movie(self):
    #     res = self.client().post('/movies', json=self.new_movie)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['message'])
    #     self.assertTrue(data['movies'])

    # def test_new_movie_fail(self):
    #     res = self.client().post('/movies')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['error'], 'Not able to add movie at this time')
    #PATCH movies
    def test_update_movie(self):
        res = self.client().patch('/movies/5', json={'title': 'Parasite', 'release_date': '8 Nov 2019  12:03:45 GMT'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    
    def test_update_movie_fail(self):
        res = self.client().patch('/movies/4')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 'Bad request')
    #GET Actors
    def test_query_actor(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    















if __name__ == "__main__":
    unittest.main()