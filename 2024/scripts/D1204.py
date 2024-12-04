import re

with open(r"D:\Projects\advent_of_code\2024\inputs\D1204", 'r') as f:
    puzzle = f.readlines()

puzzle = [p.strip() for p in puzzle]
horizontal = puzzle

horizontal_backwards = [""] * len(puzzle)

for i,line in enumerate(horizontal):
    horizontal_backwards[i] = line[::-1]

vertical = [""] * len(puzzle[0])

for line in puzzle:
    for i,char in enumerate(line):
        # print(i)
        vertical[i] += char

vertical_backwards = [""] * len(vertical)
for i,line in enumerate(vertical):
    vertical_backwards[i] = line[::-1]


diagonal_right = [""]*(2*len(horizontal)-1)
for i,line in enumerate(horizontal):
    for j,char in enumerate(line):
        diagonal_right[i+j] += char

diagonal_right_backwards  = [""]*len(diagonal_right)
for i,line in enumerate(diagonal_right):
    diagonal_right_backwards[i] = line[::-1]

diagonal_left = [""]*(2*len(horizontal_backwards)-1)
for i,line in enumerate(horizontal_backwards):
    for j,char in enumerate(line):
        diagonal_left[i+j] += char

diagonal_left_backwards = [""]*len(diagonal_left)
for i,line in enumerate(diagonal_left):
    diagonal_left_backwards[i] = line[::-1]


puzzle_all = [horizontal,
              horizontal_backwards,
              vertical,
              vertical_backwards,
              diagonal_right,
              diagonal_right_backwards,
              diagonal_left,
              diagonal_left_backwards]

pattern = r'XMAS'
total_matches = 0

for puzzle_d in puzzle_all:
    for line in puzzle_d:
        matches = re.findall(pattern, line)
        total_matches += len(matches)


print(total_matches)
puzzle = [[char for char in line] for line in puzzle]

# print(puzzle)
xmas_count = 0
# print(len(puzzle[0]))
for i in range(0,len(puzzle)-2):
    for j in range(0,len(puzzle[i])-2):
        string = puzzle[i][j] + puzzle[i+1][j+1] + puzzle[i+2][j+2] + puzzle[i][j+2] + puzzle[i+2][j]
        # print(string)
        if string in ['MASMS','MASSM', 'SAMMS', 'SAMSM']:
            xmas_count += 1

print(xmas_count)
# print(horizontal)
# print(vertical)
# print(horizontal_backwards)
# print(vertical_backwards)
# print(diagonal_right)
# print(diagonal_right_backwards)
# print(diagonal_left)
# print(diagonal_left_backwards)