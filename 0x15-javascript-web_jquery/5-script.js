#!/usr/bin/node
/* global $ */
$('DIV#add_item').click(() => {
  $('UL.my_list').append('<li>Item</li>');
});
