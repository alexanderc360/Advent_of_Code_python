# Part 1
import os
from aocd import _impartial_submit

os.system("aocd 2024 6 > ./2024/day_6/input.txt")
os.system("aocd 2024 6 -e > ./2024/day_6/exampleAnswers.txt")

input = open("./2024/day_6/input.txt")
example = open("./2024/day_6/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example

grid = {}
lenX, lenY = len(workingData), len(workingData[0].strip())
for line in workingData:
    if '^' in line:
        x, y = len(grid), line.find('^')
    grid[len(grid)] = list(line.strip())

visited = set()
# up, right, down, left
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d, dX, dY = 0, 0, 0
while 0 <= x + dX < lenX and 0 <= y + dY < lenY:
    dX, dY = dirs[d % 4]
    if grid[x + dX][y + dY] == '#':
        d += 1
    else:
        visited.add((x, y))
        x += dX
        y += dY

answer = len(visited) + 1
print(answer)
# uncomment when ready to submit
# _impartial_submit(answer, day=6, year=2024)
