#!/usr/bin/node
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, 'utf8', (err, data) => {
      if (err) {
        return console.log(err);
      }
    });
  }
});
