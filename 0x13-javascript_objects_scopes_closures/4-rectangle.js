#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let text = '';
    for (let i = 0; i < this.width; i++) {
      text += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(text);
    }
  }

  rotate () {
    let aux1 = 0;
    let aux2 = 0;
    aux1 = this.width;
    aux2 = this.height;
    this.width = aux2;
    this.height = aux1;
  }

  double () {
    let aux1 = 0;
    let aux2 = 0;
    aux1 = this.width;
    aux2 = this.height;
    this.width = aux1 * 2;
    this.height = aux2 * 2;
  }
}

module.exports = Rectangle;
