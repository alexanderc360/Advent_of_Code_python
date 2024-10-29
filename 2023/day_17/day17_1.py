# Part 1
import os
from turtle import left, right

# os.system("aocd 2023 17 > ./2023/day_17/input.txt")
# os.system("aocd 2023 17 -e > ./2023/day_17/exampleAnswers.txt")

input = open("./2023/day_17/input.txt") 
example = open("./2023/day_17/example.txt")


# workingData = input.readlines()  # change to try example
workingData = example.readlines()  # change to try example


grid = {row: col.strip() for row, col in enumerate(workingData)}
queue = [(0, 0, 0, 'right', 0)] # x, y, weight, distance
direction = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
weights = {(0, 0): 0}

numRows, numCols = len(grid[0]) - 1, len(grid) - 1
# print(grid[curX][curY])

while queue:
    check = []
    print(len(weights))
    print(min(queue, key=lambda node: node[2]))
    x, y, w, d, s = min(queue, key=lambda node: node[2])
    queue.remove((x,y,w,d,s))

    if d == 'up' or d == 'down':
        check = ['left', 'right', d]
    elif d == 'left' or d == 'right':
        check = ['up', 'down', d]

        # if dir == d:
            # if s < 3:
                # s += 1
            # else:
                # s = 0
                # break
    for dir in check:

        dx, dy = direction[dir]
        newX, newY = x + dx, y + dy
        if (newX, newY) == (numRows, numCols):
            print(f'weight: {w}')
            queue.clear()
            # break
            
        # print(X,Y)
        if 0 <= newX < numRows and 0 <= newY < numCols:
            wBuff = w + int(grid[newX][newY])
            if (newX, newY) not in weights or weights[(newX, newY)] > wBuff:
                weights[(newX, newY)] = wBuff
                queue.append((newX, newY, wBuff, dir, s))
            # print(f'{dir} -> {wBuff}')
            # print((newX, newY, wBuff, dir))


print(f'Shortest path to exit: {weights[(newX, newY)]}')


# print(grid)
