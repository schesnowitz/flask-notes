from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100), unique=False)
    password = db.Column(db.String(100), unique=False)  
    note = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data = db.Column(db.String(10000), unique=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    
