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
  #TODO add auth token for director and executive producer
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  # @requires_auth('delete:actors')
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
      }), 404
#TODO add auth token for director and executive producer
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
#TODO add auth token for director and executive producer
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
          'movies': movie.format()
        })
      except Exception:
        return json.dumps({
          'success': False,
          'error': 'An error occurred.'
        }), 500

#COMMENT endpoints for actors

  @app.route('/actors')
  def get_actors():
    try:
      actors = Actors.query.all()
      actor_list = [actor.format() for actor in actors]
      print(actor_list)
      return jsonify({
        'success': True,
        'actor': actor_list
      }), 200

    except Exception:
      return json.dumps({
        'success': False,
        'error': 'Actor not found.'
      }), 404
  #TODO add auth token for director and executive producer
  @app.route('/actors', methods=['POST'])
  # @requires_auth('post:actors')
  def post_actor():
    data = request.get_json()

    new_name = data.get('name', None)
    new_age = data.get('age', None)
    new_gender = data.get('gender', None)

    try:
      actors = Actors(name=new_name, age=new_age, gender=new_gender)
      actors.insert()

      actor_list = Actors.query.order_by('id').all()

      return jsonify({
        'success': True,
        'actors': len(actor_list),
        'message': 'Actor successfully added.'
      })
    except Exception:
      return json.dumps({
        'success': False,
        'error': 'Not able to process your request.'
      }), 422
#TODO add auth token for director and executive producer
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  # @requires_auth('delete:actors')
  def delete_actor(actor_id):
    try:
      actor = Actors.query.get(actor_id)
      actor.delete()
      return jsonify({
        'success': True,
        'message': 'Actor successfully deleted.',
        'actors': actor.id
      }), 200
    except Exception:
      return json.dumps({
        'success': False,
        'error': 'Actor not found.'
      }), 404
#TODO add auth token for director and executive producer 
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  # @requires_auth('patch:actors')
  def update_actor(actor_id):
    actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

    if actor:
      try:
        data = request.get_json()
        update_name = data.get('name', None)
        update_age = data.get('age', None)
        update_gender = data.get('gender', None)
        if update_name:
          actor.name = update_name
        if update_age:
          actor.age = update_age
        if update_gender:
          actor.gender = update_gender

        actor.update()
          
        return jsonify({
          'success': True,
          'message': 'Successfully updated.',
          'actors': actor.format()
        }), 200
      except Exception:
        return json.dumps({
          'success': False,
          'error': 'An error occurred',
        }), 500

  #COMMENT error handler
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      "message": "Unprocessable"
    }), 422

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': "Not found"
    }), 404

  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
      'success': False,
      'message': "Internal server error",
      'error': 500
    }), 500
  
  @app.errorhandler(AuthError)
  def auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
    
  return app

app = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    app.run()