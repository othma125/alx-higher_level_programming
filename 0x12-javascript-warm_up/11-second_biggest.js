#!/usr/bin/node
const { argv } = require('process');
if (argv.length < 4) {
  console.log(0);
} else {
  let biggest = Number.NEGATIVE_INFINITY;
  let secondBiggest = biggest;
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
