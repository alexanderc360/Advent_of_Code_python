import os
import re

os.system("aocd 2023 3 > ./2023/day_3/input.txt")
os.system("aocd 2023 3 -e > ./2023/day_3/exampleAnswers.txt")
input = open("./2023/day_3/input.txt")
example = open("./2023/day_3/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

grid = [list(line.strip()) for line in workingData]
nums = []
buff = 0
part = False
check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j].isdigit():
            for x, y in check:
                if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]):
                    if grid[i + x][j + y] != '.' and not grid[i + x][j + y].isdigit():
                        part = True
            if buff == 0:
                buff = int(grid[i][j])
            else:
                buff = buff*10 + int(grid[i][j])
        if not grid[i][j].isdigit() or j == len(grid[0]) - 1:
            if buff > 0:
                nums.append((buff, part))
            buff = 0
            part = False
sum = 0
for n, p in nums:
    if p:
        sum += n
print(sum)
