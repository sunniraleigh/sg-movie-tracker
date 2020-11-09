"""Models for Studio Ghibli movies tracker app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# --

class User(db.model):
    """A user."""

    __tablename__ = 'users'

    # define columns

    def __repr__(self):
        return f'<>'

class Movie(db.model):
    """A movie."""

    __tablename__ = 'movies'

    # define columns

    def __repr__(self):
        return f'<>'

class CastCrew(db.model):
    """A cast or crew member of a movie."""

    __tablename__ = 'cast_crew'

    # define columns

    def __repr__(self):
        return f'<>'

class Rating(db.model):
    """A rating."""

    __tablename__ = 'ratings'

    # define columns

    def __repr__(self):
        return f'<>'

class Review(db.model):
    """A user review."""

    __tablename__ = 'reviews'

    # define columns

    def __repr__(self):
        return f'<>'

class MovieSeen(db.model):
    """A movie that has been watched by a user."""

    __tablename__ = 'movies_seen'

    # define columns

    def __repr__(self):
        return f'<>'

class WantToWatch(db.model):
    """A movie that a user wants to watch."""

    __tablename__ = 'want_to_watch'

# --

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)