#!/usr/bin/node
function factoriel (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factoriel(n - 1);
  }
}
const { argv } = require('process');
const x = parseInt(argv[2]);
if (isNaN(x)) {
  console.log('1');
} else {
  console.log(factoriel(x));
}
