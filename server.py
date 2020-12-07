"""Server for Studio Ghibli Movie Tracker app."""

from flask import (Flask, render_template, request, flash, 
                    session, redirect, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os
from datetime import datetime

app = Flask(__name__)

app.secret_key = os.environ['APP_SECRET_KEY']
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Route to homepage. Redirect to login if user is not in session."""
    movies = crud.return_movies()
    if session.get('current_user'):
        return render_template('homepage.html', movies=movies)
    else:
        return redirect('/login')

@app.route('/<movie_id>')
def explore_movie(movie_id):
    """Display a movie's details."""

    movie = crud.return_movie_by_id(movie_id)
    director = crud.return_director_by_movie(movie_id)
    producer = crud.return_producer_by_movie(movie_id)
    site_rating = crud.return_movie_site_rating(movie_id)
    # reviews = crud.return_reviews_by_movie_id(movie_id)

    user_id = session.get('current_user')

    if user_id:
        rating = crud.get_rating_by_user_movie(user_id, movie_id)

        # check if movie is in user seen or watchlist
        seen = crud.is_seen(user_id, movie_id)
        watchlist = crud.is_watchlist(user_id, movie_id)
    else:
        rating = None
        seen = None
        watchlist = None

    return render_template('movie_details.html', movie=movie, director=director, producer=producer, site_rating=site_rating, rating=rating, seen=seen, watchlist=watchlist)

@app.route('/user_profile')
def view_current_user_profile():
    """Display a user profile."""

    user_id = session['current_user']
    user = crud.get_user_by_user_id(user_id)

    movies_watched_count = crud.get_movies_watched_count(user_id) #TODO: make func in crud file
    reviews_written_count = crud.get_reviews_written_count(user_id) #TODO: make func in crud file
    ratings_given_count = crud.get_ratings_given_count(user_id) #TODO: make func in crud file

    seenlist = crud.return_seenlist(user_id) #TODO: make func in crud file
    watchlist = crud.return_watchlist(user_id) #TODO: make func in crud file

    reviews = crud.return_reviews_by_user_id(user_id) #TODO: make func in crud file

    return render_template('user_profile.html', user=user, movies_watched_count=movies_watched_count, reviews_written_count=reviews_written_count,
    ratings_given_count=ratings_given_count, seenlist=seenlist, watchlist=watchlist, reviews=reviews)


@app.route('/submit_review<movie_id>', methods=['POST'])
def add_new_review(movie_id):
    """Adds user's new review to the db."""

    timestamp = datetime.now()
    user_id = session['current_user']
    review_content = request.form.get('new_review')

    crud.create_review(timestamp, user_id, movie_id, review_content)

    return redirect(f'/{movie_id}')

@app.route('/submit_rating<movie_id>', methods=['POST'])
def add_rating_for_user(movie_id):
    """Adds a user's rating to the db."""

    user_id = session['current_user']
    score = request.form.get('score')

    crud.create_rating(user_id, movie_id, score)

    return redirect(f'/{movie_id}')

@app.route('/submit_seen<movie_id>', methods=['POST'])
def add_movie_to_seen_for_user(movie_id):
    """Adds a movie to the seen list for the current user."""

    user_id = session['current_user']
    
    crud.create_movie_seen(user_id, movie_id)

    return redirect(f'/{movie_id}')

@app.route('/remove_from_seen<movie_id>', methods=['POST'])
def remove_movie_from_seen(movie_id):
    """Removes a movie from the seen list for the current user."""
    
    user_id = session['current_user']

    crud.remove_movie_seen(user_id, movie_id) #TODO: create func in crud file

    return redirect(f'/{movie_id}')

@app.route('/submit_watchlist<movie_id>', methods=['POST'])
def add_movie_to_watchlist_for_user(movie_id):
    """Adds a movie to the watchlist for a specific user."""

    user_id = session['current_user']
    
    crud.create_want_to_watch(user_id, movie_id)

    return redirect(f'/{movie_id}')

@app.route('/remove_from_watchlist', methods=['POST'])
def remove_movie_from_watchlist(movie_id):
    """Removes a movie from the watchlist for the current user."""

    user_id = session['current_user']

    print("*****REMOVE MOVEI FROM WATCHLIST WOO*****")

    crud.remove_movie_watchlist(user_id, movie_id)

    return redirect(f'/{movie_id}')

@app.route('/login')
def login_page():
    """Display login/create account page."""

    return render_template('login_page.html')

@app.route('/create_account', methods=['POST'])
def create_new_user_account():
    """Create a new user account."""
    
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    if crud.get_user_by_email(email):
        flash('An account with that email already exists. Please login!')
    else:
        if crud.get_user_by_username(username):
            flash('That username is taken. Please choose a different username :)')
        else:
            crud.create_user(username, email, password)
            flash('Account successfully created :D. Please login!')

    return redirect('/login')

@app.route('/login', methods=['POST'])
def login_user():
    """Logs a user in."""

    username_email = request.form.get('username_email')
    password = request.form.get('password')

    user = crud.get_user_by_email_username(username_email)

    if user:
        if user.password == password:
            session['current_user'] = user.user_id
            flash('Logged in!')
            return redirect('/')
        else:
            flash('Password incorrect. Please try again.')
            return redirect('/login')
    else:
        flash('Username or email incorrect. Please try again.')
        return redirect('/login')

@app.route('/logout', methods=['POST'])
def logout_user():
    """Logs a user out."""

    del session['current_user']
    flash('Logged out.')
    
    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)