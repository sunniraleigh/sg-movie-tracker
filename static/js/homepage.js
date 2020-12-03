// send post request to server to get movie data and seen/watchlist statuses
// generate divs for each movie

$.get('/api/movies_data.json', (response) => {
    const data = response;

    const parsedData = JSON.parse('{"1":["movie_id":{}, "title":{}, "img_url":{}, "seenlist_status":{}, "watchlist_status":{}]}')
    
    // for (const movie of data) {

    //     const movie_card = `<div>${movie.title}</div>`

    //     $('body').append(
    //         <div class="movie-card">
    //             <p>movie.title</p>
    //         </div>
    //     )
    // }
});

// append divs to body