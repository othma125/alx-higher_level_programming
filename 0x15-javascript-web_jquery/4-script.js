#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $('DIV#toggle_header').click(() => {
    $('header').toggleClass('red green');
  });
});
