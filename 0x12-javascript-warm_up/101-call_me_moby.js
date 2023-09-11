#!/usr/bin/node
// Write a function that executes x times a function
// The function must be visible from outside

exports.callMeMoby = function (x, theFunction) {
  for (let b = 0; b < x; b++) theFunction();
};
