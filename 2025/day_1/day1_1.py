# Part 1
import os
from aocd import _impartial_submit

os.system("aocd 2025 1 > ./2025/day_1/input.txt")
os.system("aocd 2025 1 -e > ./2025/day_1/exampleAnswers.txt")

input = open("./2025/day_1/input.txt")
example = open("./2025/day_1/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example

dial = 50
zero_occurs = 0
for step in workingData:
    num = int(step[1:])
    add = step[0] == "R"

    if add:
        dial += num
    else:
        dial -= num
        
    dial = dial % 100
    if dial == 0:
        zero_occurs += 1

answer = zero_occurs
print("Answer:", answer)


# uncomment when ready to submit
_impartial_submit(answer, day=1, year=2025)
