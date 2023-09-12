#!/usr/bin/node
// Write a class Square that defines a square and inherits from Square of 5-square.js
// You must use the class notation for defining your class and extends

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let b = 0; b < this.height; b++) console.log(c.repeat(this.width));
    }
  }
};
