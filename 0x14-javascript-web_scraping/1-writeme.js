#!/usr/bin/node
// Write a script that writes a string to a file
// The first argument is the file path

const fs = require('fs');

if (process.argv.length > 3) {
  fs.writeFile(process.argv[2], process.argv[3], (error) => {
    if (error) console.log(error);
  });
}
