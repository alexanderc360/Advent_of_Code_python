import os

os.system("aocd 2023 15 > ./2023/day_15/input.txt")
os.system("aocd 2023 15 -e > ./2023/day_15/exampleAnswers.txt")
input = open("./2023/day_15/input.txt")
example = open("./2023/day_15/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

strs = [i.strip() for i in workingData.readlines()][0].split(",")
sum = 0
for i in strs:
    hash = 0
    for j in i:
        hash = ((hash + ord(j)) * 17) % 256
    sum += hash
print(sum)
