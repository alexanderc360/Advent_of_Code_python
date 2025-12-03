# Part 1
import os
import re
from aocd import _impartial_submit

os.system("aocd 2024 5 > ./2024/day_5/input.txt")
os.system("aocd 2024 5 -e > ./2024/day_5/exampleAnswers.txt")

input = open("./2024/day_5/input.txt")
example = open("./2024/day_5/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example

rules = []
cur = ""
while cur != '\n':
    cur = workingData.pop(0)
    rules.append(cur.strip())
updates = [[int(j) for j in i.strip().split(',')] for i in workingData]

order = {}
nums = set()
for i in rules[:-1]:
    x, y = map(int, re.findall(r"(\d+)\|(\d+)",i)[0])
    if x in order:
        order[x].add(y)
    else:
        order[x] = set([y])

valid = []
for i in updates:
    safe = True
    for n, j in enumerate(i):
        for k in i[n + 1:]:
            if k in order and j in order[k]:
                safe = False
                break
    if safe:
        valid.append(i)

answer = sum(w[len(w) // 2] for w in valid)

# uncomment when ready to submit
_impartial_submit(answer, day=5, year=2024)
