#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    // console.log(films);
    let count = 0;
    const base = 'https://swapi.co/api/people/';
    const complete = base + '18/';
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.includes(complete)) { count += 1; }
    }
    console.log(count);
  }
});
