# Part 2
from aocd import _impartial_submit

input = open("./2024/day_1/input.txt")
example = open("./2024/day_1/example.txt")

workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

left, right = zip(*(map(int, line.strip().split()) for line in workingData))
answer = sum(i * right.count(i) for i in left)

# uncomment when ready to submit
_impartial_submit(answer, day=1, year=2024)
