// rename React funcs we want to use
const Router = ReactRouterDOM.BrowserRouter;
const { useHistory, useParams, Redirect, Switch, Prompt, Link, Route } = ReactRouterDOM;

function Homepage() {
    return (
        <div>
            This is the homepage and will display all the movies!
        </div>
    );
}

function LogIn() {
    return (
        <div>
            This is the log in page where users can create an account and login!
        </div>
    );
}

function UserProfile() {
    return (
        <div>
            This is the user profile page and will display certain information depending on the user.
        </div>
    )
}

function MovieDetails() {
    return (
        <div>
            This is the movie detail page and will display information about a certain movie.
        </div>
    )
}

function App() {
    return (
        <Router>
            <nav>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/movie_details">Movie Details</Link>
                    </li>
                    <li>
                        <Link to="/user_profile">Profile Page</Link>                        
                    </li>
                    <li>
                        <Link to="/login_page">Create an Account or Login</Link>                        
                    </li>
                </ul>
            </nav>
            <div>
                <Switch>

                    <Route path="/movie_details">
                        <MovieDetails />
                    </Route>
                    <Route path="/user_profile">
                        <UserProfile />
                    </Route>
                    <Route path="/login_page">
                        <LogIn />
                    </Route>

                    {/* Home route */}
                    <Route path="/">
                        <Homepage />
                    </Route>

                </Switch>
            </div>
        </Router>
    );
}

ReactDOM.render(<App />, document.getElementById("root"))