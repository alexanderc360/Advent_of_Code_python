# Part 2
import re


input = open("./2018/day_3/input.txt")
example = open("./2018/day_3/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example


areas = {}
points = {}
for line in workingData:
    c, x, y, w, h = [int(n) for n in re.findall(
        r'#(\d+)@(\d+),(\d+):(\d+)x(\d+)', line.replace(' ', ''))[0]]
    for i in range(w):
        for j in range(h):
            newX, newY = x + i, y + j
            if c not in areas:
                areas[c] = (x, y, w, h)
            if (newX, newY) in points:
                points[(newX, newY)] += 1
            else:
                points[(newX, newY)] = 1

for c in areas:
    (x, y, w, h), p = areas[c], 0
    for i in range(w):
        for j in range(h):
            newX, newY = x + i, y + j
            p += points[(newX, newY)]
    if p == (w*h):
        print(f'Case: {c}')
        break