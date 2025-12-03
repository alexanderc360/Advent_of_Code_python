# Part 2
import re
from aocd import _impartial_submit

input = open("./2025/day_2/input.txt")
example = open("./2025/day_2/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example


bounds = []
sum = 0

for i in workingData:
    bounds.extend([(int(b1), int(b2)) for b1, b2 in re.findall(r"(\d+)-(\d+)", i)])

from datetime import datetime

start_time = datetime.now()
for start, stop in bounds:
    for num in range(start, stop + 1):
        num = str(num)
        length = len(num)
        for i in range(1, length):
            if length % i == 0:
                part_count = length // i
                if num.count(num[:i]) == part_count:
                    sum += int(num)
                    break


answer = sum
print(answer)

# uncomment when ready to submit
# _impartial_submit(answer, day=2, year=2025)
