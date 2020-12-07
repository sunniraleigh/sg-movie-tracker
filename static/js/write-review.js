// creating a new review event handling

$('#new-review-text').on('focus', (evt) => {
    evt.preventDefault();

    const formValues = {
        new_review: $('#new-review-text').val(),
        movie_title: $('#movie-title').html()
    };

    console.log("IS THIS WORKING ****!!!!!", formValues)

    // $.post('/submit_review', formValues, (response) => {
    //     alert(response)
    // });

});