import { readFileSync } from "fs";

const lines = readFileSync("input.txt", "utf-8").trim().split("\n\n");

const inputs = lines.splice(0, 1)[0].split(",").map(n => parseInt(n));
const players = lines.map(it => it.trim().split("\n").map(r => r.trim().split(" ").filter(e => e != "").map(e => ({ n: parseInt(e), m: false }))));
