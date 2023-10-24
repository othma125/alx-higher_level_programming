#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const task of tasks) {
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 0;
        }
        completed[task.userId] += 1;
      }
    }
    console.log(completed);
  }
});
