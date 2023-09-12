#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
fs.readFile(argv[2], 'utf8', function (err, data) {
  if (err) throw err;
  fs.readFile(argv[3], 'utf8', function (err, data2) {
    if (err) throw err;
    fs.writeFile(argv[4], data + data2, err => { if (err) throw err; });
  });
});
