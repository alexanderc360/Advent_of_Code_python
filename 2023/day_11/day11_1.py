import os

os.system("aocd 2023 11 > ./2023/day_11/input.txt")
os.system("aocd 2023 11 -e > ./2023/day_11/exampleAnswers.txt")
input = open("./2023/day_11/input.txt")
example = open("./2023/day_11/example.txt")

workingData = input  # change to try example
workingData = example  # change to try example

def rotate(grid):
    newGrid = []
    for i in range(len(grid[0])):
        buff = []
        for j in range(len(grid)):
            buff.append(grid[j][i])
        newGrid.append(buff.copy())
    return newGrid

def expand(grid):
    newGrid = []
    for i in range(len(grid)):
        newGrid.append(grid[i].copy())
        if '#' not in grid[i]:
            newGrid.append(grid[i].copy())
    return newGrid

expanded = rotate(expand(rotate(expand([list(line.strip()) for line in workingData]))))
galaxys = []
sum = 0
seen = set()

for i in range(len(expanded)):
    for j in range(len(expanded[0])):
        if expanded[i][j] == '#':
            galaxys.append((i, j))
print(galaxys)
for i in galaxys:
    for j in galaxys:
        if i != j and (i, j) not in seen and (j, i) not in seen:
            seen.add((i, j))
            sum += abs(i[0] - j[0]) + abs(i[1] - j[1])
print(sum)
