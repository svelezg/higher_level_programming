#!/usr/bin/node

const request = require('request');
const baseUrl = 'http://swapi.co/api/films/';
const url = baseUrl + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
