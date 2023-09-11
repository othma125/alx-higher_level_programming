#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const { argv } = require('process');
const x = parseInt(argv[2]);
const y = parseInt(argv[3]);
if (isNaN(x) || isNaN(y)) {
  console.log('NaN');
} else {
  console.log(add(x, y));
}
