#!/usr/bin/node
const request = require('request');
const id = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else console.log(JSON.parse(body).title);
});
