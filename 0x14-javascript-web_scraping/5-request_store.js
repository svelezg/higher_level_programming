#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    // Data which will write in a file.
    const data = body;
    // Write data in 'process.argv[2]' .
    fs.writeFile('loripsum', data, 'utf-8', (err) => {
      // In case of a error throw err.
      if (err) throw err;
    });
  }
});
