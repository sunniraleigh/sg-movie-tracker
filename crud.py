"""CRUD operations."""

from model import db, connect_to_db, User, Movie, CastCrew, Rating, Review, MovieSeen, WantToWatch

# create a user
def create_user(username, email, password):
    """Create and return a user."""

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

# create a movie
def create_movie(title, year_released, overview, duration, api_movie_id, image_url):
    """Create and return a movie."""

    movie = Movie(title=title, year_released=year_released, overview=overview, duration=duration, api_movie_id=api_movie_id, image_url=image_url)

    db.session.add(movie)
    db.session.commit()

    return movie

def return_movies():
    """Return all movies."""

    return Movie.query.all()

# create a cast or crew member
def create_cast_crew(movie_id, name, position):
    """Create and return a cast or crew member."""

    cast_crew = CastCrew(movie_id=movie_id, name=name, position=position)

    db.session.add(cast_crew)
    db.session.commit()

    return cast_crew

# create a rating
def create_rating(user_id, movie_id, score):
    """Create and return a rating."""

    rating = Rating(user_id=user_id, movie_id=movie_id, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

# create a review
def create_review(timestamp, user_id, movie_id, review_content):
    """Create and return a review."""

    review = Review(timestamp=timestamp, user_id=user_id, movie_id=movie_id, review_content=review_content)

    db.session.add(review)
    db.session.commit()

    return review

# set a movie to movieseen
def create_movie_seen(user_id, movie_id):
    """Create and return a movie that has been seen by a user."""

    movie_seen = MovieSeen(user_id=user_id, movie_id=movie_id)

    db.session.add(movie_seen)
    db.session.commit()

    return movie_seen

# set a movie to wanttowatch
def create_want_to_watch(user_id, movie_id):
    """Create and return a movie that a user wants to watch."""

    want_to_watch = WantToWatch(user_id=user_id, movie_id=movie_id)

    db.session.add(want_to_watch)
    db.session.commit()

    return want_to_watch

if __name__ == '__main__':
    from server import app
    connect_to_db(app)