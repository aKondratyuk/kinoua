from app import db
from db import Base

class Movie(Base):
    __tablename__ = "movie"
    title = db.Column(db.String(255), primary_key=True)
    url = db.Column(db.String(1255), nullable=False, unique=True)
    imdbrating = db.Column(db.Float(10), nullable=False)
    ratingcount = db.Column(db.Float(10), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("director.director_id"), nullable=True)

    director = db.relationship("Director", backref="movie", lazy=True)

    def __init__(self):
        title = self.title
        url = self.url
        imdbrating = self.imdbrating
        ratingcount = self.ratingcount

class Director(Base):
    __tablename__ = "director"
    director_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    def __init__(self):
        first_name = self.first_name
        last_name = self.last_name