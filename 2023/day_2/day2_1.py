import os
import re

os.system("aocd 2023 2 > ./2023/day_2/input.txt")
os.system("aocd 2023 2 -e > ./2023/day_2/exampleAnswers.txt")
input = open("./2023/day_2/input.txt")
example = open("./2023/day_2/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

games = []
for i in workingData:
    games.append(i[i.find(":") + 2 :].strip())

sum = 0
for i in games:
    vals = {"red": 0, "green": 0, "blue": 0}
    numbers = [int(i) for i in re.findall(r"\d+", i)]
    colors = re.findall(r"(?=(red|green|blue))", i)
    for j in range(len(colors)):
        if numbers[j] >= vals[colors[j]]:
            vals[colors[j]] = numbers[j]
    if vals["red"] <= 12 and vals["green"] <= 13 and vals["blue"] <= 14:
        sum += games.index(i) + 1
print(sum)
