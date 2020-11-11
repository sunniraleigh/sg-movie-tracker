"""Models for Studio Ghibli movies tracker app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# --

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(20), unique = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    ratings = db.relationship('Rating')
    reviews = db.relationship('Review')
    movies_seen = db.relationship('MovieSeen')
    want_to_watch = db.relationship('WantToWatch')

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'

class Movie(db.Model):
    """A movie."""

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    year_released = db.Column(db.String(4))
    overview = db.Column(db.Text)
    duration = db.Column(db.Integer)
    api_movie_id = db.Column(db.Integer)
    image_url = db.Column(db.String)

    cast_crew = db.relationship('CastCrew')
    ratings = db.relationship('Rating')
    reviews = db.relationship('Review')
    movies_seen = db.relationship('MovieSeen')
    want_to_watch = db.relationship('WantToWatch')

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'

class CastCrew(db.Model):
    """A cast or crew member of a movie."""

    __tablename__ = 'cast_crew'

    cc_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    name = db.Column(db.String)
    position = db.Column(db.String)

    movies = db.relationship('Movie')

    def __repr__(self):
        return f'<CastCrew cc_id={self.cc_id} name={self.name}>'

class Rating(db.Model):
    """A rating."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    score = db.Column(db.Integer)

    users = db.relationship('User')
    movies = db.relationship('Movie')

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.score}>'

class Review(db.Model):
    """A user review."""

    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    review_content = db.Column(db.Text)

    users = db.relationship('User')
    movies = db.relationship('Movie')

    def __repr__(self):
        return f'<Review review_id={self.review_id} user_id={self.user_id} movie_id={self.movie_id}>'

class MovieSeen(db.Model):
    """A movie that has been watched by a user."""

    __tablename__ = 'movies_seen'

    movie_seen_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))

    users = db.relationship('User')
    movies = db.relationship('Movie')

    def __repr__(self):
        return f'<MovieSeen movie_seen_id={self.movie_seen_id} user_id={self.user_id} movie_id={self.movie_id}>'

class WantToWatch(db.Model):
    """A movie that a user wants to watch."""

    __tablename__ = 'want_to_watch'

    want_to_watch_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))

    users = db.relationship('User')
    movies = db.relationship('Movie')

    def __repr__(self):
        return f'<WantToWatch want_to_watch_id={self.want_to_watch_id} user_id={self.user_id} movie_id={self.movie_id}>'

# --

def connect_to_db(flask_app, db_uri='postgresql:///movie_tracker', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)