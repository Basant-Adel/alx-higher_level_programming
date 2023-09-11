#!/usr/bin/node
// Write a script that prints a square

const size = Math.floor(Number(process.argv[2]));

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let b = 0; b < size; b++) {
    let so = '';
    for (let n = 0; n < size; n++) so += 'X';
    console.log(so);
  }
}
