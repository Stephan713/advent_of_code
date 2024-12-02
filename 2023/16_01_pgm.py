from collections import deque

grid = open("inputs/16_01_input.txt", 'r').read().strip().splitlines()

# print('\n'.join(grid))


def get_energy_mirrors(r, c, dr, dc):
    start = [(r, c, dr, dc)]  # row, column, direction row and direction column
    seen = set()
    q = deque(start)

    while q:
        r,c, dr, dc = q.popleft()

        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        panel = grid[r][c]

        if panel == '.' or (panel == '-' and dc != 0) or (panel == '|' and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif panel == '/':
            if dr == 0 and dc == 1: # moving right
                dr = -1
                dc = 0
            elif dr == 1 and dc == 0: # moving down
                dr = 0
                dc = -1
            elif dr == 0 and dc == -1: # moving left
                dr = 1
                dc = 0
            elif dr == -1 and dc == 0: # moving up
                dr = 0
                dc = 1
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif panel == '\\':
            if dr == 0 and dc == 1: # moving right
                dr = 1
                dc = 0
            elif dr == 1 and dc == 0: # moving down
                dr = 0
                dc = 1
            elif dr == 0 and dc == -1: # moving left
                dr = -1
                dc = 0
            elif dr == -1 and dc == 0: # moving up
                dr = 0
                dc = -1
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif panel == '|':
            # up
            dr = -1
            dc = 0
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))

            # down
            dr = 1
            dc = 0
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif panel == '-':
            # right
            dr = 0
            dc = 1
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))

            # left
            dr = 0
            dc = -1
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))

    dedup_seen = {(r,c) for (r,c, _, _) in seen}

    return len(dedup_seen)

max_mirrors = 0

for r in range(len(grid)):
    max_mirrors = max(max_mirrors, get_energy_mirrors(r, -1, 0, 1))
    max_mirrors = max(max_mirrors, get_energy_mirrors(r, len(grid[r]), 0, -1))

for col in range(len(grid[0])):
    max_mirrors = max(max_mirrors, get_energy_mirrors(-1, col, 1, 0))
    max_mirrors = max(max_mirrors, get_energy_mirrors(len(grid), col,  -1, 0))

print(max_mirrors)