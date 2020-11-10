"""Script to seed database."""

# Python standard libraries
import os
import json
from random import choice, randint
from datetime import datetime
from faker import Faker

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
movies_in_db = [] # an empty list just for testing
for n in range(10):
    title = fake.random_object_name()
    year_released = fake.year()
    overview = fake.text()
    duration = randint(100, 200)
    site_rating = randint(1,5)
    api_movie_id = randint(1000, 2000)
    image_url = fake.file_path()

    movie = crud.create_movie(title, year_released, overview, duration, 
                        site_rating, api_movie_id, image_url)
    
    movies_in_db.append(movie)

# CastCrew
positions = ['actor', 'director', 'producer']

# User
# Rating
# Review
# MovieSeen
# WantToWatch
