# Part 1
import os
from aocd import _impartial_submit

os.system("aocd 2025 3 > ./2025/day_3/input.txt")
os.system("aocd 2025 3 -e > ./2025/day_3/exampleAnswers.txt")

input = open("./2025/day_3/input.txt")
example = open("./2025/day_3/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example

sum = 0
for line in workingData:
    max = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            cur = int(f"{line[i]}{line[j]}")
            if cur > max:
                max = cur
    sum += max

print(sum)
answer = sum
# uncomment when ready to submit
# _impartial_submit(answer, day=3, year=2025)
