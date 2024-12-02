from collections import deque
garden = open("inputs/21_01_input.txt", 'r').read().strip().splitlines()

garden = [[char for char in x] for x in garden]

for r, row in enumerate(garden):
    for c, col in enumerate(row):
        if col == 'S':
            sr = r
            sc = c

# q = deque([(sr,sc)])
seen=[]
next_q = set()
next_q.add((sr,sc))

for _ in range(64):
    q = deque(next_q)
    next_q = set()
    # print(q)
    while q:
        r, c = q.popleft()
        possible_steps = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

        for nr, nc in possible_steps:
            # print(nr, nc)
            if 0 <= nr < len(garden):
                if 0 <= nc < len(garden[0]):
                    if garden[nr][nc] != '#':
                        next_q.add((nr,nc))
                        # seen.append([nr,nc])

print(len(next_q))
        # print(q)
        # break
    # print(len(seen))
