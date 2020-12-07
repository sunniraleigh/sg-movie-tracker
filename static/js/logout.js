// send post request for logging out

$('#logout-btn').on('click', (evt) => {
    evt.preventDefault();

    $.post('/logout', (response) => {
        alert(response)
    });
});