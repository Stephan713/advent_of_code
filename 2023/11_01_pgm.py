import re

input_file = open("inputs/11_01_input.txt", 'r')

galaxy_map = input_file.readlines()

galaxy_map = [ x.strip() for x in galaxy_map]
# print(galaxy_map[46])

# galaxy_map=['...#......',
#             '.......#..',
#             '#.........',
#             '..........',
#             '......#...',
#             '.#........',
#             '.........#',
#             '..........',
#             '.......#..',
#             '#...#.....']

absent_lines = []
for i, line in enumerate(galaxy_map):
    if line.find('#') == -1:
        absent_lines.append(i)
print(absent_lines)

transpose_map = []
for i, line in enumerate(galaxy_map):
    for j, letter in enumerate(line):
        if i == 0:
            transpose_map.append(letter)
        else:
            transpose_map[j] = transpose_map[j]+letter

absent_columns = []
for i, line in enumerate(transpose_map):
    if line.find('#') == -1:
        absent_columns.append(i)
print(absent_columns)
#
#
# str_test = '.........................#...........................#......#.............#............#......#.........#.............................................'
#
# # print([m.start() for m in re.finditer('#',str_test)])

# print(galaxy_map[46])

locations = []
for i, line in enumerate(galaxy_map):
    locations.extend([(m.start(),i) for m in re.finditer('#',line)])

# print(locations)
# x,y - position,line
#
def man_distance(p1, p2):
    distance = 0
    for k, values in enumerate(zip(p1, p2)):
        if k == 0:
            mul_factor = 0
            for column in absent_columns:
                # (yp < y1) != (yp < y2)
                # print(values[0], values[1], column)
                # print(column < values[0])
                # print(column < values[1])
                if (values[0] < column < values[1]) or (values[1] < column < values[0]):
                    mul_factor = mul_factor + 1
                    # print('here')

            distance = distance + abs(values[0] - values[1]) + mul_factor * 1000000 - mul_factor
            # print(distance, mul_factor)
        else:
            mul_factor = 0
            for line in absent_lines:
                if (values[0] < line < values[1]) or (values[1] < line < values[0]):
                    mul_factor = mul_factor + 1

            distance = distance + abs(values[0] - values[1]) + mul_factor * 1000000 - mul_factor
            # print(distance, mul_factor)
    # print(distance)
    return distance
    # return sum([abs(value1 - value2) for value1, value2 in zip(p1, p2)])


# man_distance((3, 0),(0, 2))


#
tot_distance = 0
for i,location in enumerate(locations):
    for j, l2 in enumerate(locations[i+1:]):
        # print(location, l2, man_distance(location, l2))
        tot_distance = tot_distance + man_distance(location, l2)


print(tot_distance)
