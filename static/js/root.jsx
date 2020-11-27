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

function LogInPage() {
    return (
        <div>
            This is the log in page where users can create an account and login!
            <p>Login here:</p>
            <LogIn />
            <p>Creaate a new account here:</p>
            <CreateAnAccount />
        </div>
    );
}

function LogIn() {

    const [usernameemail, setUserNameEmail] = React.useState('');
    const [password, setPassword] = React.useState('');

    function handleLogIn(evt) {
        evt.preventDefault();
        const data = {
            usernameemail: usernameemail,
            password: password
        };
        const options = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {'Content-Type': 'application/json'}
        };
        fetch('/api/login', options);
        // console.log('logged in maybe ***!!!! WOOW');
    }

    function handleUserNameEmailChange(evt) {
        setUserNameEmail(evt.target.value);
    }

    function handlePasswordChange(evt) {
        setPassword(evt.target.value);
    }

    return (
        // form for logging in
        <div>
            <form onSubmit={handleLogIn}>
                Username or email:
                <input value={usernameemail} onChange={handleUserNameEmailChange} type="text"></input>
                Password:
                <input value={password} onChange={handlePasswordChange} type="text"></input>
                <button>Login</button>
            </form>
        </div>
    );
}

function CreateAnAccount() {

    const [email, setEmail] = React.useState('');
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');
    let check_email = false

    function handleNewAccount() {
        evt.preventDefault();
        alert('submitted form')

        const data = {
            email: email,
            username: username,
            password: password
        };

        const options = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {'Content-Type': 'application/json'}
        };

        fetch('/api/create_account', options);
    }

    function handleEmailChange(evt) {
        setEmail(evt.target.value)
        // console.log(evt.target.value)
        // fetch data from backend to determine if email is already used
        const data = {
            email: email
        };

        const options = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {'Content-Type': 'application/json'}
        };
        fetch('/api/check_email', options)
        .then(response => response.json())
        .then(data => check_email = data)
        // is email is being used, set a var to True to help determine display below
    }

    function handleUsernameChange(evt) {
        setUsername(evt.target.value)
        // console.log(evt.target.value)
        // fetch data from backend to determine if username is already taken
        // if username is take, set a var to True which can help determine display below
    }

    function handlePasswordChange(evt) {
        setPassword(evt.target.value)
        // console.log(evt.target.value)
    }

    if (check_email == true) {
        return (
            // for creating an account
            <div>
                <form onSubmit={handleNewAccount}>
                    Email:
                    <input value={email} onChange={handleEmailChange} type="text"></input>
                    This email is already in use. Login or use a different email.
                    Username:
                    <input value={username} onChange={handleUsernameChange} type="text"></input>
                    Password:
                    <input value={password} onChange={handlePasswordChange} type="text"></input>
                    <button>Create a New Account</button>
                </form>
            </div>
        );
    } else {
        return (
            // for creating an account
            <div>
                <form onSubmit={handleNewAccount}>
                    Email:
                    <input value={email} onChange={handleEmailChange} type="text"></input>
                    Username:
                    <input value={username} onChange={handleUsernameChange} type="text"></input>
                    Password:
                    <input value={password} onChange={handlePasswordChange} type="text"></input>
                    <button>Create a New Account</button>
                </form>
            </div>
        );
    }
    // return (
    //     // for creating an account
    //     <div>
    //         <form onSubmit={handleNewAccount}>
    //             Email:
    //             <input value={email} onChange={handleEmailChange} type="text"></input>
    //             Username:
    //             <input value={username} onChange={handleUsernameChange} type="text"></input>
    //             Password:
    //             <input value={password} onChange={handlePasswordChange} type="text"></input>
    //             <button>Create a New Account</button>
    //         </form>
    //     </div>
    // );
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
                        <LogInPage />
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