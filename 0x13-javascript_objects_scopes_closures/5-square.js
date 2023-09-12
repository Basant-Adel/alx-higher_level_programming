#!/usr/bin/node
// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
// You must use the class notation for defining your class and extends

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
