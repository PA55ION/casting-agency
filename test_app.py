import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movies, Actors


PRODUCER = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpScDF1cEE1VV95LXhfODR1NFVLNiJ9.eyJpc3MiOiJodHRwczovL2Rldi15czAtY3hzaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY0OTI3ODQxNDYxNjEwMDZkMjUzZWM5IiwiYXVkIjoiY2FzdGluZy1hZ2VuY3kiLCJpYXQiOjE2MDExNTE0OTMsImV4cCI6MTYwMTIzNzg5MywiYXpwIjoiRXI0VUxGRFAzRUpwUGgzRHM2UHUxa2dOR042eUkybXoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Pz3FenpFzrRO82AqxTZxcGDYyK2DWknWlUqggyLKfgv_qDFci_LOQOvkNNYkCQZ2-Ql1W1uGuMahzilKSw8PYyhTFfz_QjtTHjIL76fASQmQpYwX9kCRSc3UfhIc6HClm7f5ewZg5vnGdWEfhjZq8v8JaSkqZxHwRTOuy9bK8q-M3_M-toi_gQmAhtTj4F45z81UByU2qBd_VJe7Q9ucSTgel8sfui6LTDLC0jPyOUEc5x23Vepmaa36yqPKh5awu4z1MjzZ4beFTj9tlpuAReusy64u9JpCIyw7DZ3KbV5dBojvSzKSqpyk6sLx-a_SkrM9KpinqUDm_gClOJZeJg"


"""This class represents the casting agency test case"""


class CastingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'casting-agency'
        self.database_path = "postgres://{}/{}".format('@localhost:5432',
                                                       self.database_name)
        setup_db(self.app, self.database_path)

        self.auth_header = {
            'Content-Type': 'application/json',
            'Authorization': PRODUCER
        }

        self.new_movie = {
            "title": "Black Panther",
            "release_date": "20 August 2018"
        }

        self.new_actor = {
            "name": "Adam Sandler",
            "age": 30,
            "gender": "Female"
        }

        # bind the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # self.db.create_all()

    def tearDown(self):
        """ Executed after each test"""
        pass

    # GET movies PASS
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # DELETE Movies PASS
    def test_delete_movie(self):
        res = self.client().delete('/movies/12', headers=self.auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 12)
        self.assertTrue(data['message'])

    def test_delete_movies_fail(self):
        res = self.client().delete('/movies/1000', headers=self.auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 'Movie not found')

    # POST Movies PASS

    def test_post_new_movie(self):
        res = self.client().post(
            '/movies', headers=self.auth_header, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['message'])
        self.assertTrue(data['movies'])

    # PATCH movies PASS
    def test_update_movie(self):
        res = self.client().patch('/movies/5', headers=self.auth_header, json={
            'title': 'Parasite',
            'release_date': '8 Nov 2019  12:03:45 GMT'
            })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # GET Actors
    def test_query_actor(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_add_new_actor(self):
        res = self.client().post('/actors', headers=self.auth_header, json={
            "name": "Adam Sandler",
            "age": 45,
            "gender": "Male"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # DELETE actors
    def test_delete_actor(self):
        res = self.client().delete(
            '/actors/7', headers=self.auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Actor successfully deleted.')
        self.assertTrue(data['actors'])

    def test_delete_actor_fail(self):
        res = self.client().delete('/actors/1000', headers=self.auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 500)
        self.assertEqual(data['success'], False)

    # PATCH actors
    def test_update_actor(self):
        res = self.client().patch('/actors/1',
                                  headers=self.auth_header,
                                  json={
                                      'name': 'Leonado DiCaprio',
                                      'age': 47,
                                      'gender': 'Male'
                                  })
        data = json.loads(res.data)

        actor = Actors.query.filter(Actors.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'Successfully updated.')
        self.assertTrue(data['actors'])


if __name__ == "__main__":
    unittest.main()
