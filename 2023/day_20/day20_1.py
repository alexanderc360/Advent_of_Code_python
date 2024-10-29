import re
import os

os.system("aocd 2023 20 > ./2023/day_20/input.txt")
os.system("aocd 2023 20 -e > ./2023/day_20/exampleAnswers.txt")

input = open("./2023/day_20/input.txt")
example = open("./2023/day_20/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

modules = {}
for line in workingData:
    line = line.replace(" ", '')
    data = re.findall(
        r"broadcaster->([a-zA-Z]+(?:,[a-zA-Z]+)*)|([%&])([a-zA-z]+)->([a-zA-Z]+(?:,[a-zA-Z]+)*)", line)[0]
    if data[0] != '':
        modules['broadcaster'] = data[0].split(',')
    else:
        t, d = data[1], data[3].split(',')
        modules[data[2]] = (t, d, False, {})

        for i in data[3].split(','):  
            if i not in modules:
                modules[i] = ('',  [], False, {})

for m in modules:
    if m == "broadcaster":
        for t in modules[m]:
            modules[t][3][m] = 0
    else:
        for t in modules[m][1]:
            modules[t][3][m] = 0
    

def pulse(mods):
    low, high, = 0, 0
    queue = [("button","broadcaster", 0)]
    while queue:
        sender, cur, power = queue.pop(0)
        if power == 0:
            low += 1
        else:
            high += 1
            
        if cur == 'broadcaster':
            for m in mods[cur]:
                queue.append((cur, m, 0))
        else:
            (t, d, p, i) = mods[cur]
            i[sender] = power
            if t == '%':
                if power == 0:
                    mods[cur] = (t, d, not p, i)
                    for m in d:
                        queue.append((cur, m, 0 if p else 1))
            elif t == '&':
                if sum([i[k] for k in i]) == len(i):
                    for m in d:
                        queue.append((cur, m, 0))
                else:
                    for m in d:
                        queue.append((cur, m, 1))
    return mods, low, high

tL, tH = 0, 0
for i in range(1000):
    modules, l, h = pulse(modules)
    tL += l
    tH += h
print(tL * tH)
