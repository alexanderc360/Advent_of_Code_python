# Part 2
from aocd import _impartial_submit

input = open("./2025/day_3/input.txt")
example = open("./2025/day_3/example.txt")

workingData = input.readlines()  # uncomment to try input
workingData = example.readlines()  # uncomment to try example


num_of_digits = 12
sum = 0
for line in workingData:
    line = list(line.strip())
    largest, start_index = "", 0
    for i in range(num_of_digits):
        max, cur = 0, 0
        for j in range(
            start_index,
            len(line) - (num_of_digits - i) + 1,  # prevents overflow
        ):
            maybe = int(line[j])
            if maybe > max:
                max, cur = maybe, j
        largest += str(max)
        start_index = cur + 1  # offset to prevent repeats
    sum += int(largest)

print(sum)
answer = sum
# uncomment when ready to submit
# _impartial_submit(answer, day=3, year=2025)
