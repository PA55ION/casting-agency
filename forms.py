from datetime import datetime
from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, DateField, SelectMultipleField
from wtforms.validators import DataRequired, AnyOf, URL


class MovieForm(Form):
    title = StringField(
        'title', validators=[DataRequired(message='Please enter a title.')]
    )
    description = StringField(
        'description', validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link', validators=[DataRequired()]
    )
    release_date = StringField(
        'release_date', validators=[DataRequired()]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    


class ActorForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    gender = StringField(
        'gender', validators=[DataRequired()]
    )
    age = StringField(
        'age',  validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link', validators=[DataRequired()]
    )
    description = StringField(
        'descripton'
    )
