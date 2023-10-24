#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const fs = require('fs');
    const file = process.argv[3];
    fs.writeFile(file, body, 'utf8', (err, data) => {
      if (err) {
        return console.log(err);
      }
    });
  }
});
