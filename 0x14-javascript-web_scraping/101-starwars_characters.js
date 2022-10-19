#!/usr/bin/node
// Node.js script that prints all characters of a Star Wars movie

const request = require('request');
const reqUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(reqUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  const actors = data.characters;
  printactors(actors, 0);
});

function printactors (actors, idx) {
  if (idx === actors.length) {
    return;
  }
  request(actors[idx], (err, response, body) => {
    if (err) {
      console.error(err);
    }
    console.log(JSON.parse(body).name);
    printactors(actors, idx + 1);
  });
}
