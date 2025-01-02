with open(r"D:\Projects\advent_of_code\2024\inputs\D1210", 'r') as f:
    t_map = f.readlines()

t_map = [[int(height) for height in row.strip()] for row in t_map]

# print(t_map)
from collections import deque
q = deque()

for i, row in enumerate(t_map):
    for j, height in enumerate(row):
        # print(i, j, height)
        if height == 0:
            # print(t_map[i][j])
            q.append((i, j))

# print(q)

score = 0

for x,y in q:
    q_1 = deque()
    q_1.append((x, y))
    # print('*******************')
    # print(x, y)
    seen = {(x,y)}
    while len(q_1) > 0:
        x,y = q_1.popleft()
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<len(t_map) and 0<=ny<len(t_map[0]):
                if t_map[nx][ny] - t_map[x][y] == 1:
                    # if (nx,ny) not in seen:
                    if t_map[nx][ny] == 9:
                        score += 1
                        # print(nx,ny)
                    else:
                        q_1.append((nx,ny))
                        # seen.add((nx,ny))
        # print(q_1)
    # print(score)
    # break

print(score)


# for x,y in q:
#     print(x,y)
#
#     for dx, dy in directions:
#         new_x, new_y = x+dx, y+dy
#         if new_x < 0 or new_x >= len(t_map) or new_y < 0 or new_y >= len(t_map[0]):
#             continue
#         else:
#             if t_map[new_x][new_y] == 9:
#                 score += 1
#             elif t_map[new_x][new_y] - t_map[x][y] == 1:
#                 q.append((new_x, new_y))
#
#     q.popleft()
#
# print(score)