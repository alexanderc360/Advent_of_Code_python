import datetime
import sys
import os

args = sys.argv
dateChecked = False
year, day = 0, 0
if len(args) == 2:
    if 1 <= int(args[1]) <= 25:
        day = int(args[1])
        year = datetime.datetime.today().year

elif len(args) == 3:
    if 2015 <= int(args[1]) <= 2023:
        year = int(args[1])
    if 1 <= int(args[2]) <= 25:
        day = int(args[2])

if year == 0 and day == 0:
    exit()


part1 = f'''# Part 1
import os

os.system("aocd {year} {day} > ./{year}/day_{day}/input.txt")
os.system("aocd {year} {day} -e > ./{year}/day_{day}/exampleAnswers.txt")

input = open("./{year}/day_{day}/input.txt")
example = open("./{year}/day_{day}/example.txt")

# workingData = input.readlines()  # change to try example
workingData = example.readlines()  # change to try example
'''

part2 = f'''# Part 2
input = open("./{year}/day_{day}/input.txt")
example = open("./{year}/day_{day}/example.txt")

workingData = input.readlines()  # change to try example
workingData = example.readlines()  # change to try example
'''

neccesaryFiles = ['input.txt', 'example.txt', 'exampleAnswers.txt']

if not os.path.exists(f'{year}'):
    os.mkdir(f'{year}')

if os.path.exists(f'{year}/day_{day}'):
    pass
else:
    os.mkdir(f'{year}/day_{day}')
for f in neccesaryFiles:
    if not os.path.exists(f'{year}/day_{day}/{f}'):
        with open(f'{year}/day_{day}/{f}', 'w'):
            pass
if not os.path.exists(f'{year}/day_{day}/day{day}_1.py'):
    with open(f'{year}/day_{day}/day{day}_1.py', 'w') as f:
        f.write(part1)
    f.close()
if not os.path.exists(f'{year}/day_{day}/day{day}_2.py'):
    with open(f'{year}/day_{day}/day{day}_2.py', 'w') as f:
        f.write(part2)
    f.close()
