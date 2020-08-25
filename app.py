import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movies, Actors



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  db = setup_db(app)
  cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

  @app.route('/')
  def greeting():
    return 'This is home screen'

  @app.route('/movies')
  def get_movies():
    try:
      movies_list = Movies.query.all()
      all_movies = [movie.format() for movie in movies_list]
      print(all_movies)
      return jsonify({
        'success': True,
        'movies': all_movies,
      })
    except Exception as e:
      print(e)

  return app

app = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    app.run()