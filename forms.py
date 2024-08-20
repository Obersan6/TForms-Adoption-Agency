"""Pets forms."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, URL, NumberRange, Optional

# classes

# Class to add a new pet
class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[DataRequired()])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[DataRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', validators=[Length(max=500)])
    available = SelectField('Available', choices=[('True', 'Available'), ('False', 'Unavailable')], validators=[DataRequired()])

# Class to edit some fields of a pet
class EditPetForm(FlaskForm):
    """Only edits Photo URL, Notes, and Available fields"""
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Length(max=500)])
    available = SelectField('Available', choices=[('True', 'Available'), ('False', 'Unavailable')], validators=[DataRequired()])








# STEP 6: Add Display/Edit Form

# Make a page that shows some information about the pet:

# - Name
# - Species
# - Photo, if present
# - Age, if present

# It should also show a form that allows us to edit this pet:

# - Photo URL
# - Notes
# - Available

# This should be at the URL `/[pet-id-number]`. Make the homepage link to this.
