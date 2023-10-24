#!/usr/bin/node
// Write a script that gets the contents of
// a webpage and stores it in a file

const fs = require('fs');

const request = require('request');

if (process.argv.length > 3) {
  request.get(process.argv[2], (error, resopnse, body) => {
    if (error) console.log(error);
    else {
      fs.writeFile(process.argv[3], body, 'utf8', (error) => {
        if (error) console.log(error);
      });
    }
  });
}
