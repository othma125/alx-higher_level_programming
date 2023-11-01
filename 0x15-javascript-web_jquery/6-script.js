#!/usr/bin/node
/* global $ */
$('DIV#update_header').click(() => {
  $('header').text('New Header!!!');
});
