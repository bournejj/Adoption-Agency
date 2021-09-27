from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Pet, db
from forms import AddPetForm, EditPetForm


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_pets():
    """return a list of all pets"""

    pets = Pet.query.all()

    return render_template('list_pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """show a form for adding a new pet"""

    form = AddPetForm()
    
    if form.validate_on_submit():

        name = form.pet_name.data
        species = form.Species.data
        photo = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo=photo, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:

         return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():

        pet.photo = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')

    return render_template('edit_pet.html', pet=pet, form=form)




