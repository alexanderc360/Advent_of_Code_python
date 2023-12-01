def lowPoint(row, col, grid):
    low = True
    buff = grid[row][col]

    if row == 0:
        if col == 0:
            if buff >= grid[row + 1][col] or buff >= grid[row][col + 1]:
                low = False
        elif col == len(grid[0]) - 1:
            if buff >= grid[row + 1][col] or buff >= grid[row][col - 1]:
                low = False
        else:
            if buff >= grid[row + 1][col] or buff >= grid[row][col + 1] or buff >= grid[row][col - 1]:
                low = False
    elif row == len(grid) - 1:
        if col == 0:
            if buff >= grid[row - 1][col] or buff >= grid[row][col + 1]:
                low = False
        elif col == len(grid[0]) - 1:
            if buff >= grid[row - 1][col] or buff >= grid[row][col - 1]:
                low = False
        else:
            if buff >= grid[row - 1][col] or buff >= grid[row][col + 1] or buff >= grid[row][col - 1]:
                low = False
    else:
        if col == 0:
            if buff >= grid[row - 1][col] or buff >= grid[row + 1][col] or buff >= grid[row][col + 1]:
                low = False
        elif col == len(grid[0]) - 1:
            if buff >= grid[row - 1][col] or buff >= grid[row + 1][col] or buff >= grid[row][col - 1]:
                low = False
        else:
            if buff >= grid[row - 1][col] or buff >= grid[row + 1][col]\
                    or buff >= grid[row][col - 1] or buff >= grid[row][col + 1]:
                low = False

    # if low:
        # return buff + 1
    # else:
        # return -1
    return low

# starts from a low point


def basin(row, col, grid):
    buff = grid[row][col]
    # grid[row][col] = 10

    print("\n(x, y):", row, col)
    print("val:", buff)
    # print(len(grid[0]) - 1)

    if row == 0:
        if grid[row + 1][col] < 9:
            return 1 + basin(row + 1, col, grid)
    elif row == len(grid) - 1:
        if grid[row - 1][col] < 9:
            return 1 + basin(row - 1, col, grid)
    else:
        if grid[row + 1][col] < 9:
            return 1 + basin(row + 1, col, grid)
        elif grid[row + 1][col] == 9:
            return 1

        if grid[row - 1][col] < 9:
            print("hi")
            return 1 + basin(row - 1, col, grid)
        elif grid[row - 1][col] == 9:
            return 1

    # if col == 0:
    #     if grid[row][col + 1] < 9:
    #         return 1 + basin(row, col + 1, grid)
    # elif col == len(grid[0]) - 1:
    #     if grid[row][col - 1] < 9:
    #         return 1 + basin(row, col - 1, grid)
    # else:
    #     if grid[row][col + 1] < 9:
    #         return 1 + basin(row, col + 1, grid)
    #     if grid[row][col - 1] < 9:
    #         return 1 + basin(row, col - 1, grid)


    return 1


# file = open("input-2021-9.txt")
file = open("test.txt")

grid = []

for line in file:
    buff = []
    for l in line.strip():
        buff.append(int(l))
    grid.append(buff)

lows = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if lowPoint(i, j, grid):
            # print(i, j)
            # print(grid[i][j])
            lows.append((i, j))

print(lows)

t = lows[2]
print(basin(t[0], t[1], grid))

# print(len(grid))
# print(len(grid[0]))
