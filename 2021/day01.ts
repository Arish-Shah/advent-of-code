import { readFileSync } from "fs";

let part1 = 0, part2 = 0;

const lines = readFileSync("input.txt", "utf8").trim().split("\n").map(l => +l);

for (let i = 1; i < lines.length; i++) {
  if (lines[i] > lines[i - 1]) part1++;
}

let prevSum = lines[0] + lines[1] + lines[2];
for (let i = 1; i < lines.length; i++) {
  let currentSum = lines[i] + lines[i + 1] + lines[i + 2];
  if (currentSum > prevSum) part2++;
  prevSum = currentSum;
}

console.log(part1);
console.log(part2);
