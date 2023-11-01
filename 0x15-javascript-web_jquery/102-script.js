#!/usr/bin/node
/* global $ */
const url = 'https://www.fourtonfish.com/hellosalut/hello/';

$(document).ready(() => {
  $('#btn_translate').click(() => {
    const langCode = $('#language_code').val();
    $.get(`${url}?lang=${langCode}`, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
