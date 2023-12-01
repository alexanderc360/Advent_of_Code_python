file = open("inputs/input-2021-12.txt")

connect = []

for line in file:
    # print(line)
    connect.append(line.strip().split('-'))
    # if "start" in line:

# print(connect[0][len(connect[0])-1])
for c in connect:
    print(c)

def path():
    print()