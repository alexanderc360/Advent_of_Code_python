input = open("./2023/day_3/input.txt")
example = open("./2023/day_3/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

grid = [list(line.strip()) for line in workingData]


nums, gears = [], []
digits, sum = 0, 0
check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
numLocs = set()
partNums = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j].isdigit():
            if digits == 0:
                digits = int(grid[i][j])
            else:
                digits = digits*10 + int(grid[i][j])
            numLocs.add((i, j))
        if not grid[i][j].isdigit() or j == len(grid[0]) - 1:
            if digits > 0:
                nums.append((digits, numLocs))
            digits = 0
            numLocs = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '*':
            for x, y in check:
                if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]):
                    if grid[i + x][j + y].isdigit():
                        for n, locs in nums:
                            if (i + x, j + y) in locs:
                                partNums.add(n)
            gears.append(partNums)
            partNums = set()

sum = 0
for locs in gears:
    buff = 1
    if len(locs) == 2:
        for i in locs:
            buff *= i
        sum += buff
print(sum)
