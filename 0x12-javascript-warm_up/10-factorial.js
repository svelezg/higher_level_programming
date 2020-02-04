#!/usr/bin/node
function myFactorial (a) {
  if (!a || isNaN(a)) {
    return (1);
  } else if (a === 1) {
    return (1);
  } else {
    return (myFactorial(a - 1) * a);
  }
}

console.log(myFactorial(parseInt(process.argv[2])));
