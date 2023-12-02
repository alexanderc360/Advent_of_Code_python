import os
import re
os.system("aocd 2023 1 > ./2023/day_1/input.txt")
os.system("aocd 2023 1 -e > ./2023/day_1/exampleAnswers.txt")
input = open("./2023/day_1/input.txt")
example = open("./2023/day_1/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

sum = 0
buff = []
for i in workingData:
    line = [int(i) for i in re.findall(r"\d", i)]
    sum += (line[0]*10 + line[-1])
print(sum)
