"""Adoption Agency application."""

from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from flask_migrate import Migrate  # Import Migrate

app = Flask(__name__)

# Configuration settings
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Caccolino5@localhost/adopt"
app.config["SECRET_KEY"] = "abcde12345"
app.config["DEBUG_TB_INTERCEPT_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# Initialize extensions
debug = DebugToolbarExtension(app)
connect_db(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Routes

# homepage displays all the pets
@app.route('/')
def homepage():
    """Lists the pets"""
    pets = Pet.query.all()
    return render_template('pets_list.html', pets=pets)

# Add pet form and form handling
@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Shows form to add a new pet and handles form submission.
    It includes validation:
    - If it doesn’t validate, it should re-render the form
    - If it does validate, it should create the new pet, and redirect to the homepage"""

    form = AddPetForm() # Makes an instance of 'AddPetForm'

    # Check if it's a 'post request' and validate the form (if the token is valid)
    if form.validate_on_submit():
        # Retrieve each field from the form and create a new Pet
        pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data,
            available = form.available.data == 'True' # Convert string to boolean
        )
       
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    
    else:
        return render_template('add_pet_form.html', form=form)
    
# Shows a pet and edit pet form
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_info_edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data == 'True'  # Convert to boolean

        db.session.commit()

        return redirect(url_for('pet_info_edit_pet', pet_id=pet_id))

    return render_template('pet.html', pet=pet, form=form)







