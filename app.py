from flask import Flask, render_template, redirect,url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'asfdsfds'

connect_db(app)
db.create_all()

@app.route('/')
def list_pets():
    '''show a list of all pets on database'''

    pets = Pet.query.all()

    return render_template('pet_list.html', pets=pets)

@app.route('/add',methods=['GET' , 'POST'])
def add_pets():
    '''add a pet and redirect back to homepage or show form to try again'''

    form = AddPetForm()

    if form.validate_on_submit():
        name=form.name.data,
        species=form.species.data,
        photo_url=form.photo_url.data,
        age=form.age.data,
        notes=form.notes.data
        
        pets = Pet(name=name,
                      species=species,
                      photo_url=photo_url,
                      age=age,
                      notes=notes)
        
        db.session.add(pets)
        db.session.commit()

        return redirect('/')

    else:

        return render_template('add_pet.html',form=form)

@app.route('/<int:pet_id>', methods=['GET','POST'])
def edit_pets(pet_id):
    '''present a form to edit pet information and redirect if edits allowed'''

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
        db.session.commit()

        return redirect('/')
    else:
        return render_template('edit_pet.html',form=form,pet=pet)



        


