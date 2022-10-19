#!/usr/bin/node
// Node.js script that gets the contents of a
// webpage and stores it in a file.

const fs = require('fs');
const request = require('request');
const reqUrl = process.argv[2];
request(reqUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  }
}).pipe(fs.createWriteStream(process.argv[3], { encode: 'utf8' }));
