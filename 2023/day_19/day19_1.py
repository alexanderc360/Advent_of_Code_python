import re
import os

os.system("aocd 2023 19 > ./2023/day_19/input.txt")
os.system("aocd 2023 19 -e > ./2023/day_19/exampleAnswers.txt")

input = open("./2023/day_19/input.txt")
example = open("./2023/day_19/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

workflows = {}
parts = []
i = 0
for line in workingData:
    name = line[:line.find('{')]
    rules = line[len(name) + 1 :line.find('}')].split(',')
    target = rules.pop()
    workflows[name] = (rules, target)

    i += 1
    if line.isspace():
        partList = workingData[i:]
        break

for i in partList:
    parts.append({key: int(val) for (key, val) in re.findall(r"([a-z])=(\d+)", i)})


def evaluate(part, flows):
    cur = 'in'
    while cur != 'R' and cur != 'A':
        rules, dest = flows[cur][0], flows[cur][1]
        for rule in rules:
            r = rule[:rule.find(':')]
            t = rule[rule.find(':')+1:]
            if eval(f"{part[rule[0]]}{r[1:]}"):
                cur = t
                break
        else:
            cur = dest
    if cur == 'R':
            pass
    elif cur == 'A':
            total = 0
            for n in part:
                 total += int(part[n])
            return total
    return 0
    


total = 0
for p in parts:
    total += evaluate(p, workflows)
print(total)