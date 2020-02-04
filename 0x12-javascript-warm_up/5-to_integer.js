#!/usr/bin/node
const myVar = ['Not a number', 'Argument found', 'Arguments found'];
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log(myVar[0]);
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
