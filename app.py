import os
from flask import Flask, request, abort, jsonify, request, render_template, redirect
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movies, Actors



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  db = setup_db(app)
  cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

  @app.route('/')
  def index():
    return render_template('/home.html')

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
  #COMMENT add auth token for director and executive producer
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  def delete_movie(movie_id):

    try:
      movie = Movies.query.get(movie_id)
      movie.delete()
      return jsonify({
        'success': True,
        'deleted': movie.id,
        'message': 'Successfully deleted'
      }), 200
    except Exception:
      return json.dumps({
        'success': False,
        'error': 'Movie not found'
      }), 400
#COMMENT add auth token for director and executive producer
  @app.route('/movies', methods=['POST'])
  # @requires_auth('post:movies')
  def post_movie():
    data = request.get_json()

    new_title = data.get('title', None)
    new_release_date = data.get('release_date', None)

    try:
      movie = Movies(title=new_title, release_date=new_release_date)
      movie.insert()

      selection = Movies.query.order_by('id').all()

      return jsonify({
        'success': True,
        'message': 'Successfully added',
        'movies': len(selection)
      })
    except Exception:
      return json.dumps({
        'success': False,
        'error': 'Not able to add movie at this time',
      }), 400
#COMMENT add auth token for director and executive producer
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  # @requires_auth('patch:movies')
  def update_movie(movie_id):
    movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
    if movie:
      try:
        data = request.get_json()
        update_title = data.get('title', None)
        update_release_date = data.get('release_date', None)
        if update_title:
          movie.title = update_title
        if update_release_date:
          movie.release_date = update_release_date
        movie.update()
        return jsonify({
          'success': True,
          'movies': [movie.format()]
        })
      except Exception:
        return json.dumps({
          'success': False,
          'error': 'An error occurred'
        }), 500

  return app

app = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    app.run()