from heapq import heappush, heappop

grid = [list(map(int,line.strip()))for line in open("inputs/17_01_input.txt", 'r')]

# # print(grid)
# # heat, current row, current column, direction row, direction column, number of steps in direction
# start =[(0, 0, 0, 0, 0, 0)]
#
# seen = set()
#
# q = start
# # q.append((1,0,0,0,0,0))
# # print(q)
# def get_min_node():
#     global q
#     last_hl = float('inf')
#     for i, (hl, r, c, dr, dc, n) in enumerate(q):
#         if hl < last_hl:
#             min_node = q[i]
#             last_hl = hl
#
#     q.remove(min_node)
#     # print(min_node)
#     return min_node
#
# while q:
#     hl, r, c, dr, dc, n = get_min_node()
#
#     if r == len(grid) - 1 and c == len(grid[0]) -1:
#         print(hl)
#         break
#
#     if (r, c, dr, dc, n) in seen:
#         continue
#
#     seen.add((r, c, dr, dc, n))
#
#     if n < 3 and (dr,dc) != (0,0):
#         nr = r + dr
#         nc = c + dc
#         if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
#             q.append((hl + grid[nr][nc], nr, nc, dr, dc, n+1))
#
#     for ndr, ndc in [(1,0), (0,1), (-1,0), (0,-1)]:
#         # print('here')
#         if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
#             nr = r + ndr
#             nc = c + ndc
#             # print('here 1')
#             if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
#                 # print('here 2')
#                 q.append((hl + grid[nr][nc], nr, nc, ndr, ndc, 1))
#                 # print(q)



seen = set()
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    hl, r, c, dr, dc, n = heappop(pq)

    if r == len(grid) - 1 and c == len(grid[0]) - 1 and n>=4:
        print(hl)
        break

    if (r, c, dr, dc, n) in seen:
        continue

    seen.add((r, c, dr, dc, n))

    if n < 10 and (dr, dc) != (0, 0):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

    if n >= 4 or (dr,dc) == (0,0):
        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))