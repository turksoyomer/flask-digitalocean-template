from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ExampleForm(FlaskForm):
    string_field = StringField('StringField', validators=[DataRequired('Örnek giriniz.')])
    submit_field = SubmitField('SubmitField')