import os
import re

os.system("aocd 2023 9 > ./2023/day_9/input.txt")
os.system("aocd 2023 9 -e > ./2023/day_9/exampleAnswers.txt")
input = open("./2023/day_9/input.txt")
example = open("./2023/day_9/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example


def deltaList(line, delta):
    if len(delta) > 0:
        if delta[0] == [0 for i in range(len(delta[0]))]:
            return delta
    if len(line) == 1:
        return delta
    
    delta.insert(0,[])
    for i in range(len(line) - 1):
        delta[0].append(line[i + 1] - line[i])
    return deltaList(delta[0], delta)

sum = 0
for line in workingData:
    line = [int(x) for x in re.findall(r"[-\d]+", line)]
    buff = deltaList(line, [])
    answer = 0
    for i in buff:
        answer += i[-1]
    answer += line[-1]
    sum += answer

print(sum)