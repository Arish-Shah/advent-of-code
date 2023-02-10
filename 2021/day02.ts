import { readFileSync } from "fs";

let part1 = { x: 0, y: 0 };
let part2 = { x: 0, y: 0, aim: 0 };

readFileSync("input.txt", "utf8").trim().split("\n").forEach(l => {
  const [direction, amount] = l.split(" ");
  switch(direction) {
    case "forward":
      part1.x += +amount;
      part2.x += +amount;
      part2.y += (part2.aim * +amount);
      break;
    case "up":
      part1.y -= +amount;
      part2.aim -= +amount;
      break;
    case "down":
      part1.y += +amount;
      part2.aim += +amount;
      break;
  }
});

console.log(part1.x * part1.y);
console.log(part2.x * part2.y);
