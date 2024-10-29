from ast import mod
import copy
import re

input = open("./2023/day_20/input.txt")
example = open("./2023/day_20/example.txt")


workingData = input.readlines()  # change to try example
workingData = example.readlines()  # change to try example

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
    done = False
    low, high, = 0, 0
    queue = [("button","broadcaster", 0)]
    while queue:
        sender, cur, power = queue.pop(0)
        # print(sender, power, cur)
        if cur == 'rx' :
            # print('we got it')
            # print(sender, power, cur)

            if power == 0:
                done = True 
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
                        # if m == 'rx' and:
                            # done = True
                        
            elif t == '&':
                if sum([i[k] for k in i]) == len(i):
                    for m in d:
                        queue.append((cur, m, 0))
                        # if m == 'rx':
                            # done = True
                else:
                    for m in d:
                        queue.append((cur, m, 1))
    return mods, done

# tL, tH = 0, 0
count = 0
done = False
cpy = copy.deepcopy(modules) 
print(f"copy: {cpy}")
print()
# while not done:
for i in range(10):
    print(f"iteration {count}")
    modules, done = pulse(modules)
    print(f"copy: {cpy}")
    print(f"modules: {modules}")
    count += 1
    if done or (modules == cpy):
        break
        # print(f"{i} moves needed to turn on rx")
# print(f"{count} moves needed to turn on rx")

#     tL += l
#     tH += h
# print(tL * tH)

# for i in modules:
#     if i == "rx":
#         print(f"{i}: {modules[i]}")
