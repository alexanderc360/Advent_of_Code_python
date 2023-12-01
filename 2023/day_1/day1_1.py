import os
import re
os.system("aocd > AOC2023/Day_1/input.txt")
os.system("aocd -e > AOC2023/Day_1/exampleAnswers.txt")
input = open("AOC2023/Day_1/input.txt")
example = open("AOC2023/Day_1/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

sum = 0
buff = []
for i in workingData:
    line = [int(i) for i in re.findall(r"\d", i)]
    sum += (line[0]*10 + line[-1])
print(sum)
