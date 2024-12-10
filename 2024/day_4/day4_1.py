# Part 1
import os
from aocd import _impartial_submit

# os.system("aocd 2024 4 > ./2024/day_4/input.txt")
# os.system("aocd 2024 4 -e > ./2024/day_4/exampleAnswers.txt")

input = open("./2024/day_4/input.txt")
example = open("./2024/day_4/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example

answer = 0
rows, cols = len(workingData), len(workingData[0].strip())
# up-left, up, up-right, left, right, down-left, down, down-right
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]

for x in range(rows):
    for y in range(cols):
        if workingData[x][y] == 'X':
            for dx, dy in directions:
                if 0 <= x + 3*dx < rows and 0 <= y + 3*dy < cols:
                    if workingData[x + dx][y + dy] == 'M':
                        if workingData[x + 2*dx][y + 2*dy] == 'A':
                            if workingData[x + 3*dx][y + 3*dy] == 'S':
                                answer += 1

# uncomment when ready to submit
_impartial_submit(answer, day=4, year=2024)
