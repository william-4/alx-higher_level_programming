#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; row++) {
    let print = '';
    for (let col = 0; col < size; col++) print += 'X';
    console.log(print);
  }
}
