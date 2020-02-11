#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, 'utf-8', (err) => {
      // In case of a error throw err.
      if (err) throw err;
    });
  }
});
