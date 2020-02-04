#!/usr/bin/node
const myVar = ['No argument', 'Argument found', 'Arguments found'];

if (!process.argv[2]) {
  console.log(myVar[0]);
} else {
  console.log(process.argv[2]);
}
