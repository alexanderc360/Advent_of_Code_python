input = open("./2023/day_15/input.txt")
example = open("./2023/day_15/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example


def hash(str):
    hashVal = 0
    for i in str:
        hashVal = ((hashVal + ord(i)) * 17) % 256
    return hashVal


strs = [i.strip() for i in workingData.readlines()][0].split(",")
boxes = {i: [] for i in range(256)}
for i in strs:
    if i.find('=') > -1:
        label, lens = i[:i.find('=')], int(i[i.find('=') + 1:])
        index = hash(label)
        if label in [j[0] for j in boxes[index]]:
            boxes[index] = [(j, lens) if j == label else (j, k)
                            for j, k in boxes[index]]
        else:
            boxes[index].append((label, lens))
    elif i.find('-') > -1:
        label = i[:i.find('-')]
        index = hash(label)
        boxes[index] = [(j, k) for j, k in boxes[index] if j != label]

sum = 0
for i in boxes:
    buff = 1
    for j, (k, v) in enumerate(boxes[i]):
        sum += (i + 1) * (j + 1) * v
print(sum)
