#!/usr/bin/node
// Write a class Rectangle that defines a rectangle
// You must use the class notation for defining your class

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
};
