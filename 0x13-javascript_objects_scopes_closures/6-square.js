#!/usr/bin/node

/* class square that inherits from rectangle */
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) row += c;
      console.log(row);
    }
  }
}

module.exports = Square;