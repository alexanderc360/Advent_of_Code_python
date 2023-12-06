import re

input = open("./2023/day_4/input.txt")
example = open("./2023/day_4/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

total = 0
def scratchcard(cards, index):
    global total
    total += 1
    count = 0
    cur = cards[index]
    for i in cur[1]:
        if i in cur[0]:
            count += 1
    for i in range(count):
        scratchcard(cards, index+i+1)


cards = []
for line in workingData:
    c1 = line.find(":")
    c2 = line.find("|")
    win = [int(i) for i in re.findall(r"\d+",line[c1+1:c2])]
    nums = [int(i) for i in re.findall(r"\d+",line[c2:])]
    cards.append((win,nums))

for i in range(len(cards)):
    scratchcard(cards, i) 
print(total)