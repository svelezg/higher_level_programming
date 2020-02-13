$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/films/?format=json',
    success: function (data) {
      const myResults = data.results;
      for (const result of myResults) {
        $('UL#list_movies').append('<li>' + result.title + '</li>');
      }
    }
  });
});
