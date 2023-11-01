#!/usr/bin/node
/* global $ */
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (data) => {
  $.each(data.results, (i, movie) => {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  });
});
