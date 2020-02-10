#!/usr/bin/node
const SquareBase = require('./5-square');
class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let text = '';
    for (let i = 0; i < this.width; i++) {
      text += c;
    }
    for (let j = 0; j < this.width; j++) {
      console.log(text);
    }
  }
}

module.exports = Square;
