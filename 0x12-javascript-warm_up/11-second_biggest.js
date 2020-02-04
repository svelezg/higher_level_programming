#!/usr/bin/node
let i, second, max;
const myLength = process.argv.length;
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  max = parseInt(process.argv[2]);
  second = 0;
  for (i = 3; i < myLength; i++) {
    if (parseInt(process.argv[i]) > max) {
      second = max;
      max = parseInt(process.argv[i]);
      // console.log("max change   "+ max + " " + second);
    } else if (parseInt(process.argv[i]) !== max && parseInt(process.argv[i]) > second) {
      second = process.argv[i];
      // console.log("second change   " +max + " " + second);
    }
  }
  console.log(second);
}
