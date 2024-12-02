maze = open("inputs/10_01_input.txt", 'r').read().strip().splitlines()

# find source
#

for r, line in enumerate(maze):
    if line.find('S') != -1:
        source_row = r
        source_column = line.find('S')

path = []

def next_step(pipe, row, column, prev_row, prev_column ):
    if pipe == '|':
        if prev_row < row:
            return row + 1, column
        else:
            return row - 1, column
    elif pipe == '-':
        if prev_column < column:
            return row, column + 1
        else:
            return row, column - 1
    elif pipe == 'L':
        if prev_row < row:
            return row, column + 1
        else:
            return row - 1, column
    elif pipe == 'J':
        if prev_row < row:
            return row, column - 1
        else:
            return row - 1, column
    elif pipe == '7':
        if prev_row > row:
            return row, column - 1
        else:
            return row + 1, column
    elif pipe == 'F':
        if prev_row > row:
            return row,column + 1
        else:
            return row + 1, column
    elif pipe == 'S':
        return -1,-1

pipe = S = '-'
row = source_row
column = source_column
prev_row = source_row
prev_column = source_column - 1

while row != -1:
    path.append((row, column))
    # print(next_step(pipe, row, column, prev_row, prev_column))
    next_row, next_column = next_step(pipe, row, column, prev_row, prev_column)
    pipe = maze[next_row][next_column]
    prev_row = row
    prev_column = column
    row = next_row
    column = next_column

print(len(set(path))//2)

maze = [''.join(pipe if (r,c) in path else '.' for c, pipe in enumerate(row))for r, row in enumerate(maze)]

print("\n".join(maze))
inside = 0
for r, row in enumerate(maze):
    for c, pipe in enumerate(row):
        if pipe == '.':
            crossing = 0
            bend = ''
            for ch in row[c:]:
                if ch == '|':
                    crossing = crossing +1
                elif ch == 'F' and bend == '':
                    bend = 'F'
                elif ch == '7' and bend == 'F':
                    bend = ''
                elif ch == 'J' and bend == 'F':
                    crossing = crossing + 1
                    bend = ''
                elif ch == 'L' and bend == '':
                    bend = 'L'
                elif ch == '7' and bend == 'L':
                    crossing = crossing + 1
                    bend = ''
                elif ch == 'J' and bend == 'L':
                    bend = ''

            if crossing%2==1:
                inside = inside + 1

print(inside)