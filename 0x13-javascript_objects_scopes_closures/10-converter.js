#!/usr/bin/node
exports.converter = (base) => {
  return (num) => {
    return num.toString(base);
  };
};
