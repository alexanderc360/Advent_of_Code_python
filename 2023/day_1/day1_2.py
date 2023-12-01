import re
input = open("AOC2023/Day_1/input.txt")
example = open("AOC2023/Day_1/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example


def nums(n):
    if n == "one":
        return 1
    elif n == "two":
        return 2
    elif n == "three":
        return 3
    elif n == "four":
        return 4
    elif n == "five":
        return 5
    elif n == "six":
        return 6
    elif n == "seven":
        return 7
    elif n == "eight":
        return 8
    elif n == "nine":
        return 9
    else:
        return int(n)


buff = []
sum = 0
for i in workingData:
    d = re.findall(
        r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", i)
    sum += (nums(d[0]) * 10 + nums(d[-1]))

print(sum)
