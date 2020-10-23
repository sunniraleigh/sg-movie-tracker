# Studio Ghibli Movie Tracker

## General Description

The Studio Ghibli Movie Tracker is like if you made a simpler MyAnimeList for just Studio Ghibli films. The SGMT allows the user to keep track of the Studio Ghibli films they’ve seen and also explore them further by reading about movie details etc.

---

## Features

### MVP
- General setup page where Users are prompted to signup or login.
- User can generate a unique list for themselves that stores which Studio Ghibli films they’ve seen
    - Users will have a page unique to them with the list of movies they’ve seen
    - They can scroll through an index of all Ghibli movies and add new movies to that list if they aren’t in the list
- User can view basic information about a movie such as description, director, producer, and character list.

### 2.0
- Expand wiki-like abilities of the app. Include more information on each movie, character in a movie, directors etc. Allows user to almost explore the Studio Ghibli universe by letting them learn more about locations, species, and other details of a film.

### Further Ideas
- User interaction, community capabilities
- Journal/review: users can write what they think about the movies they have seen which can be kept private for themselves or can be published for community forum?

---

## APIs/Data
- [Studio Ghibli Api](https://ghibliapi.herokuapp.com/#section/Studio-Ghibli-API)
    - Use Studio Ghibli Api to retrieve list of all Studio Ghibli movies and basic information about those movies (summary, director, producer, characters)
- [IMDb Api](https://developer.imdb.com/)
    - Use Api to retrive the following information:
        1. Budget and grossing of film
        2. Actor information
        3. Movie posters
