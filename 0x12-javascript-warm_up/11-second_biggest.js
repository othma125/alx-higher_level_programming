#!/usr/bin/node
const { argv } = require('process');
const x = parseInt(argv[2]);
if (isNaN(x)) {
  console.log(0);
} else {
  let biggest = x;
  let secondBiggest = x;
  for (let i = 2; i < argv.length; i++) {
    if (parseInt(argv[i]) > biggest) {
      secondBiggest = biggest;
      biggest = parseInt(argv[i]);
    } else if (parseInt(argv[i]) > secondBiggest) {
      secondBiggest = parseInt(argv[i]);
    }
  }
  console.log(secondBiggest);
}
