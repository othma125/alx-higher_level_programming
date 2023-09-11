#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < num) {
    console.log('X'.repeat(num));
    i++;
  }
}
