from .. import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # func gets the current date and time
    # each user can have multiple notes so store a foreign key on the user object
    # referencing to the primary key of another table
    # Foreign key is used for one-to-many relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# defining a new database model
# define the name of the object and inherit it from db.Model
# since this is a User object, also inherit it from UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # every time we create a note, add that note into this
    # user's note relationship
    notes = db.relationship('Note')
