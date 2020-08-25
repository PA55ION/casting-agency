import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  db = setup_db(app)
  cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

  @app.route('/')
  def greeting():
    return 'This is home screen'

  @app.route('/testing')
  def testing():
    return 'This is testing screen'

  return app

app = create_app()

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    app.run()