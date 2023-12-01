# file = open("inputs/input-2022-17.txt")
file = open("day 17/test.txt")


def view(height, bricks, fallingBricks):
    for i in range(height, -1, -1):
        for j in range(7):
            if [j, i] in bricks:
                print("@", end="")
            elif [j, i] in fallingBricks:
                print("@", end="")

            else:
                print(".", end="")
        print()


def shapes(i, height):
    fallingBricks = []
    diff = 0
    if i % 5 == 0:
        fallingBricks, diff = [[2, height], [3, height],
                               [4, height], [5, height]], 1
    elif i % 5 == 1:
        fallingBricks, diff = [
            [3, height+2], [2, height+1], [3, height+1], [4, height+1], [3, height]], 3
    elif i % 5 == 2:
        fallingBricks, diff = [
            [4, height+2], [4, height+1], [2, height], [3, height], [4, height]], 3
    elif i % 5 == 3:
        fallingBricks, diff = [
            [2, height+3], [2, height+2], [2, height+1], [2, height]], 4
    elif i % 5 == 4:
        fallingBricks, diff = [
            [2, height + 1], [3, height + 1], [2, height], [3, height]], 2
    return fallingBricks, diff


bricks = []
height = 0
landing = 3
width = 7

fallingBricks = []
diff = 0
direction = file.readline()
shapeCounter = 0
fallingBricks, diff = shapes(shapeCounter, landing)
shapeCounter += 1
atRest = False
# for i in range(len(direction)):
for i in range(12):
    print(height)
    print("orig 1", fallingBricks)
    view(landing, bricks, fallingBricks)
    height = landing + 3

    bound = 1
    if direction[i] == ">":
        for j in fallingBricks:
            if j[0] + 1 == 7 or [j[0], j[1] + 1] in bricks:
                bound = 0
        for j in fallingBricks:
            j[0] += 1 * bound
    else:
        for j in fallingBricks:
            if j[0] == 0 or [j[0], j[1] - 1] in bricks:
                bound = 0
        for j in fallingBricks:
            j[0] -= 1 * bound
    print(direction[i])
    print("shift 2", fallingBricks)
    view(landing+4, bricks, fallingBricks)

    for j in fallingBricks:
        for b in bricks:
            if [j[0], j[1]-1] == b:
                atRest = True
                # break
        if j[1] == 0:
            atRest = True
            # break
    if not atRest:
        for j in fallingBricks:
            j[1] -= 1
    else:
        for i in fallingBricks:
            bricks.append(i)
        landing += diff
        fallingBricks, diff = shapes(shapeCounter, landing)
        atRest = False
        shapeCounter += 1

    print("fall 3", fallingBricks)
    view(landing, bricks, fallingBricks)
