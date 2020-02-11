#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let list = [];
    const films = JSON.parse(body).results;
    for (const film of films) {
      list = list.concat(film.characters);
    }
    const filterList = list.filter(x => x.includes('18'));
    console.log(filterList.length);
  }
});
