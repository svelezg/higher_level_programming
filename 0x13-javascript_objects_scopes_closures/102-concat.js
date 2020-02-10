#!/usr/bin/node

const fs = require('fs');
const file1 = fs.readFileSync(process.argv[2], (err, data) => {
  if (err) throw err;
  return (data);
});
const file2 = fs.readFileSync(process.argv[3], (err, data) => {
  if (err) throw err;
  return (data);
});

fs.appendFile(process.argv[4], file1, function (err) {
  if (err) throw err;
});
fs.appendFile(process.argv[4], file2, function (err) {
  if (err) throw err;
});
