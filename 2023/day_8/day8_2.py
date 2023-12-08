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
    elems[i[:i.find('=')-1]] = re.findall(r'[A-Z\d]+',i[i.find('=')+1:])
starts = [i for i in elems if i[-1] == 'A']
count = 0
zSpot = []
while True:
    for i in steps.strip():
        count += 1
        for j in starts:
            if i == 'R':
                starts[starts.index(j)] = elems[j][1]
            elif i == 'L':
                starts[starts.index(j)] = elems[j][0]
        for s in starts:
            if s[-1] == 'Z':
                zSpot.append(count)
                if len(zSpot) == len(starts):
                    break
        else:
            continue
        break
    else:
        continue
    break

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

result = 1
for num in zSpot:
    result = lcm(result, num)
print(result)