# Part 2
input = open("./2018/day_1/input.txt")
example = open("./2018/day_1/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

reached = set()
freq = 0
i = 0
while True:
    freq += eval(workingData[i % len(workingData)])
    if freq not in reached:
        reached.add(freq)
    else:
        print(f'Answer: {freq}')
        break
    i += 1