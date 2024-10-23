# Part 1
import os

os.system("aocd 2023 16 > ./2023/day_16/input.txt")
os.system("aocd 2023 16 -e > ./2023/day_16/exampleAnswers.txt")

input = open("./2023/day_16/input.txt")
example = open("./2023/day_16/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

grid = {x: y.strip() for x, y in enumerate(workingData)}

def pulse(grid):
    xLen, yLen = len(grid[0]), len(grid)
    charged = set()
    queue = [(0, 0, 'right')]
    dir = {'up': (0, -1), 'down': (0, 1), 'right': (1, 0), 'left': (-1, 0)}
    mirror = {'up': {'/': 'right', '\\': 'left'}, 'down': {'/': 'left', '\\': 'right'},
              'right': {'/': 'up', '\\': 'down'}, 'left': {'/': 'down', '\\': 'up'}}
    while queue:
        x, y, d = queue.pop(0)
        while 0 <= x < xLen and 0 <= y < yLen and (x, y, d) not in charged:
            charged.add((x,y,d))
            symbol = grid[y][x]
            if symbol == '|' and (d == 'left' or d == 'right'):
                queue.extend([(x, y - 1, 'up'), (x, y + 1, 'down')])
                break
            elif symbol == '-' and (d == 'up' or d == 'down'):
                queue.extend([(x + 1, y, 'right'), (x - 1, y, 'left')])
                break
            elif symbol == '\\' or symbol == '/':
                d = mirror[d][symbol]

            dx, dy = dir[d]
            x += dx
            y += dy
    return charged

print(len(set([(x, y) for x, y, _ in pulse(grid)])))
