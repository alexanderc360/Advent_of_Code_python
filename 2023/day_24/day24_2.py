# Part 2
import re 

input = open("./2023/day_24/input.txt")
example = open("./2023/day_24/example.txt")


workingData = input.readlines()  # change to try example
workingData = example.readlines()  # change to try example


points = []

for i in workingData:
    # print(i)
    data = re.findall(
        r"(\d+),(\d+),(\d+)@(-?\d+),(-?\d+),(-?\d+)", i.replace(' ', ''))[0]

    # First three values (coordinates)
    coords = tuple(map(int, data[:3]))

    # Last three values (velocities)
    vel = tuple(map(int, data[3:]))
    slope = vel[1]/vel[0]

    print("Coordinates:", coords)
    print("Velocity:", vel)

    print(f'x = {coords[0]} + t * {vel[0]}')
    print(f'y = {coords[1]} + t * {vel[1]}')
    print(f'z = {coords[2]} + t * {vel[2]}')

    points.append((coords, vel))
    print()

# # print(points)
# count = 0
# loop = 0
# intersect = (7, 27)
# intersect = (200000000000000, 400000000000000)
# for i in range(len(points)):
#     x, y, z = points[i][0]
#     vx, vy, vz = points[i][1]
#     slope = vy/vx
#     b = -slope*x + y
#     # print(f'y = {slope}x + {-slope*x + y}')
#     for j in range(i, len(points)):
#         # print(f'check {loop}')
#         loop += 1
#         # print(f'{points[i][0]} @ {points[i][1]}')
#         # print(f'{points[j][0]} @ {points[j][1]}')
#         x2, y2, z2 = points[j][0]
#         vx2, vy2, vz2 = points[j][1]
#         slope2 = vy2/vx2
#         b2 = -slope2*x2 + y2
#         # print(f'y = {slope}x + {b}')
#         # print(f'y = {slope2}x + {b2}')
#         if slope != slope2:
#             # print(f'{slope}x + {b} = {slope2}x + {b2}')
#             # print(f'{slope}x + {-slope2}x = {b2} - {b}')
#             s = slope + -slope2
#             b3 = b2 - b
#             # print(f'{s}x = {b3}')
#             # print(f'x = {b3}/{s}')
#             # print(f'x = {b3 / s}')
#             ix = b3 / s
#             iy = slope*ix + b

#             # print(f'({ix}, {iy})')

#             fut = False
#             for k in ((x, vx), (x2, vx2)):
#                 # print(k)
#                 (tempX, tempV) = k
#                 if tempV < 0 and tempX > ix:
#                     fut = True
#                 elif tempV > 0 and tempX < ix:
#                     fut = True
#                 else:
#                     fut = False
#                     # print(f'past for {"A" if tempX == x else "B"}')
#                     break
#             if fut:
#                 # print('future for both')
#                 if intersect[0] <= ix <= intersect[1] and intersect[0] <= iy <= intersect[1]:
#                     # print('in zone')
#                     count += 1

#         # print()
#         # break
#         # else
#     # break
#     # print()

# print(count)
