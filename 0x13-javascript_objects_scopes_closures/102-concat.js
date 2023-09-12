#!/usr/bin/node
// Write a script that concats 2 files
// (1)-> The file path of the first source file
// (2)-> The file path of the second source file
// (3)-> The file path of the destination

const fs = require('fs');

const x = fs.readFileSync(process.argv[2], 'utf8');

const y = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], (x + y));
