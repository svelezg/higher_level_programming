#!/usr/bin/node

const fs = require('fs');

// Data which will write in a file.
const data = process.argv[3];

// Write data in 'process.argv[2]' .
fs.writeFile(process.argv[2], data, 'utf-8', (err) => {
// In case of a error throw err.
  if (err) throw err;
});
