#!/usr/bin/node
const request = require('request');
const names = [];
const printNames = (characters, i) => {
  if (i === characters.length) {
    return;
  }
  request(characters[i], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      names.push(JSON.parse(body).name);
      printNames(characters, i + 1);
    }
    if (i === characters.length - 1) {
      names.forEach((name) => console.log(name));
    }
  });
};

request(
  'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  (err, response, body) => {
    if (err) {
      console.error(err);
    } else {
      const characters = JSON.parse(body).characters;
      printNames(characters, 0);
    }
  }
);
