import os
import re

# os.system("aocd > inputs/input-2022-15.txt")

# file = open("inputs/input-2022-15.txt")
file = open("day 15/test.txt")


def manhattan(bec, sen):
    return abs(bec[0] - sen[0]) + abs(bec[1] - sen[1])


minX = 0
maxX = 0

dists = {}
sensors = set()
beacons = set()
for line in file:
    nums = re.findall("\-?\d+", line)
    sen = (int(nums[0]), int(nums[1]))
    bec = (int(nums[2]), int(nums[3]))
    sensors.add(sen)
    beacons.add(bec)
    if sen not in dists:
        dists[sen] = manhattan(sen, bec)


row = 10  # largest collumn = 24
# row = 2000000
count = 0
max = 0
clear = set()

step = 0
bound = 20

while step < bound + 1:
    print(row, step)
    for s in sensors:  # TODO: need to calculate the x value based on y so i can skip iterations
        yDiff = abs(row - s[1])
        if yDiff <= dists[s]:
            spots = abs(dists[s] - yDiff)
            print(spots)
    step += 1

# print(len(clear), max)
