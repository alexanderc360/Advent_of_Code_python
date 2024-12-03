# Part 1
import os
import re
from aocd import _impartial_submit

os.system("aocd 2024 3 > ./2024/day_3/input.txt")
os.system("aocd 2024 3 -e > ./2024/day_3/exampleAnswers.txt")

input = open("./2024/day_3/input.txt")
example = open("./2024/day_3/example.txt")

workingData = input.readlines()  # uncomment to try input
workingData = example.readlines()  # uncomment to try example

multi = [match for line in workingData for match in re.findall(
    r'(mul\([0-9]+,[0-9]+\))', line)]
answer = sum((int(m[4:m.find(',')]) * int(m[m.find(',')+1:-1])) for m in multi)

# uncomment when ready to submit
_impartial_submit(answer, day=3, year=2024)
