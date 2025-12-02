# Part 2
from aocd import _impartial_submit

input = open("./2025/day_1/input.txt")
example = open("./2025/day_1/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example


dial = 50
zero_occurs = 0
for step in workingData:
    num, add = int(step[1:]), step[0] == "R"
    step = 1 if add else -1

    check = [i % 100 for i in range(dial, dial + (num * step) + step, step)]
    zero_occurs += check[1:].count(0)

    dial = check[-1]

answer = zero_occurs
print("Answer:", answer)


# uncomment when ready to submit
# _impartial_submit(answer, day=1, year=2025)
