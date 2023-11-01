#!/usr/bin/node
/* global $ */
$(document).ready(() => {
  $('DIV#red_header').click(() => {
    $('header').addClass('red');
  });
});
