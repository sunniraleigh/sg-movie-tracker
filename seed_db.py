"""Script to seed database."""

# Python standard libraries
import os
import json
from random import choice, randint
from datetime import datetime
from faker import Faker
import imdb
import requests

# App files
import model
import crud
import server

# Drop and re-create the db
os.system('dropdb movie_tracker')
os.system('createdb movie_tracker')

# Connect to db and create tables
model.connect_to_db(server.app)
model.db.create_all()

# Seed DB with fake data
fake = Faker()

# Movie
# Generate 10 random movies
movies_in_db = [] # an empty list for randomizing user data

# Retrive movies from SG API
res = requests.get('https://ghibliapi.herokuapp.com/films')
search_results = res.json()

# Create IMDb Object
ia = imdb.IMDb()

# Seed movies and cast_crew tables
for movie in search_results:
    movie_imdb = ia.search_movie(movie['title'])[0] # first movie in imdb db with title from sg api

    title = movie['title']
    year_released = movie['release_date']
    overview = movie['description']
    duration = movie_imdb.get('runtime', None)
    api_movie_id = movie['id']
    image_url = movie_imdb['full-size cover url']

    director = movie.get('director', None)
    producer = movie.get('producer', None)
    
    movie = crud.create_movie(title, year_released, overview, duration, api_movie_id, image_url)
    
    crud.create_cast_crew(movie.movie_id, director, 'director')
    crud.create_cast_crew(movie.movie_id, producer, 'producer')
    
    movies_in_db.append(movie)

# User
    # Rating
    # Review
    # MovieSeen
    # WantToWatch

# randomly generate 10 users each with 5 ratings and 2 reviews
# users also have 3 movies each on movieseen and watchlist
for n in range(10):
    username = fake.user_name()
    email = fake.email()
    password = "testpw"

    user = crud.create_user(username, email, password)
    user_id = user.user_id

    for n in range(5):
        movie_id = choice(movies_in_db).movie_id
        score = randint(1,5)

        crud.create_rating(user_id, movie_id, score)
    
    # for n in range(2):
    #     timestamp = fake.past_datetime(start_date='-30d')
    #     movie_id = choice(movies_in_db).movie_id
    #     review_content = fake.text()

    #     crud.create_review(timestamp, user_id, movie_id, review_content)
    
    for n in range(3):
        movie_id = choice(movies_in_db).movie_id

        crud.create_movie_seen(user_id, movie_id)
    
    for n in range(3):
        movie_id = choice(movies_in_db).movie_id
        
        crud.create_want_to_watch(user_id, movie_id)

