with open(r"D:\Projects\advent_of_code\2024\inputs\D1206", 'r') as f:
    grid = f.readlines()

grid = [[char for char in line.strip()] for line in grid]

for i,line in enumerate(grid):
    for j,char in enumerate(line):
        if char == '^':
            start_position = (i,j)
            direction = 'N'

steps = set()
steps.add(start_position)
current_i, current_j = start_position

while True:
    if direction == 'N':
        next_position = (current_i-1,current_j)
    elif direction == 'E':
        next_position = (current_i,current_j+1)
    elif direction == 'S':
        next_position = (current_i+1,current_j)
    elif direction == 'W':
        next_position = (current_i,current_j-1)

    # next_position
    if next_position[0] <= len(grid)-1 and next_position[1] <= len(grid[0])-1:
        if grid[next_position[0]][next_position[1]] == '#' and direction == 'N':
            direction = 'E'
        elif grid[next_position[0]][next_position[1]] == '#' and direction == 'E':
            direction = 'S'
        elif grid[next_position[0]][next_position[1]] == '#' and direction == 'S':
            direction = 'W'
        elif grid[next_position[0]][next_position[1]] == '#' and direction == 'W':
            direction = 'N'
        else:
            steps.add(next_position)
            current_i, current_j = next_position
    else:
        break

# print(start_position)
# print(direction)
#
# print(len(grid[0]))

print(len(steps))
closed_loops = 0
steps.remove(start_position)
steps = list(steps)
for i, (x, y) in enumerate(steps):

    # if i == 5:
    # 1. Get new grid
    # 2. Start finding the number of steps and look for closed loops.
    # 3. Start tracking (x, y, direction)
    # print(f"{x} : {y}")
    # print(grid)
    grid[x][y] = '#'
    # print(grid)
    # new_grid = grid

    direction = 'N'
    state = (start_position[0], start_position[1], direction)
    current_i, current_j = start_position
    # print(state)
    state_steps = [state]

    while True:
        if direction == 'N':
            next_position = (current_i - 1, current_j)
        elif direction == 'E':
            next_position = (current_i, current_j + 1)
        elif direction == 'S':
            next_position = (current_i + 1, current_j)
        elif direction == 'W':
            next_position = (current_i, current_j - 1)

        # print(next_position)
        # next_position
        if next_position[0] <= len(grid) - 1 and next_position[1] <= len(grid[0]) - 1 and next_position[0] >= 0 and next_position[1] >= 0:
            if grid[next_position[0]][next_position[1]] == '#' and direction == 'N':
                direction = 'E'
            elif grid[next_position[0]][next_position[1]] == '#' and direction == 'E':
                direction = 'S'
            elif grid[next_position[0]][next_position[1]] == '#' and direction == 'S':
                direction = 'W'
            elif grid[next_position[0]][next_position[1]] == '#' and direction == 'W':
                direction = 'N'
            else:
                next_state = [next_position[0], next_position[1], direction]
                # print(next_state)
                if next_state in state_steps:
                    closed_loops += 1
                    grid[x][y] = '.'
                    break
                else:
                    state_steps.append(next_state)
                current_i, current_j = next_position
        else:
            grid[x][y] = '.'
            break

print(closed_loops)

