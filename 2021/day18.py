import copy
from os import linesep
from re import L


def fixDoubleDigit(num):
    fixed = []
    i = 0
    while i < len(num):
        buff = num[i]
        if buff.isnumeric():
            while num[i + 1].isnumeric():
                buff += num[i + 1]
                i += 1
        fixed.append(buff)
        i += 1
    return fixed


def explode(num):
    nest = 0
    for i in range(len(num)):
        buff = num[i]
        if buff == '[':
            nest += 1
            if nest >= 5:
                buffStr = num[i:]
                pair = buffStr[1:buffStr.index(']')]

                for j in reversed(range(i)):  # looking for number to the left
                    j += 1
                    if num[j].isnumeric():
                        if num[j - 1] == ',' or num[j + 1] == ',':
                            num[j] = str(int(num[j]) + int(pair[0]))
                            break

                for j in range(i + 4, len(num), 1):  # looking for number to the right
                    if num[j].isnumeric():
                        if num[j - 1] == ',' or num[j + 1] == ',':
                            num[j] = str(int(num[j]) + int(pair[2]))
                            break

                del num[i:i+5]
                num.insert(i, '0')
                break

        elif buff == ']':
            nest -= 1


def split(num):
    for i in range(len(num)):
        s = num[i]
        if s.isnumeric() and int(s) >= 10:
            half = int(int(s)/2)
            round = 0 if int(s) % 2 == 0 else 1
            del num[i]
            newPair = '[' + str(half) + ',' + str(half + round) + ']'
            for k in range(len(newPair)):
                num.insert(i+k, newPair[k])
            break

    return num


def reduce(num):
    count = 0
    while True:
        num = fixDoubleDigit(num)
        count += 1
        buff = copy.deepcopy(num)
        explode(buff)
        if buff == num:
            split(buff)
            if buff == num:
                return buff
        num = buff


def add(num1, num2):
    sum = ['[']
    for i in num1:
        sum.append(i)
    sum.append(',')
    for i in num2:
        sum.append(i)
    sum.append(']')

    return reduce(sum)


def magnitude(num):
    for i in range(len(num)):
        buff = num[i]
        if buff == ']':
            mag = (3 * int(num[i - 3])) + (2 * int(num[i - 1]))
            del num[i-4:i+1]
            num.insert(i-4, str(mag))
            break

    if num[0] == '[':
        magnitude(num)

    return num


file = open('inputs/input-2021-18.txt')

# part 1
# count = 0
# for line in file:
#     line = line.strip()
#     list = []

#     for i in line:
#         list.append(i)

#     list = fixDoubleDigit(list)

#     if count == 0:
#         sum = list
#     else:
#         sum = add(sum, list)
#     count += 1
# print(magnitude(sum))


# part 2
nums = []
for line in file:
    nums.append(line.strip())

max = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            a = add(nums[i], nums[j])
            m = magnitude(a)[0]
            if max < int(m):
                max = int(m)


print(max)
