# Part 1
import os
from aocd import _impartial_submit

os.system("aocd 2024 1 > ./2024/day_1/input.txt")
os.system("aocd 2024 1 -e > ./2024/day_1/exampleAnswers.txt")

input = open("./2024/day_1/input.txt")
example = open("./2024/day_1/example.txt")

workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

left, right = zip(*(map(int, line.strip().split()) for line in workingData))
answer = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

# uncomment when ready to submit
_impartial_submit(answer, day=1, year=2024)
