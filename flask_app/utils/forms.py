from flask_wtf import FlaskForm
from wtforms import (StringField)
from wtforms.validators import InputRequired, Length


class UserForm(FlaskForm):
    name = StringField('Имя', validators=[InputRequired(),
                                          Length(min=3, max=100)],
                       render_kw={"placeholder": "Arthur"})
    city = StringField('Город', validators=[InputRequired(),
                                            Length(min=3, max=100)],
                       render_kw={"placeholder": "Camelot"})
    username = StringField('Юзернейм', validators=[InputRequired(),
                                                   Length(min=5, max=100)],
                           render_kw={"placeholder": "@arthurfromcamelot"})
