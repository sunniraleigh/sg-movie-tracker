"""Server for Studio Ghibli Movie Tracker app."""

from flask import (Flask, render_template, request, flash, 
                    session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os

app = Flask(__name__)

app.secret_key = os.environ['APP_SECRET_KEY']
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Route to homepage."""

    movies = crud.return_movies()

    return render_template('homepage.html', movies=movies)

@app.route('/<movie_id>')
def explore_movie(movie_id):
    """Display a movie's details."""

    movie = crud.return_movie_by_id(movie_id)
    director = crud.return_director_by_movie(movie_id)
    producer = crud.return_producer_by_movie(movie_id)
    site_rating = crud.return_movie_site_rating(movie_id)
    # reviews = crud.return_reviews_by_movie_id(movie_id)

    return render_template('movie_details.html', movie=movie, director=director, producer=producer, site_rating=site_rating)

@app.route('/login')
def login_page():
    """Display login/create account page."""

    return render_template('login_page.html')

@app.route('/login', methods=['POST'])
def login_user():
    """Logs a user in."""

    username_email = request.form.get('username_email')
    password = request.form.get('password')

    user = crud.get_user_by_email_username(username_email)

    if user:
        if user.password == password:
            session['current_user'] = user.user_id
            flash("Logged in!")
            return redirect('/')
        else:
            flash("Password incorrect. Please try again.")
            return redirect('/login')
    else:
        flash("Username or email incorrect. Please try again")
        return redirect('/login')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)