from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, AnyOf, URL

class MovieForm(Form):
    title = StringField(
        'title', validators=[DataRequired()]
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