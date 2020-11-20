"""CRUD operations."""

from model import db, connect_to_db, User, Movie, CastCrew, Rating, Review, MovieSeen, WantToWatch

# create a user
def create_user(username, email, password):
    """Create and return a user."""

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

# get user by user_id
def get_user_by_user_id(user_id):
    """Return a user by their user id."""

    return User.query.get(user_id)

# get user by email or username
def get_user_by_email_username(username_email):
    """Return a user by either their username or email."""

    if User.query.filter(User.username==username_email).first():
        return User.query.filter(User.username==username_email).first()
    
    if User.query.filter(User.email==username_email).first():
        return User.query.filter(User.username==username_email).first()

# get user by email
def get_user_by_email(email):
    """Returns a user by email."""

    return User.query.filter(User.email==email).first()

# get user by username
def get_user_by_username(username):
    """Returns a user by username."""

    return User.query.filter(User.username==username).first()

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

def return_movie_by_id(movie_id):
    """Return a single movie by id."""

    return Movie.query.get(movie_id)

def return_director_by_movie(movie_id):
    """Return the director of a movie."""

    return CastCrew.query.filter( (CastCrew.movie_id == movie_id) & (CastCrew.position == "director")).all()

def return_producer_by_movie(movie_id):
    """Return the producer of a movie."""

    return CastCrew.query.filter( (CastCrew.movie_id == movie_id) & (CastCrew.position == "producer") ).all()

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

def return_movie_site_rating(movie_id):
    """Return the site rating of a movie."""
    
    sum_rating = 0
    ratings = Rating.query.filter(Rating.movie_id==movie_id).all()

    for rating in ratings:
        if rating != None:
            sum_rating += rating.score
    
    return sum_rating/len(ratings) if len(ratings)!=0 else sum_rating

def get_rating_by_user_movie(user_id, movie_id):
    """Return a rating by user_id and movie_id."""

    return Rating.query.filter( (Rating.user_id==user_id) & (Rating.movie_id==movie_id)).first()

def get_ratings_given_count(user_id):
    """Return count of the number of ratings a user has given by user id."""

    ratings_given = Rating.query.filter(Rating.user_id==user_id).all()

    return len(ratings_given)

# create a review
def create_review(timestamp, user_id, movie_id, review_content):
    """Create and return a review."""

    review = Review(timestamp=timestamp, user_id=user_id, movie_id=movie_id, review_content=review_content)

    db.session.add(review)
    db.session.commit()

    return review

def return_reviews_by_movie_id(movie_id):
    """Return movie reviews by movie_id."""

    return Review.query.filter(Review.movie_id==movie_id).all()

def get_reviews_written_count(user_id):
    """Return count of movie reviews written by a user by user id."""

    reviews = Review.query.filter(Review.user_id==user_id).all()

    return len(reviews)

# set a movie to movieseen
def create_movie_seen(user_id, movie_id):
    """Create and return a movie that has been seen by a user."""

    movie_seen = MovieSeen(user_id=user_id, movie_id=movie_id)

    db.session.add(movie_seen)
    db.session.commit()

    return movie_seen

def is_seen(user_id, movie_id):
    """Checks to see if a user has seen a movie."""

    if MovieSeen.query.filter( (MovieSeen.user_id==user_id) & (MovieSeen.movie_id==movie_id) ).first():
        return True
    else:
        return False

def remove_movie_seen(user_id, movie_id):
    """Removes a movie from a user's seen list."""

    seen_movie = MovieSeen.query.filter( (MovieSeen.user_id==user_id) & (MovieSeen.movie_id==movie_id) ).first()

    db.session.delete(seen_movie)
    db.session.commit()

def get_movies_watched_count(user_id):
    """Return the count of movies the current user has watched."""

    seen_movies = MovieSeen.query.filter(MovieSeen.user_id==user_id).all()

    return len(seen_movies)

# set a movie to wanttowatch
def create_want_to_watch(user_id, movie_id):
    """Create and return a movie that a user wants to watch."""

    want_to_watch = WantToWatch(user_id=user_id, movie_id=movie_id)

    db.session.add(want_to_watch)
    db.session.commit()

    return want_to_watch

def is_watchlist(user_id, movie_id):
    """Checks to see if a user has seen a movie."""

    if WantToWatch.query.filter( (WantToWatch.user_id==user_id) & (WantToWatch.movie_id==movie_id) ).first():
        return True
    else:
        return False

def remove_movie_watchlist(user_id, movie_id):
    """Removes a movie from a user's watchlist."""

    # watchlist = WantToWatch.query.filter(WantToWatch.user_id==user_id).all()
    # print("THE WATCHLIST BEFORE DELETION!!!*****", watchlist) #before deletion

    watchlist_movie = WantToWatch.query.filter( (WantToWatch.user_id==user_id) & (WantToWatch.movie_id==movie_id) ).first()

    db.session.delete(watchlist_movie)
    db.session.commit()

    # print("THE WATCHLIST AFTER DELETION!!!*****", watchlist) #after deletion

if __name__ == '__main__':
    from server import app
    connect_to_db(app)