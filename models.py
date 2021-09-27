from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model): 

    __tablename__ = 'adoption-pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column (db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo = db.Column(db.String)
    age = db.Column(db.Integer)
    notes = db.Column (db.String)
    available = db.Column(db.Boolean, nullable=False)

    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or GENERIC_IMAGE





   