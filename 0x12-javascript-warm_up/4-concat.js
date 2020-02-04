#!/usr/bin/node
const myVar = ['No arguments', 'Argument found', 'Arguments found'];
if (!process.argv[3]) {
  console.log(myVar[0]);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
