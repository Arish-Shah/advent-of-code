const lines = require("fs").readFileSync("input.txt", "utf8").trim().split("\n");

const part1 = lines.map(line => {
  const [l, w, h] = line.split("x")
  const smallest = Math.min(l*w, w*h, h*l);
  return 2*l*w + 2*w*h + 2*h*l + smallest;
}).reduce((curr, acc) => curr + acc, 0);

console.log(part1);
