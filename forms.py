from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    '''allow users to add a pet'''

    name = StringField('Pet Name', validators=[InputRequired()],)
    species = SelectField('Species', choices=[('cat'),('dog'),('porcupine')],)
    photo_url = StringField('Photo Url', validators=[Optional(), URL()],)
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)],)
    notes = TextAreaField('Notes', validators=[Optional()],)


class EditPetForm(FlaskForm):
    '''allow users to edit a pet'''

    photo_url = StringField('Photo Url', validators=[Optional(), URL()],)
    notes = TextAreaField('Notes', validators=[Optional()],)
    available = BooleanField('Available?')

