#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const myError = 'NaN';
if (!process.argv[3] || isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(myError);
} else {
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
}
