const line = require("fs").readFileSync("input.txt", "utf8");

let part1 = 0, part2 = 0, basement_found = false;

[...line].forEach((ch, i) => {
  if (ch == "(")
    part1 += 1
  else if (ch == ")")
    part1 -= 1

  if (part1 == -1 && !basement_found) {
    part2 = i + 1;
    basement_found = true;
  }
});

console.log(part1);
console.log(part2);
