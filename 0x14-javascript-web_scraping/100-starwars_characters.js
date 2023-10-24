#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    for (const caracterURL of JSON.parse(body).characters) {
      request(caracterURL, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
