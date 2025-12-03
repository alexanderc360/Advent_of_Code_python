# Part 1
import os
import re
from aocd import _impartial_submit

# os.system("aocd 2025 2 > ./2025/day_2/input.txt")
# os.system("aocd 2025 2 -e > ./2025/day_2/exampleAnswers.txt")

input = open("./2025/day_2/input.txt")
example = open("./2025/day_2/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example

bounds = []

for i in workingData:
    bounds.extend([(int(b1), int(b2)) for b1, b2 in re.findall(r"(\d+)-(\d+)", i)])

sum = 0

for start, stop in bounds:
    for num in range(start, stop + 1):
        num = str(num)
        length = len(num)
        if length % 2 == 0:
            if num[: length // 2] == num[length // 2 :]:
                sum += int(num)

answer = sum
print(answer)

# uncomment when ready to submit
# _impartial_submit(answer, day=2, year=2025)
