import datetime

input = open("./2023/day_14/input.txt")
example = open("./2023/day_14/example.txt")

workingData = input  # uncomment to try input
# workingData = example  # uncomment to try example

def tilt(bd, cb, cir):
    # north
    for i in range(len(bd[0])):
        stop = 0
        for j in range(len(bd)):
            if i in cb[j]:
                stop = j + 1
            elif i in cir[j]:
                if j > stop:
                    cir[stop].add(i)
                    cir[j].remove(i)
                stop += 1
    # west
    for i in range(len(bd)):
        stop = 0
        for j in range(len(bd[0])):
            if j in cb[i]:
                stop = j + 1
            elif j in cir[i]:
                if j > stop:
                    cir[i].add(stop)
                    cir[i].remove(j)
                stop += 1
    # south
    for i in range(len(bd[0])):
        stop = len(bd) - 1
        for j in reversed(range(len(bd))):
            if i in cb[j]:
                stop = j - 1
            elif i in cir[j]:
                if j < stop:
                    cir[stop].add(i)
                    cir[j].remove(i)
                stop -= 1
    # east
    for i in range(len(bd)):
        stop = len(bd[0]) - 1
        for j in reversed(range(len(bd[0]))):
            if j in cb[i]:
                stop = j - 1
            elif j in cir[i]:
                if j < stop:
                    cir[i].add(stop)
                    cir[i].remove(j)
                stop -= 1
    return cir

def findLoop(sequence):
    l = len(sequence)
    for i in range(l):
        for size in range(1, l//2 + 1):
            if sequence[i:i+size] == sequence[i+size:i+(2*size)]:
                pattern = sequence[i:i+size]
                repeated = True
                for j in range(i, l - l%size, size):
                    if sequence[j:j+size] != pattern:
                        repeated = False
                        break
                if repeated:
                    return i, pattern
    return -1, []

startTime = datetime.datetime.now()
board = {num: line.strip() for num, line in enumerate(workingData)}

cube = {int(i): set() for i in board}
circ = {int(i): set() for i in board}
for row in board:
    cube[row].update([i for i in range(len(board[row])) if board[row][i] == "#"])
    circ[row].update([i for i in range(len(board[row])) if board[row][i] == "O"])

loads = []
for i in range(500):
    circ = tilt(board, cube, circ)
    loads.append(sum((len(circ) - j) * len(circ[j]) for j in circ))

start, pattern = findLoop(loads)
cycleCount = 1000000000
answer = pattern[((cycleCount - start)%len(pattern))-1]

finishTime = datetime.datetime.now()
print(f"Answer: {answer}  Time: {finishTime - startTime}")