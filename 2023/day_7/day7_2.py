import os
import re

input = open("./2023/day_7/input.txt")
example = open("./2023/day_7/example.txt")

workingData = input  # change to try example
# workingData = example  # change to try example

# 0: five of a kind 
# 1: four of a kind 
# 2: full house 
# 3: three of a kind
# 4: two pair 
# 5: one pair
# 6: high card
hands = [{} for i in range(7)]
cardValues = [i for i in "AKQT98765432J"]
for line in workingData:
    res = re.findall(r'([A-Z\d]+) (\d+)', line)
    cards = {}
    joker = 0
    for hand, bet in res:
        for c in hand:
            if c == 'J':
                joker += 1
            else:
                if c not in cards:
                    cards[c] = 1
                else:
                    cards[c] += 1
        ocur = sorted(cards.values(), reverse=True)
        if len(ocur) == 0:
            ocur.append(joker)
        else:
            ocur[0] += joker

        if ocur[0] == 5 or len(ocur) < 2:
            hands[0][hand] = bet
        elif ocur[0] == 4:
            hands[1][hand] = bet
        elif ocur[0] == 3 and ocur[1] == 2:
            hands[2][hand] = bet
        elif ocur[0] == 3:
            hands[3][hand] = bet
        elif ocur[0] == 2 and ocur[1] == 2:
            hands[4][hand] = bet
        elif ocur[0] == 2:
            hands[5][hand] = bet
        else:
            hands[6][hand] = bet

rank = []
winnings = 0
for type in hands:
    for i in sorted(type, key=lambda x: [cardValues.index(c) for c in x]):
        rank.append((i,type[i]))
for i, h in enumerate(reversed(rank)):
    winnings += (i + 1) * int(h[1])
print(winnings)