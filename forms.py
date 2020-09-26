from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, AnyOf, URL


class MovieForm(FlaskForm):
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


class ActorForm(FlaskForm):
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
