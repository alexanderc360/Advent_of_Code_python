input = open("./2023/day_11/input.txt")
example = open("./2023/day_11/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

def rotate(grid):
    newGrid = []
    for i in range(len(grid[0])):
        buff = []
        for j in range(len(grid)):
            buff.append(grid[j][i])
        newGrid.append(buff.copy())
    return newGrid

cols, rows = set(), set()
grid = [list(line.strip()) for line in workingData]
galaxys = []
sum, growth = 0, 1000000
seen = set()

for i in range(len(grid)):
    if '#' not in grid[i]:
        rows.add(i)
for i in range(len(rotate(grid))):
    if '#' not in rotate(grid)[i]:
        cols.add(i)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        newX, newY = i, j
        if grid[i][j] == '#':
            for k in rows:
                if i > k:
                    newX += growth - 1
            for k in cols:
                if j > k:
                    newY += growth - 1
            galaxys.append((newX, newY))

for i in galaxys:
    for j in galaxys:
        if i != j and (i, j) not in seen and (j, i) not in seen:
            seen.add((i, j))
            sum += (abs(i[0] - j[0]) + abs(i[1] - j[1]))
print(sum)
