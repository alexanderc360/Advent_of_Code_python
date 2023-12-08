import os
import re

os.system("aocd 2023 8 > ./2023/day_8/input.txt")
os.system("aocd 2023 8 -e > ./2023/day_8/exampleAnswers.txt")
input = open("./2023/day_8/input.txt")
example = open("./2023/day_8/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

steps = workingData.readline()
workingData.readline()
elems = {}
for i in workingData:
    elems[i[:i.find('=')-1]] = re.findall(r'[A-Z]+',i[i.find('=')+1:])

cur = 'AAA'
count = 0
print(cur)
while cur != 'ZZZ':
    for i in steps:
        print(cur)
        if cur == 'ZZZ':
            break
        if i == 'R':
            cur = elems[cur][1]
            count += 1
        elif i == 'L':
            cur = elems[cur][0]
            count += 1  
print(count)