#!/usr/bin/node
exports.nbOccurences = (list, searchElement) => {
  let count = 0;
  list.forEach((element) => {
    if (element === searchElement) {
      count++;
    }
  });
  return count;
};
