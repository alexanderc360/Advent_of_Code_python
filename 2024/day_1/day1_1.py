# Part 1
import os

os.system("aocd 2024 1 > ./2024/day_1/input.txt")
os.system("aocd 2024 1 -e > ./2024/day_1/exampleAnswers.txt")

input = open("./2024/day_1/input.txt")
example = open("./2024/day_1/example.txt")

workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

left, right = [], []
for line in workingData:
    l, r = [int(i) for i in line.strip().split()]
    left.append(l)
    right.append(r)
left.sort()
right.sort()

count = 0
for i in range(len(left)):
    count += abs(left[i] - right[i])
print(count)