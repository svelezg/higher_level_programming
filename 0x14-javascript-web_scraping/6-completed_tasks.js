#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body);
    const dict = {};
    for (let i = 0; i < results.length; i++) {
      if (results[i].userId in dict) {
        if (results[i].completed) {
          dict[results[i].userId] = dict[results[i].userId] + 1;
        }
      } else {
        if (results[i].completed) {
          dict[results[i].userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
