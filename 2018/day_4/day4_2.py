# Part 2
import re
import datetime

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
    curTime, event = i['time'],  i['event']
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


maxFreq, g, minute = 0, 0, 0
for i in gaurds:
    for j in gaurds[i]:
        if gaurds[i][j] > maxFreq:
            maxFreq, g, minute = gaurds[i][j], int(i), j

print(g * minute)
