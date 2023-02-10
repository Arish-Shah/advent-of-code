import { readFileSync } from "fs";

const lines = readFileSync("input.txt", "utf-8").trim().split("\n");
let o2 = [...lines];
let co2 = [...lines];

let gamma = "";
let epsilon = "";

function getCount(items: string[], index: number) {
  const count = [0, 0];
  for (let item of items) {
    count[+item[index]]++;
  }
  return count;
}

// part 1
for (let i = 0; i < lines[0].length; i++) {
  const count = getCount(lines, i);

  if (count[0] > count[1]) {
    gamma += "0";
    epsilon += "1";
  } else {
    gamma += "1";
    epsilon += "0";
  }
}

const part1 = parseInt(gamma, 2) * parseInt(epsilon, 2);
console.log(part1);

// part 2
for (let i = 0; i < lines[0].length; i++) {
  const o2count = getCount(o2, i);
  const co2count = getCount(co2, i);

  if (o2.length > 1) {
    if (o2count[0] > o2count[1]) o2 = o2.filter(item => +item[i] == 0);
    else o2 = o2.filter(item => +item[i] == 1);
  }

  if (co2.length > 1) {
    if (co2count[0] > co2count[1]) co2 = co2.filter(item => +item[i] == 1);
    else co2 = co2.filter(item => +item[i] == 0);
  }
}

const part2 = parseInt(o2[0], 2) * parseInt(co2[0], 2);
console.log(part2);
