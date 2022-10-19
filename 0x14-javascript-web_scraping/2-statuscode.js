#!/usr/bin/node
// Node.js script that displays the status code of a GET request.

const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', response && response.statusCode);
});
