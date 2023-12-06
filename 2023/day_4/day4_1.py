import os
import re

os.system("aocd 2023 4 > ./2023/day_4/input.txt")
os.system("aocd 2023 4 -e > ./2023/day_4/exampleAnswers.txt")
input = open("./2023/day_4/input.txt")
example = open("./2023/day_4/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

sum = 0
for line in workingData:
    c1 = line.find(":")
    c2 = line.find("|")
    win = [int(i) for i in re.findall(r"\d+",line[c1+1:c2])]
    nums = [int(i) for i in re.findall(r"\d+",line[c2:])]

    points = 0
    for i in nums:
        if i in win:
            points = 1 if points == 0 else points * 2
    sum += points

print(sum)