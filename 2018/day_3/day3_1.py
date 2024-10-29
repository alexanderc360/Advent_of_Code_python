# Part 1
import os
import re

# os.system("aocd 2018 3 > ./2018/day_3/input.txt")
# os.system("aocd 2018 3 -e > ./2018/day_3/exampleAnswers.txt")

input = open("./2018/day_3/input.txt")
example = open("./2018/day_3/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

areas = {}
for line in workingData:
    _, x, y, w, h = [int(n) for n in re.findall(
        r'#(\d+)@(\d+),(\d+):(\d+)x(\d+)', line.replace(' ', ''))[0]]
    
    for i in range(w):
        for j in range(h):
            newX, newY = x + i, y + j
            if (newX, newY) in areas:
                areas[(newX, newY)] += 1
            else:
                areas[(newX, newY)] = 1

overlap = sum([1 if areas[i] > 1 else 0 for i in areas])
print(f"Answer: {overlap}")
