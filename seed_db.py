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
from model import Movie, User, CastCrew, Rating, Review, MovieSeen, WantToWatch
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
movies_in_db = [] # an empty list just for testing
for n in range(10):
    title = fake.name() # pull from SG API - title
    year_released = fake.year() # pull from SG API - release_date
    overview = fake.text() # pull from SG API - description
    duration = randint(100, 200) #IMDB API
    api_movie_id = fake.sentence() # SG API - id 
    image_url = fake.file_path() # IMDB API

    movie = crud.create_movie(title, year_released, overview, duration, 
                        site_rating, api_movie_id, image_url)
    
    movies_in_db.append(movie)

# Retrive movies from SG API
res = requests.get('https://ghibliapi.herokuapp.com/films')
search_results = res.json()

for movie in search_results:
    title = movie['title']
    year_released = movie['release_date']
    overview = movie['description']
    duration = 0
    api_movie_id = movie['id']
    image_url = 'tbd'
    
    movie = crud.create_movie(title, year_released, overview, duration, 
                        site_rating, api_movie_id, image_url)
    
    movies_in_db.append(movie)

# CastCrew
# 100 random crew members
positions = ['actor', 'director', 'producer']
for n in range(10):
    movie_id = choice(movies_in_db).movie_id
    name = fake.name()
    position = choice(positions)

    crud.create_cast_crew(movie_id, name, position)

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
    
    for n in range(2):
        timestamp = fake.past_datetime(start_date='-30d')
        movie_id = choice(movies_in_db).movie_id
        review_content = fake.text()

        crud.create_review(timestamp, user_id, movie_id, review_content)
    
    for n in range(3):
        movie_id = choice(movies_in_db).movie_id

        crud.create_movie_seen(user_id, movie_id)
    
    for n in range(3):
        movie_id = choice(movies_in_db).movie_id
        
        crud.create_want_to_watch(user_id, movie_id)

