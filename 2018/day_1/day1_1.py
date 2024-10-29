# Part 1
import os

# os.system("aocd 2018 1 > ./2018/day_1/input.txt")
# os.system("aocd 2018 1 -e > ./2018/day_1/exampleAnswers.txt")

input = open("./2018/day_1/input.txt")
example = open("./2018/day_1/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

print(sum([int(i) for i in workingData]))