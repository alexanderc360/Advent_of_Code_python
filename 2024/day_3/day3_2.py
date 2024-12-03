# Part 2
import re
from aocd import _impartial_submit

input = open("./2024/day_3/input.txt")
example = open("./2024/day_3/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example

multi = [match for line in workingData for match in re.findall(
    r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", line)]

answer = 0
ignore = False
for m in multi:
    if m == "don't()":
        ignore = True
    elif m == "do()":
        ignore = False
    else:
        if not ignore:
            answer += (int(m[4:m.find(',')]) * int(m[m.find(',')+1:-1]))

# uncomment when ready to submit
_impartial_submit(answer, day=3, year=2024)