import os
import re
print(os.getcwd())
os.system("aocd 2023 5 > ./2023/day_5/input.txt")
os.system("aocd 2023 5 -e > ./2023/day_5/exampleAnswers.txt")
input = open("./2023/day_5/input.txt")
example = open("./2023/day_5/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

lines = workingData.readlines()
lines.append('\n')
seeds = [int(i) for i in re.findall(r"\d+", lines[0][lines[0].find(":") + 1:])]
maps = []

for i in range(len(lines)):
    if "map" in lines[i]:
        buff = []
        while lines[i+1] != "\n":
            i += 1
            buff.append([int(n) for n in lines[i].strip().split(" ")])
        maps.append(buff)

min = seeds[0]
for s in seeds:
    cur = s
    for i in maps:
        for j in i:
            if cur in range(j[1], j[1]+j[2]):
                cur = j[0] + (cur-j[1])
                break
    if cur < min:
        min = cur
print(min)
