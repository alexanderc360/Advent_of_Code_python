# Part 2
from aocd import _impartial_submit

input = open("./2024/day_2/input.txt")
example = open("./2024/day_2/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example

reports = [[int(j) for j in line.split()] for line in workingData]
answer = 0
for report in reports:
    for i in range(len(report)):
        buff = report[:i] + report[i+1:]
        if (buff == sorted(buff) or buff == sorted(buff, reverse=True)) and \
                all(1 <= abs(buff[j] - buff[j + 1]) <= 3 for j in range(len(buff) - 1)):
            answer += 1
            break

# uncomment when ready to submit
_impartial_submit(answer, day=2, year=2024)
