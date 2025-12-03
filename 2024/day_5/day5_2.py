# Part 2
import re
from aocd import _impartial_submit

input = open("./2024/day_5/input.txt")
example = open("./2024/day_5/example.txt")

workingData = input.readlines()  # uncomment to try input
workingData = example.readlines()  # uncomment to try example


rules = []
cur = ""
while cur != '\n':
    cur = workingData.pop(0)
    rules.append(cur.strip())
updates = [[int(j) for j in i.strip().split(',')] for i in workingData]

order = {}
nums = set()
for i in rules[:-1]:
    x, y = map(int, re.findall(r"(\d+)\|(\d+)", i)[0])
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
    if not safe:
        valid.append(i)


def topo(cur, visited, stack, order):
    if cur not in visited:
        visited.add(cur)
        for i in order[cur]:
            topo(i, visited, stack, order)
        stack.append(cur)


updates = []
for w in valid:
    stack = []
    visited = set()
    orderBuff = {i: set() for i in w}
    for i in w:
        for j in w:
            if i in order and j in order[i]:
                orderBuff[i].add(j)
    for i in orderBuff:
        topo(i, visited, stack, orderBuff)
    updates.append(stack[::-1])

answer = sum(w[len(w) // 2] for w in updates)

# uncomment when ready to submit
_impartial_submit(answer, day=5, year=2024)
