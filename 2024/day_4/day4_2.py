# Part 2
from aocd import _impartial_submit

input = open("./2024/day_4/input.txt")
example = open("./2024/day_4/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example


# up-left, up-right, down-left, down-right
directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
rows, cols = len(workingData), len(workingData[0].strip())
answer = 0
for x in range(rows):
    for y in range(cols):
        if workingData[x][y] == 'A':
            count = 0
            for dx, dy in directions:
                if 0 < x < rows - 1 and 0 < y < cols - 1:
                    if workingData[x+dx][y+dy] == 'S':
                        if workingData[x-dx][y-dy] == 'M':
                            count += 1
            if count == 2:
                answer += 1

# uncomment when ready to submit
_impartial_submit(answer, day=4, year=2024)
