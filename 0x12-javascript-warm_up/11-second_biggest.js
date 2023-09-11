#!/usr/bin/node
const { argv } = require('process');
const x = parseInt(argv[2]);
if (isNaN(x)) {
  console.log('0');
} else {
  let biggest = x;
  let second_biggest = x;
  for (let i = 2; i < argv.length; i++) {
    if (parseInt(argv[i]) > biggest) {
      second_biggest = biggest;
      biggest = parseInt(argv[i]);
    } else if (parseInt(argv[i]) > second_biggest) {
      second_biggest = parseInt(argv[i]);
    }
  }
  console.log(second_biggest);
}
