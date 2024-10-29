import re
import os

os.system("aocd 2023 19 > ./2023/day_19/input.txt")
os.system("aocd 2023 19 -e > ./2023/day_19/exampleAnswers.txt")

input = open("./2023/day_19/input.txt")
example = open("./2023/day_19/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example
