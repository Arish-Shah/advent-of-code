text = open("input.txt").read().split("\n\n")

entries = text[0].split(",")

def check(boards):
  for i, board in enumerate(boards):
    for row in board:
      if len(set(row)) == 1:
        return i
    for row in zip(*board):
      if len(set(row)) == 1:
        return i
  return None


boards = []
for board in text[1:]:
  boards.append([list(filter(None, x.split(" "))) for x in board.split("\n")])

for entry in entries:
  for board in boards:
    for row in board:
      if entry in row:
        row[row.index(entry)] = "X"
  i = check(boards)
  if i != None:
    s = 0
    for row in boards[i]:
      for item in row:
        if item != "X": s += int(item)
    break

part1 = int(entry) * s
print(part1)