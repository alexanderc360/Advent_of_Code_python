# Part 1
import os
from aocd import _impartial_submit

# os.system("aocd 2024 2 > ./2024/day_2/input.txt")
# os.system("aocd 2024 2 -e > ./2024/day_2/exampleAnswers.txt")

input = open("./2024/day_2/input.txt")
example = open("./2024/day_2/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example

reports = [[int(j) for j in line.split()] for line in workingData]
answer = 0
for report in reports:
    if (report == sorted(report) or report == sorted(report, reverse=True)) and \
            all(1 <= abs(report[j] - report[j + 1]) <= 3 for j in range(len(report) - 1)):
        answer += 1

# uncomment when ready to submit
_impartial_submit(answer, day=2, year=2024)
