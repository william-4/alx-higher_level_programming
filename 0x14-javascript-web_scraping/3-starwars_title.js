#!/usr/bin/node
// Node.js script that prints the title of a Star Wars
// movie where the episode number matches a given integer.

const request = require('request');
const reqUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(reqUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
