#!/usr/bin/node
// Write a script that prints x times “C is fun”

const x = Math.floor(Number(process.argv[2]));

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let b = 0; b < x; b++) {
    console.log('C is fun');
  }
}
