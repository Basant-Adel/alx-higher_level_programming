#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence

const dict = require('./101-data.js').dict;

const n = {};

for (const key in dict) {
  if (n[dict[key]] === undefined) {
    n[dict[key]] = [];
  }
  n[dict[key]].push(key);
}

console.log(n);
