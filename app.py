import os

from flask import Flask, request, render_template, session
from flask_sqlalchemy import SQLAlchemy

from sql_operations import get_all_data
from db import Base
from db import db_string

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Movie

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/movies")
def movie():
    movies = get_all_data(Movie)
    #movies = Movie.query.all()
    return render_template("movie.html", movies=movies)

if __name__ == '__main__':
    app.run()
