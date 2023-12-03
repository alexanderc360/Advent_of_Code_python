import re
input = open("./2023/day_2/input.txt")
example = open("./2023/day_2/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

games = []
for i in workingData:
    games.append(i[i.find(':') + 2:].strip())

sum = 0
for i in games:
    vals = {"red": 0, "green": 0, "blue": 0}
    numbers = [int(i) for i in re.findall(r"\d+", i)]
    colors = re.findall(r"(?=(red|green|blue))", i)
    for j in range(len(colors)):
        if numbers[j] >= vals[colors[j]]:
            vals[colors[j]] = numbers[j]
    sum += (vals["red"] * vals["green"] * vals["blue"] ) 
print(sum)