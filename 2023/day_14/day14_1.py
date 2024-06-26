import os

os.system("aocd 2023 14 > ./2023/day_14/input.txt")
os.system("aocd 2023 14 -e > ./2023/day_14/exampleAnswers.txt")

input = open("./2023/day_14/input.txt")
example = open("./2023/day_14/example.txt")

workingData = input  # uncomment to try input
# workingData = example  # uncomment to try example

board = dict(enumerate(workingData))
cube = {int(i): set() for i in board}
circ = {int(i): set() for i in board}

for row in board:
    cube[row].update([i for i in range(len(board[row].strip())) if board[row].strip()[i] == "#"])
    circ[row].update([i for i in range(len(board[row].strip())) if board[row].strip()[i] == "O"])

playing = True
while playing:
    change = False
    for i in range(1, len(board), 1):
        buff = circ[i].copy()
        for c in buff:
            if c not in circ[i -1] and c not in cube[i - 1]:
                circ[i].remove(c)
                circ[i - 1].add(c)
                change = True
    playing = change

load = 0
for i in circ:
    load += (len(circ) - i) * len(circ[i])
print(f"Answer: {load}")