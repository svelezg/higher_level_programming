#!/usr/bin/node
let i;
const myVar = ['Not a number', 'C is fun', 'Arguments found'];
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log(myVar[0]);
} else {
  for (i = 0; i < process.argv[2]; i++) {
    console.log(myVar[1]);
  }
}
