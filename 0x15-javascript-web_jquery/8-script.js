$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (const movie in data.results) {
    $('UL#list_movies').append('<li>movie.title</li>');
  }
});
