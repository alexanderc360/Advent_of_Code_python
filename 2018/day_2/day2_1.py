# Part 1
import os

# os.system("aocd 2018 2 > ./2018/day_2/input.txt")
# os.system("aocd 2018 2 -e > ./2018/day_2/exampleAnswers.txt")

input = open("./2018/day_2/input.txt")
example = open("./2018/day_2/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

double, triple = 0, 0
for i in workingData:
    letters = {}
    for j in i:
        if j in letters:
            letters[j] += 1
        else:
            letters[j] = 1
    freqs = set(letters[n] for n in letters)

    if 2 in freqs:
        double += 1
    if 3 in freqs:
        triple += 1

print(double * triple)
    