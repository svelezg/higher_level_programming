#!/usr/bin/node

const request = require('request');

const base = 'http://swapi.co/api/films/';
const url = base + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    }
  }
});
