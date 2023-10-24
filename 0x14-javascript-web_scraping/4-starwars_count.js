#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const dataSet = JSON.parse(body).results;
    let count = 0;
    for (const data of dataSet) {
      const characters = data.characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) count++;
      }
    }
    console.log(count);
  }
});
