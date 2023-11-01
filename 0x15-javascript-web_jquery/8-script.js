// Script that fetches and lists the title for all movies by using this URL
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  $('UL#list_movies').append('<li>' + data.results.title + '</li>');
});
