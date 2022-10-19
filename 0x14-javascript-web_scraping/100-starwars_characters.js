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
  const len = actors.length;
  for (let idx = 0; idx < len; idx++) {
    const actorUrl = actors[idx];
    request(actorUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const info = JSON.parse(body);
      console.log(info.name);
    });
  }
});
