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