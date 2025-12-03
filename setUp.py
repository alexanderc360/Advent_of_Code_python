import datetime
import sys
from pathlib import Path

args = sys.argv
year, day = 0, 0

if len(args) == 1:
    day = datetime.datetime.today().day
    year = datetime.datetime.today().year
elif len(args) == 2:
    if 1 <= int(args[1]) <= 25:
        day = int(args[1])
        year = datetime.datetime.today().year
        if datetime.datetime.today().month < 12:
            year -= 1
            print(f"Advent hasn't started yet! Defaulting to {year}")
elif len(args) == 3:
    if 2015 <= int(args[1]) <= datetime.datetime.today().year:
        year = int(args[1])
    if 1 <= int(args[2]) <= 25:
        day = int(args[2])

if year == 0 or day == 0:
    print("Too many or incorect arguments, exiting.")
    exit()
else:
    print(f"Generated template for day {day} of {year}. Good luck!")


part1 = f"""# Part 1
import os
from aocd import _impartial_submit

os.system("aocd {year} {day} > ./{year}/day_{day}/input.txt")
os.system("aocd {year} {day} -e > ./{year}/day_{day}/exampleAnswers.txt")

input = open("./{year}/day_{day}/input.txt")
example = open("./{year}/day_{day}/example.txt")

workingData = input.readlines()  # uncomment to try input
workingData = example.readlines()  # uncomment to try example



# uncomment when ready to submit
# _impartial_submit(answer, day={day}, year={year})
"""

part2 = f"""# Part 2
from aocd import _impartial_submit

input = open("./{year}/day_{day}/input.txt")
example = open("./{year}/day_{day}/example.txt")

workingData = input.readlines()  # uncomment to try input
workingData = example.readlines()  # uncomment to try example



# uncomment when ready to submit
# _impartial_submit(answer, day={day}, year={year})
"""

# Create a dated directory
dir = Path(str(year)) / f"day_{day}"
if not dir.exists():
    dir.mkdir(parents=True, exist_ok=True)

# Generate input and example files
for f in ["input.txt", "example.txt", "exampleAnswers.txt"]:
    if not (dir / f).exists():
        with open(f"{year}/day_{day}/{f}", "w"):
            pass

# Generate solution files using the above templates
if not (dir / f"day{day}_1.py").exists():
    with open(dir / f"day{day}_1.py", "w") as f:
        f.write(part1)
if not (dir / f"day{day}_2.py").exists():
    with open(dir / f"day{day}_2.py", "w") as f:
        f.write(part2)
