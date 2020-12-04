// create account form event handling

$('#create-account-form').on('submit', (evt) => {
    evt.preventDefault();

    const formValues = {
        'email': $('#create-account-email').val(),
        'username': $('#create-account-username').val(),
        'password': $('#login-password').val()
    };

    $.post('/create_account', formValues, (response) => {
        alert(response)
    })
})