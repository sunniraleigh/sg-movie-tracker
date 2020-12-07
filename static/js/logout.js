// send post request for logging out

$('#logout-form').on('submit', (evt) => {
    evt.preventDefault();

    $.post('/logout', (response) => {
        alert(response)
    });
});