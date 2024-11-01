# Part 1
import os
import re
import datetime

# os.system("aocd 2018 4 > ./2018/day_4/input.txt")
# os.system("aocd 2018 4 -e > ./2018/day_4/exampleAnswers.txt")

input = open("./2018/day_4/input.txt")
example = open("./2018/day_4/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

events = []
for line in workingData:
    y, m, d, h, mm, e = re.findall(
        r'\[(\d+)-(\d+)-(\d+) (23|00):(\d+)\] ([a-zA-Z\d# ]+)', line)[0]
    y, m, d, h, mm = [int(i) for i in [y, m, d, h, mm]]
    t = datetime.datetime(y, m, d, h, mm)
    events.append({'time': t, 'event': e})


sortedEvents = sorted(events, key=lambda x: x['time'])

gaurds = {}
for i in sortedEvents:
    curTime = i['time']
    event = i['event']
    if event.startswith('Guard'):
        gaurd = event[event.find('#') + 1: event.find('begins') - 1]
        if gaurd not in gaurds:
            gaurds[gaurd] = {j: 0 for j in range(60)}
    elif event.startswith('falls'):
        falls = curTime.minute
    elif event.startswith('wakes'):
        wakes = curTime.minute
        for j in range(falls, wakes, 1):
            gaurds[gaurd][j] += 1


minsMax, g = 0, 0
for i in gaurds:
    totalMins = sum([gaurds[i][j] for j in gaurds[i]])
    if totalMins > minsMax:
        minsMax, g = totalMins, i

maxSleep, minute = 0, 0
for i in gaurds[g]:
    if gaurds[g][i] > maxSleep:
        maxSleep, minute = gaurds[g][i], i

print(int(g) * minute)
