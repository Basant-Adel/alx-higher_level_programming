#!/usr/bin/node
// Write a script that prints the number of movies
// where the character “Wedge Antilles” is present

const request = require('request');

const url = process.argv[2];
if (!url) process.exit();
request.get(url, (error, response, body) => {
  if (!error) {
    const count = body.split('/people/18/').length - 1;
    console.log(count);
  }
});
