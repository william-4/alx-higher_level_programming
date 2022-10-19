#!/usr/bin/node
// Node.js script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');
const reqUrl = process.argv[2];
request(reqUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  const results = data.results;
  let moviesNum = 0;
  const antilles = '18';
  for (const i of results) {
    for (const j of i.characters) {
      if (j.search(antilles) > 0) { moviesNum++; }
    }
  }
  console.log(moviesNum);
});
