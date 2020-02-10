#!/usr/bin/node
const theDict = require('./101-data').dict;
const theEntries = Object.entries(theDict);
const theValues = Object.values(theDict);
const newDictKeys = Array.from(new Set(theValues));

const newDict = {};
for (const index in newDictKeys) {
  const list = [];
  for (const indexKey in theEntries) {
    if (theEntries[indexKey][1] === newDictKeys[index]) {
      list.push(theEntries[indexKey][0]);
    }
  }
  newDict[newDictKeys[index]] = list;
}
console.log(newDict);
