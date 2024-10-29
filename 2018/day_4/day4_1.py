# Part 1
import os

# os.system("aocd 2018 4 > ./2018/day_4/input.txt")
# os.system("aocd 2018 4 -e > ./2018/day_4/exampleAnswers.txt")

input = open("./2018/day_4/input.txt")
example = open("./2018/day_4/example.txt")


workingData = input.readlines()  # change to try example
workingData = example.readlines()  # change to try example

for line in workingData:
    print(line)