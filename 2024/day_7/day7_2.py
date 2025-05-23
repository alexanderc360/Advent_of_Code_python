# Part 2
import re
from aocd import _impartial_submit

input = open("./2024/day_7/input.txt")
example = open("./2024/day_7/example.txt")

workingData = input.readlines()  # uncomment to try input
# workingData = example.readlines()  # uncomment to try example


def char_combos(chars: str, len: int):
    """
    Generate all combinations of a given length from a set of characters.

    Args:
        chars (str): The set of characters to use for combinations.
        len (int): The length of the combinations to generate.
    """
    if len == 0:
        return [""]
    else:
        prev_combos = char_combos(chars, len - 1,)
        return [c + x for c in chars for x in prev_combos]


def calculate(numbers: list[int], operations: str):
    """
    Calculate the result of a list of numbers and operations.
    Args:
        numbers (list[int]): The list of numbers to calculate.
        operations (str): The string of operations to perform.
    """
    result = 0
    for n, i in enumerate(numbers):
        if n == 0:
            result = i
        else:
            if operations[n - 1] == "+":
                result += i
            elif operations[n - 1] == "*":
                result *= i
            elif operations[n - 1] == "|":
                result = int(f"{result}{i}")
    return result


answer = 0
equations = {}
for i in workingData:
    i = i.strip()
    a, nums = re.findall(r"(\d+):((?: \d+)+)", i)[0]
    equations[int(a)] = [int(x) for x in nums.split()]

for i in equations:
    ops = char_combos("+*|", len(equations[i]) - 1)
    for op in ops:
        result = calculate(equations[i], op)
        if result == i:
            answer += result
            break

print(f"Final Answer: {answer}")

# uncomment when ready to submit
_impartial_submit(answer, day=7, year=2024)
