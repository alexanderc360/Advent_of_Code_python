import os
import re

os.system("aocd 2023 6 > ./2023/day_6/input.txt")
os.system("aocd 2023 6 -e > ./2023/day_6/exampleAnswers.txt")
input = open("./2023/day_6/input.txt")
example = open("./2023/day_6/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

time  = workingData.readline()
dist  = workingData.readline()
time = [int(i) for i in re.findall(r"\d+",time[time.find(":"):])]
dist = [int(i) for i in re.findall(r"\d+",dist[dist.find(":"):])]

count = 1
for i in time:
    win = 0
    for j in range(i):
        if j * (i-j) > dist[time.index(i)]:
            win += 1
    count *= win
print(count)