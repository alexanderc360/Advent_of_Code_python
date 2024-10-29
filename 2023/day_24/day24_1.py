# Part 1
import os
import re

# os.system("aocd 2023 24 > ./2023/day_24/input.txt")
# os.system("aocd 2023 24 -e > ./2023/day_24/exampleAnswers.txt")

input = open("./2023/day_24/input.txt")
example = open("./2023/day_24/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

points = []

for i in workingData:
    data = re.findall(r"(\d+),(\d+),(\d+)@(-?\d+),(-?\d+),(-?\d+)", i.replace(' ', ''))[0]
    coords,vel = tuple(map(int, data[:3])), tuple(map(int, data[3:]))
    slope = vel[1]/vel[0]
    points.append((coords,vel))

count = 0
min, max = 200000000000000, 400000000000000
for i in range(len(points)):
    (x, y, z,), (vx, vy, vz) = points[i][0], points[i][1]
    slope = vy/vx
    b = -slope*x + y
    for j in range(i, len(points)):
        (x2, y2, z2), (vx2, vy2, vz2) = points[j][0], points[j][1]
        slope2 = vy2/vx2
        b2 = -slope2*x2 + y2
        if slope != slope2: # no need to check if parallel 
            s = slope + -slope2
            b3 = b2 - b

            ix = b3 / s # solve for x
            iy = slope*ix + b # solve for y

            fut = False
            for k in ((x,vx), (x2, vx2)): # checks if the intersection is in the future for each point
                (tempX, tempV) = k
                if (tempV < 0 and tempX > ix) or (tempV > 0 and tempX < ix):
                    fut = True
                else:
                    fut = False
                    break
            if fut:
                if min <= ix <= max and min <= iy <= max: # checks if a future intersection is in the target zone
                    count += 1

print(count)

