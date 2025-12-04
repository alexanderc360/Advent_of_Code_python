import datetime
import sys
from pathlib import Path

# Define constants
args = sys.argv
DAY, MONTH, YEAR = (
    datetime.datetime.today().day,
    datetime.datetime.today().month,
    datetime.datetime.today().year,
)


if MONTH != 12 and len(args) < 3:
    print("Advent hasn't started!!!")
    print("Usage: python setUp.py <year> <day>")
    print("\nThe following are available in DECEMBER ONLY:")
    print("\tpython setUp.py")
    print("\tpython setUp.py <day>")
    exit(0)

if len(args) == 1:  # python setUp.py
    _day = DAY
    _year = YEAR
elif len(args) == 2:  # python setUp.py <day>
    _day = int(args[1])
    if not 1 <= _day <= 25:
        _day = 0
    _year = YEAR
elif len(args) == 3:  # python setUp.py <year> <day>
    _year, _day = int(args[1]), int(args[2])
    if not 2015 <= _year <= YEAR:
        _year = 0
    if 1 <= _day <= 25:
        _day = 0


if _year == 0 or _day == 0:
    print("Too many or incorect arguments, exiting.")
    exit()
else:
    print(f"Generated template for day {_day} of {_year}. Good luck!")


part1 = f"""# Part 1
import os
from aocd import _impartial_submit

os.system("aocd {_year} {_day} > ./{_year}/day_{_day}/input.txt")
os.system("aocd {_year} {_day} -e > ./{_year}/day_{_day}/exampleAnswers.txt")

input = open("./{_year}/day_{_day}/input.txt")
example = open("./{_year}/day_{_day}/example.txt")

workingData = input.readlines()  # uncomment to try input
workingData = example.readlines()  # uncomment to try example



# uncomment when ready to submit
# _impartial_submit(answer, day={_day}, _year={_year})
"""

part2 = f"""# Part 2
from aocd import _impartial_submit

input = open("./{_year}/day_{_day}/input.txt")
example = open("./{_year}/day_{_day}/example.txt")

workingData = input.readlines()  # uncomment to try input
workingData = example.readlines()  # uncomment to try example



# uncomment when ready to submit
# _impartial_submit(answer, day={_day}, _year={_year})
"""

# Create a dated directory
dir = Path(str(_year)) / f"day_{_day}"
if not dir.exists():
    dir.mkdir(parents=True, exist_ok=True)

# Generate input and example files
for f in ["input.txt", "example.txt", "exampleAnswers.txt"]:
    if not (dir / f).exists():
        (dir / f).touch()

# Generate solution files using the above templates
for d, t in [(dir / f"day{_day}_1.py", part1), (dir / f"day{_day}_2.py", part2)]:
    if not d.exists():
        d.write_text(t)
