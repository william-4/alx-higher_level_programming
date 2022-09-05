#!/usr/bin/node

const number = Math.floor(Number(process.argv[2]));
console.log(isNan(number) ? 'Not a number' : `My number: ${num}`);
