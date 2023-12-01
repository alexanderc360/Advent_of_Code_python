import re
import time

file = open('inputs/input-2022-21.txt')
# file = open('day 21/test.txt')


def monkeyMath(curMonkey, monks):
    val = monks[curMonkey]
    if re.search("[0-9]+", val):
        return int(val)
    else:
        if '+' in val:
            buff = val.split('+')
            return monkeyMath(buff[0], monks) + monkeyMath(buff[1], monks)
        elif '-' in val:
            buff = val.split('-')
            return monkeyMath(buff[0], monks) - monkeyMath(buff[1], monks)
        elif '*' in val:
            buff = val.split('*')
            return monkeyMath(buff[0], monks) * monkeyMath(buff[1], monks)
        elif '/' in val:
            buff = val.split('/')
            return monkeyMath(buff[0], monks) / monkeyMath(buff[1], monks)


# start = time.time()
trialNum = 0
monkeys = {}
for line in file:
    line = line.strip().replace(' ', '').split(':')

    monkeys[line[0]] = line[1]
start = re.split("[+\-*/]", monkeys["root"])

monkeys["humn"] = str(trialNum)
# while True:
#     if monkeyMath(start[0], monkeys) == monkeyMath(start[1], monkeys):
#         print(trialNum)
#         break
#     trialNum += 1
#     monkeys["humn"] = str(trialNum)
for i in start:
    print(monkeyMath(i, monkeys))
# end = time.time()
# print(end-start)
