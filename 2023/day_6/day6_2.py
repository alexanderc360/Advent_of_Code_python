import dis
import re

input = open("./2023/day_6/input.txt")
example = open("./2023/day_6/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

time  = workingData.readline()
dist  = workingData.readline()
time = int(time[time.find(":")+1:].replace(' ',''))
dist = int(dist[dist.find(":")+1:].replace(' ',''))

win = 0
for j in range(time):
    if j * (time-j) > dist:
        win += 1
print(win)