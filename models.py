import os
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime
import json

database_path = os.environ.get('DATABASE_URL')
#database_path = postgresql://mykecampbell@localhost:5432/casting-agency
if not database_path:
    database_name = "casting-agency"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

"""
set up_db(app)
"""

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all()

# def db_drop_and_create_all():
#     db.drop_all()
#     db.create_all()


class Movies(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime, nullable=False)
    image_link = Column(String)
    description = Column(String)

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'description': self.description,
            'image_link': self.image_link,
        }
    
    def __repr__(self):
        return f'<Movies id:{self.id} title: {self.title} release_date: {self.release_date}>'

class Actors(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    image_link = Column(String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def __repr__(self):
        return f'<Actors {self.id} name: {self.name} age: {self.age} gender:{self.gender}>'



