"""Models for Adoption Agency."""

from sqlalchemy import Column, Integer, String, ForeignKey, Table, func
from sqlalchemy.orm import relationship #See if I keep this import
from flask_sqlalchemy import SQLAlchemy
# from app import app

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

# Models

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(500), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

