import os
from flask import Flask, session, url_for, flash
from flask import abort
from flask import jsonify
from flask import request
from flask import render_template
from flask import redirect
import json
from six.moves.urllib.parse import urlencode
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movies, Actors, rollback
from auth import AuthError, requires_auth
from flask_wtf import FlaskForm
from flask_wtf import Form
from forms import *
import sys


SECRET_KEY = os.urandom(32)
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
AUTH0_API_AUDIENCE = os.environ.get('AUTH0_API_AUDIENCE')
AUTH0_CALLBACK_URL = os.environ.get('AUTH0_CALLBACK_URL')
AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')
AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID')
AUTH0_BASE_URL = 'https://{AUTH0_DOMAIN}'


def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__)
    db = setup_db(app)
    app.config['SECRET_KEY'] = SECRET_KEY
    cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PATCH,  POST, DELETE, OPTIONS')
        return response

    @app.route('/')
    def index():
        return render_template('layouts/home.html')

    @app.route('/movies')
    def get_movies():
        movies = Movies.query.all();
        return render_template('pages/movies.html', movies=movies)
        # try:
        #     movies = Movies.query.all()
        #     all_movies = [movie.format() for movie in movies]
        #     print(all_movies)
        #     return jsonify({
        #         'success': True,
        #         'movies': all_movies,
        #     })
        # except Exception as e:
        #     print(e)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movie(movie_id):
    # @requires_auth('delete:movies')
    # def delete_movie(token, movie_id):
        try:
            movie = Movies.query.get(movie_id)
            name = movie.title
            movie.delete()
            flash(name + ' successfully deleted!')
            return jsonify({
                'success': True,
                'deleted': movie.id,
                'message': 'Movie ' + name + ' successfully deleted'
            }), 200
        except Exception:
            flash(name +
                  'can not be delete at this time. Please try again later')
            return json.dumps({
                'success': False,
                'error': 'Movie not found'
            }), 404

    @app.route('/movies', methods=['POST'])
    # @requires_auth('post:movies')
    # def add_movie(token):
    def add_movie():
        data = request.get_json()

        new_title = data.get('title', None)
        new_release_date = data.get('release_date', None)
        new_image_link = data.get('image_link', None)
        new_description = data.get('description', None)
        new_genres = data.get('genres', None)

        try:
            movie = Movies(
                title=new_title,
                release_date=new_release_date,
                description=new_description,
                image_link=new_image_link,
                genres=new_genres)
            movie.insert()

            selection = Movies.query.order_by('id').all()
            flash(movie.title + 'successfully added')
            return jsonify({
                'success': True,
                'message': 'Movie ' + movie.title + ' successfully added',
                'movies': len(selection)
            })

        except Exception:
            return json.dumps({
                'success': False,
                'error': 'Not able to add movie at this time',
            }), 422

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    # @requires_auth('patch:movies')
    # def update_movie(token, movie_id):
    def update_movie(movie_id):
        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        if movie:
            try:
                data = request.get_json()
                update_title = data.get('title', None)
                update_release_date = data.get('release_date', None)
                update_image = data.get('image_link', None)
                update_description = data.get('description', None)
                update_genres = data.get('genres', None)
                if update_title:
                    movie.title = update_title
                if update_release_date:
                    movie.release_date = update_release_date
                if update_image:
                    movie.image_link = update_image
                if update_description:
                    movie.description = update_description
                if update_genres:
                    movie.genres = update_genres
                movie.update()
                return jsonify({
                    'success': True,
                    'movies': movie.format()
                })
            except Exception:
                return json.dumps({
                    'success': False,
                    'error': 'Bad request'
                }), 400

    # Get form
    @app.route('/add_movie', methods=['GET'])
    def create_movie_form():
        form = MovieForm()
        return render_template('forms/new_movies.html')

    @app.route('/movies/<int:movie_id>')
    def edit_movie(movie_id):
        form = MovieForm()
        movie = Movies.query.get(movie_id)
        form.title.data = movie.title
        form.release_date.data = movie.release_date
        form.description.data = movie.description
        form.image_link.data = movie.image_link
        return render_template('forms/edit_movie.html', form=form, movie=movie)

# COMMENT endpoints for actors
    @app.route('/actors')
    def get_actors():
        actors = Actors.query.all()
        # try:
        #     actors = Actors.query.all()
        #     actor_list = [actor.format() for actor in actors]
        #     print(actor_list)
        #     return jsonify({
        #         'success': True,
        #         'actors': actor_list
        #     }), 200

        # except Exception:
        #     return json.dumps({
        #         'success': False,
        #         'error': 'Actor not found.'
        #     }), 404

        return render_template('pages/actors.html', actors=actors)
    # add actor
    @app.route('/add_actor', methods=['POST'])
    # @requires_auth('post:actors')
    def add_actor():
        error = False
        new_name = request.form['name']
        new_age = request.form['age']
        new_gender = request.form['gender']
        new_image_link = request.form['image_link']
        new_description = request.form['description']

        try:
            actor = Actors(name=new_name, age=new_age,
                           gender=new_gender, image_link=new_image_link,
                           description=new_description)
                           
            actor.insert()
            flash('Artist ' + request.form['name'] + ' successfully created 🚀')

        except Exception:
            rollback()
            error = True
            abort(400)
            flash('An error occurred. ' + actor.name + ' could not be listed.')

        return redirect(url_for('get_actors'))
        # try:
        #     data = request.get_json()
        #     new_name = data.get('name', None)
        #     new_age = data.get('age', None)
        #     new_gender = data.get('gender', None)
        #     new_image_link = data.get('image_link', None)
        #     new_description = data.get('description', None)

        #     actor = Actors(
        #         name=new_name,
        #         age=new_age,
        #         gender=new_gender,
        #         image_link=new_image_link,
        #         description=new_description)
        #     actor.insert()

        #     selection = Actors.query.order_by('id').all()
        #     return jsonify({
        #         'success': True,
        #         'message': 'Successfully added',
        #         'actors': len(selection)
        #     })

        # except Exception:
        #     return json.dumps({
        #         'success': False,
        #         'error': 'Not able to add model at this time',
        #     }), 422

# delete actor endpoint
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    def delete_actor(actor_id):
    # @requires_auth('delete:actors')
    # def delete_actor(token, actor_id):
        try:
            actor = Actors.query.get(actor_id)
            name = actor.name
            actor.delete()
            flash('Model ' + name + ' successfully deleted!')
            return jsonify({
                'success': True,
                'message': 'Actor successfully deleted.',
                'actors': actor.id
            }), 200
        except Exception:
            flash('Model ' + name +
                  'can not be delete at this time. Please try again later')
            return json.dumps({
                'success': False,
                'error': 'Actor not found.'
            }), 404

# edit actor
    @app.route('/actors/<int:actor_id>', methods=['PATCH', 'POST'])
    # @requires_auth('patch:actors')
    # def update_actor(token, actor_id):
    def update_actor(actor_id):
        actor = Actors.query.get(actor_id)

        try:
            actor.name = request.form['name']
            actor.age = request.form['age']
            actor.gender = request.form['gender']
            actor.image_link = request.form['image_link']
            actor.update()
            flash(request.form['name'] + ' successfully updated 🚀 ')
        except BaseException:
            rollback()
            flash(request.form['name'] + ' cannot be updated! 😞')

        return redirect(url_for('get_actors', actor_id=actor_id))


        # actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
        # if actor:
        #     try:
        #         data = request.get_json()
        #         update_name = data.get('name', None)
        #         update_age = data.get('age', None)
        #         update_gender = data.get('gender', None)
        #         update_image = data.get('image_link', None)
        #         update_description = data.get('description', None)
        #         if update_name:
        #             actor.name = update_name
        #         if update_age:
        #             actor.age = update_age
        #         if update_gender:
        #             actor.gender = update_gender
        #         if update_image:
        #             actor.image_link = update_image
        #         if update_description:
        #             actor.description = update_description

        #         actor.update()

        #         return jsonify({
        #             'success': True,
        #             'message': 'Successfully updated.',
        #             'actors': actor.format()
        #         }), 200
        #     except Exception:
        #         return json.dumps({
        #             'success': False,
        #             'error': 'Bad request.',
        #         }), 400

    @app.route('/add_actor', methods=['GET'])
    def create_actor_form():
        form = ActorForm()
        return render_template('forms/new_actors.html', form=form)

    @app.route('/actors/<int:actor_id>')
    def edit_actor(actor_id):
        form = ActorForm()
        actor = Actors.query.get(actor_id)
        form.name.data = actor.name
        form.age.data = actor.age
        form.gender.data = actor.gender
        form.image_link.data = actor.image_link
        return render_template('forms/edit_actor.html', form=form, actor=actor)

# Error handler

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
    app.run(host='0.0.0.0', port=8080, debug=True)
    # app.run()
