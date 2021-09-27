from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    """form for adding a new pet"""

    pet_name = StringField('Pet Name')
    Species = StringField('Species', validators=[AnyOf(values=['cat','dog','porcupine'], message='wrong species')])
    photo_url = StringField('Photo URL')
    age = FloatField('Age', validators=[NumberRange(min=0,max=30, message="Age must be between 0-30")])
    notes = StringField('Notes')
    available = BooleanField('Availabile')

class EditPetForm(FlaskForm):
    """form for adding a new pet"""

    
    photo_url = StringField('Photo URL')
    notes = StringField('Notes')
    available = BooleanField('Availabile')



