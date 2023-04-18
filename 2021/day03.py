from copy import deepcopy

d = open("input.txt").read().splitlines()
dc = deepcopy(d)

def count(arr, index):
  c0, c1 = 0, 0
  for j in range(len(arr)):
    if arr[j][i] == "1": c1 += 1
    else: c0 += 1
  return c0, c1

def remove(arr, index, val):
  if len(arr) == 1:
    return
  return [x for x in arr if x[index] == val]

part1 = ["", ""]
for i in range(len(d[0])):
  c0, c1 = count(d, i)
  if c0 > c1:
    part1[0] += "1"
    part1[1] += "0"
  else:
    part1[0] += "0"
    part1[1] += "1"

part1 = list(map(lambda x: int(x, 2), part1))
print(part1[0] * part1[1])

for i in range(len(d[0])):
  if len(d) == 1:
    break
  c0, c1 = count(d, i)
  if c0 > c1:
    d = remove(d, i, "1")
  else:
    d = remove(d, i, "0")

for i in range(len(dc[0])):
  if len(dc) == 1:
    break
  c0, c1 = count(dc, i)
  if c0 > c1:
    dc = remove(dc, i, "0")
  else:
    dc = remove(dc, i, "1")
part2 = int(d[0], 2) * int(dc[0], 2)
print(part2)