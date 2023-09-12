#!/usr/bin/node
module.exports.logMe = (item) => {
  if (this.count === undefined) {
    this.count = 0;
  }
  console.log(this.count + ': ' + item);
  this.count++;
};
