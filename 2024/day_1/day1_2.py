# Part 2
input = open("./2024/day_1/input.txt")
example = open("./2024/day_1/example.txt")

workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example

left, right = [], []
freq = {}
for line in workingData:
    l, r = [int(i) for i in line.strip().split()]
    left.append(l)
    right.append(r)
    if r in freq:
        freq[r] += 1
    else:
        freq[r] = 1

count = 0
for i in left:
    if i in freq:
        count += i * freq[i]
print(count)
