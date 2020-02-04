#!/usr/bin/node
let i;

let text = '';
const myError = 'Missing size';
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log(myError);
} else {
  for (i = 0; i < process.argv[2]; i++) {
    text += 'X';
  }
  for (i = 0; i < process.argv[2]; i++) {
    console.log(text);
  }
}
