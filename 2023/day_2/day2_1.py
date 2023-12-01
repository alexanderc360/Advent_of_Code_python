import os
import re
os.system("aocd > AOC2023/Day_2/input.txt")
os.system("aocd -e > AOC2023/Day_2/exampleAnswers.txt")
input = open("AOC2023/Day_2/input.txt")
example = open("AOC2023/Day_2/example.txt")

# workingData = input  # change to try example
workingData = example  # change to try example

buff = []
for i in workingData:
    print(i)
