// event handling and DOM manipulation for seenlist button

const button = $('#seenlist')

// $('#seenlist').on('click', () => {
//     // console.log('button clicked')

// });

button.click(() => {
    console.log('seen status changed')

    // console.log(button.attr(name))

    const movieId = {
        movie_id: 1
    }

    // manipulate DOM
    if (button.html() === "Add to seenlist"){
        button.html("Remove from seenlist")

        $.post('/remove_from_watchlist', movieId, (res) => {
            alert(res.movie_id)
        })
    
    } else {
        button.html("Add to seenlist")
    }
    // console.log(button.html())
    // button.html('Remove from seenlist')

    // define data to send to server
    // send post request with ajax?
})