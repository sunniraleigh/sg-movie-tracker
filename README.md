<h1 align="center">
    <img width=50% alt="studio-ghibli-logo" src="static/img/logo_login.png">
</h1>

The Studio Ghibli Tracker allows the user to keep track of the Studio Ghibli films they’ve seen, explore details about the film, and rate and review them.

[Watch a video demo of the app here!](https://www.youtube.com/watch?v=7IYSztzpgFQ)


# Content
- [Tech Stack](#tech-stack)
- [App Features](#app-features)

# <a name="tech-stack"></a> Tech Stack 

- Python
- JavaScript
- PostgreSQL
- SQLAlchemy
- jQuery
- Flask
- Jinja
- HTML
- CSS
- Bootstrap

# <a name="app-features"></a> App Features

## Login Page

When first entering the app, the user lands on the login page if they are not already logged in.

<h1 align="center">
    <img width=75% alt="login-page" src="static/img/login_page.png">
</h1>

### Create an Account
A user must first create an account with a unique username and email before engaging with the app.

If an email or username is already in the database, the user will get a warning.
<h1 align="center">
    <img width=75% alt="account-exists-warning" src="static/img/account_exists.png">
</h1>

### Login to Account
Once a user has an account, they can login.

If the email, username, or password is incorrect, the user will get a warning notifying them of the issue.
<h1 align="center">
    <img width=75% alt="password-incorrect-warning" src="static/img/password_incorrect.png">
    <img width=75% alt="useremail-incorrect-warning" src="static/img/user_email_incorrect.png">
</h1>

## Homepage
On the homepage, users can scroll through the different Studio Ghibli films sorted by release date.
<h1 align="center">
    <img width=75% alt="password-incorrect-warning" src="static/img/user_email_incorrect.png">
</h1>

## Movie Details

Each movie has its own details page.
<h1 align="center">
    <img width=75% alt="movie-details-page-gif" src="static/img/site-demo.gif">
</h1>

A user can rate the movie on a scale from 1 to 5. This rating will influence the overall site rating.
<h1 align="center">
    <img width=50% alt="rating-feature" src="static/img/rating_form.png">
</h1>

A user can add and remove the movie from their Watch and Seen lists.

<h1 align="center">
    <img width=25% alt="add-feature" src="static/img/add_button.png">
    <img width=25% alt="remove-feature" src="static/img/remove_button.png">
</h1>

A user can write and read reviews of the movie.

<h1 align="center">
    <img width=75% alt="write-review-feature" src="static/img/write_review.png">
</h1>

## User Profile

Each user has their own profile page where they can view their statistics, their Watch and Seen lists, and reviews they've written.

<h1 align="center">
    <img width=75% alt="user-profile-screenshot1" src="static/img/user_profile1.png">
    <img width=75% alt="user-profile-screenshot2" src="static/img/user_profile2.png">
</h1>

---

Thank you for reading about the Studio Ghibli Movie Tracker :)