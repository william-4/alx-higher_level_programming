#!/usr/bin/node

let obj = {
  type: 'object',
  value: 12
};
console.log(obj);

obj.incr = function () {
  this.value++;
};

obj.incr();
console.log(obj);
obj.incr();
console.log(obj);
obj.incr();
console.log(obj);
