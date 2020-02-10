#!/usr/bin/node
const numbers = require('./100-data').list;
console.log(numbers);
const newList = numbers.map(function (number, index) {
  return (number * index);
});

console.log(newList);
