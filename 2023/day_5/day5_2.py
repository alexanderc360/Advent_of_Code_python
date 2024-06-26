import re

input = open("./2023/day_5/input.txt")
example = open("./2023/day_5/example.txt")

workingData = input  # uncomment to try input
# workingData = example  # uncomment to try example

lines = workingData.readlines()
lines.append('\n')
seedbuff = [int(i) for i in re.findall(r"\d+", lines[0][lines[0].find(":") + 1:])]
seeds = [(int(seedbuff[i]), int(seedbuff[i+1]) + int(seedbuff[i]), int("0")) for i in range(0, len(seedbuff), 2)]
seedSet = set()
maps = []

for i in range(len(lines)):
    if "map" in lines[i]:
        buff = []
        i += 1
        while not lines[i].isspace():
            buff.append([int(n) for n in lines[i].strip().split(" ")])
            i += 1
        maps.append(buff)

locs = []
while seeds:
    start, end, layer = seeds.pop()
    if layer == 7:
        locs.append(start)
        continue   
    for m in maps[layer]:
        s1, s2, = m[1], m[1] + m[2]
        diff = m[0] - m[1]
        if start >= s2 or end <= s1:
            continue
        if start < s1:
            seeds.append((start, s1, layer))
            start = s1
        if end > s2:
            seeds.append((s2, end, layer))
            end = s2
        seeds.append((start + diff, end + diff, layer + 1))
        break
    else:
        seeds.append((start, end, layer + 1))

print(f"Answer: {sorted(locs)[0]}")