// login form event handling

$('#login-form').on('submit', (evt) => {
    evt.preventDefault();

    const formValues = {
        'username_email': $('#login-username-email').val(),
        'password': $('#login-password').val()
    };

    $.post('/login', formValues, (response) => {
        alert(response)
    })
})