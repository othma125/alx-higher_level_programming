#!/usr/bin/node
$(document).ready(() => {
  $('DIV#toggle_header').click(() => {
    $('header').toggleClass('red green');
  });
});
